import asyncio
import sys
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.main import app
from app.contrib.models import BaseModel
from app.contrib.dependencies import get_session

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine_test = create_async_engine(DATABASE_URL, echo=False)
async_session_test = async_sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(autouse=True)
async def reset_tables():
    """Recria as tabelas antes de cada teste — garante banco limpo."""
    async with engine_test.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)
    yield


@pytest_asyncio.fixture
async def db_session():
    async with async_session_test() as session:
        yield session


@pytest_asyncio.fixture
async def client(db_session):
    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_overrides.clear()


# ── Fixtures de dados ──────────────────────────────────────────────────────────

@pytest_asyncio.fixture
async def categoria_fixture(client):
    response = await client.post("/categorias/", json={"nome": "Scale"})
    assert response.status_code == 201
    return response.json()


@pytest_asyncio.fixture
async def centro_fixture(client):
    response = await client.post("/centros_treinamento/", json={
        "nome": "CT King",
        "endereco": "Rua A, 10",
        "proprietario": "Marcos"
    })
    assert response.status_code == 201
    return response.json()


@pytest_asyncio.fixture
async def atleta_fixture(client, categoria_fixture, centro_fixture):
    response = await client.post("/atletas/", json={
        "nome": "João Silva",
        "cpf": "12345678900",
        "idade": 25,
        "peso": 75.5,
        "altura": 1.75,
        "sexo": "M",
        "categoria": {"nome": categoria_fixture["nome"]},
        "centro_treinamento": {"nome": centro_fixture["nome"]}
    })
    assert response.status_code == 201
    return response.json()