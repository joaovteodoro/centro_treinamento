import asyncio
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import text
from app.configs.settings import settings

engine = create_async_engine(settings.DB_URL, echo=False)

async_session = async_sessionmaker(   
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session


async def test_connection():
    try:
        async with engine.connect() as connection:
            result = await connection.execute(text("SELECT version();"))
            print("Conexão bem-sucedida!")
            print("Versão do PostgreSQL:", result.fetchone())
    except Exception as e:
        print("Erro na conexão:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())