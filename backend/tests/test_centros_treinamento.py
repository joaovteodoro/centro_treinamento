import pytest
from httpx import AsyncClient


# ── POST ──────────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_criar_centro(client: AsyncClient):
    response = await client.post("/centros_treinamento/", json={
        "nome": "CT Zero",
        "endereco": "Rua B, 20",
        "proprietario": "Pedro"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "CT Zero"
    assert "id" in data


@pytest.mark.asyncio
async def test_criar_centro_duplicado(client: AsyncClient):
    payload = {"nome": "CT Dup", "endereco": "Rua C, 1", "proprietario": "Ana"}
    await client.post("/centros_treinamento/", json=payload)
    response = await client.post("/centros_treinamento/", json=payload)
    assert response.status_code == 303


@pytest.mark.asyncio
async def test_criar_centro_campo_faltando(client: AsyncClient):
    response = await client.post("/centros_treinamento/", json={"nome": "CT Incompleto"})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_criar_centro_nome_muito_longo(client: AsyncClient):
    response = await client.post("/centros_treinamento/", json={
        "nome": "Nome muito longo para um centro de treinamento",
        "endereco": "Rua D, 5",
        "proprietario": "Carlos"
    })
    assert response.status_code == 422


# ── GET ALL ───────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_listar_centros(client: AsyncClient, centro_fixture):
    response = await client.get("/centros_treinamento/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


# ── GET BY ID ─────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_buscar_centro_por_id(client: AsyncClient, centro_fixture):
    centro_id = centro_fixture["id"]
    response = await client.get(f"/centros_treinamento/{centro_id}")
    assert response.status_code == 200
    assert response.json()["id"] == centro_id


@pytest.mark.asyncio
async def test_buscar_centro_inexistente(client: AsyncClient):
    response = await client.get("/centros_treinamento/550e8400-e29b-41d4-a716-446655440000")
    assert response.status_code == 404


# ── DELETE ────────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_deletar_centro(client: AsyncClient):
    response = await client.post("/centros_treinamento/", json={
        "nome": "CT Del",
        "endereco": "Rua E, 3",
        "proprietario": "Lucas"
    })
    centro_id = response.json()["id"]
    delete_response = await client.delete(f"/centros_treinamento/{centro_id}")
    assert delete_response.status_code == 204


@pytest.mark.asyncio
async def test_deletar_centro_inexistente(client: AsyncClient):
    response = await client.delete("/centros_treinamento/550e8400-e29b-41d4-a716-446655440000")
    assert response.status_code == 404