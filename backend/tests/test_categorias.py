import pytest
from httpx import AsyncClient


# ── POST ──────────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_criar_categoria(client: AsyncClient):
    response = await client.post("/categorias/", json={"nome": "Rx"})
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Rx"
    assert "id" in data


@pytest.mark.asyncio
async def test_criar_categoria_duplicada(client: AsyncClient):
    await client.post("/categorias/", json={"nome": "Duplicada"})
    response = await client.post("/categorias/", json={"nome": "Duplicada"})
    assert response.status_code == 303


@pytest.mark.asyncio
async def test_criar_categoria_nome_muito_longo(client: AsyncClient):
    response = await client.post("/categorias/", json={"nome": "NomeMuitoLongoParaCategoria"})
    assert response.status_code == 422


# ── GET ALL ───────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_listar_categorias(client: AsyncClient, categoria_fixture):
    response = await client.get("/categorias/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


# ── GET BY ID ─────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_buscar_categoria_por_id(client: AsyncClient, categoria_fixture):
    categoria_id = categoria_fixture["id"]
    response = await client.get(f"/categorias/{categoria_id}")
    assert response.status_code == 200
    assert response.json()["id"] == categoria_id


@pytest.mark.asyncio
async def test_buscar_categoria_inexistente(client: AsyncClient):
    response = await client.get("/categorias/550e8400-e29b-41d4-a716-446655440000")
    assert response.status_code == 404


# ── DELETE ────────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_deletar_categoria(client: AsyncClient):
    response = await client.post("/categorias/", json={"nome": "Deletar"})
    categoria_id = response.json()["id"]
    delete_response = await client.delete(f"/categorias/{categoria_id}")
    assert delete_response.status_code == 204


@pytest.mark.asyncio
async def test_deletar_categoria_inexistente(client: AsyncClient):
    response = await client.delete("/categorias/550e8400-e29b-41d4-a716-446655440000")
    assert response.status_code == 404