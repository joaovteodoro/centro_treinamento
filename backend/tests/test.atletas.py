import pytest
from httpx import AsyncClient


# ── POST ──────────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_criar_atleta(client: AsyncClient, atleta_fixture):
    assert atleta_fixture["nome"] == "João Silva"
    assert atleta_fixture["cpf"] == "12345678900"
    assert "id" in atleta_fixture


@pytest.mark.asyncio
async def test_criar_atleta_cpf_duplicado(client: AsyncClient, categoria_fixture, centro_fixture):
    payload = {
        "nome": "Maria",
        "cpf": "11111111111",
        "idade": 22,
        "peso": 60.0,
        "altura": 1.65,
        "sexo": "F",
        "categoria": {"nome": categoria_fixture["nome"]},
        "centro_treinamento": {"nome": centro_fixture["nome"]}
    }
    await client.post("/atletas/", json=payload)
    response = await client.post("/atletas/", json=payload)
    assert response.status_code == 303


@pytest.mark.asyncio
async def test_criar_atleta_categoria_inexistente(client: AsyncClient, centro_fixture):
    response = await client.post("/atletas/", json={
        "nome": "Teste",
        "cpf": "99999999999",
        "idade": 20,
        "peso": 70.0,
        "altura": 1.70,
        "sexo": "M",
        "categoria": {"nome": "Inexistente"},
        "centro_treinamento": {"nome": centro_fixture["nome"]}
    })
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_criar_atleta_centro_inexistente(client: AsyncClient, categoria_fixture):
    response = await client.post("/atletas/", json={
        "nome": "Teste",
        "cpf": "88888888888",
        "idade": 20,
        "peso": 70.0,
        "altura": 1.70,
        "sexo": "M",
        "categoria": {"nome": categoria_fixture["nome"]},
        "centro_treinamento": {"nome": "Inexistente"}
    })
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_criar_atleta_campo_faltando(client: AsyncClient):
    response = await client.post("/atletas/", json={"nome": "Incompleto"})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_criar_atleta_peso_negativo(client: AsyncClient, categoria_fixture, centro_fixture):
    response = await client.post("/atletas/", json={
        "nome": "Teste",
        "cpf": "77777777777",
        "idade": 20,
        "peso": -10.0,
        "altura": 1.70,
        "sexo": "M",
        "categoria": {"nome": categoria_fixture["nome"]},
        "centro_treinamento": {"nome": centro_fixture["nome"]}
    })
    assert response.status_code == 422


# ── GET ALL ───────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_listar_atletas(client: AsyncClient, atleta_fixture):
    response = await client.get("/atletas/")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert data["total"] >= 1


@pytest.mark.asyncio
async def test_filtrar_atleta_por_nome(client: AsyncClient, atleta_fixture):
    response = await client.get("/atletas/?nome=João")
    assert response.status_code == 200
    items = response.json()["items"]
    assert any("João" in a["nome"] for a in items)


@pytest.mark.asyncio
async def test_filtrar_atleta_por_cpf(client: AsyncClient, atleta_fixture):
    response = await client.get("/atletas/?cpf=12345678900")
    assert response.status_code == 200
    items = response.json()["items"]
    assert len(items) >= 1


@pytest.mark.asyncio
async def test_filtrar_atleta_inexistente(client: AsyncClient):
    response = await client.get("/atletas/?nome=NomeQueNaoExiste")
    assert response.status_code == 200
    assert response.json()["total"] == 0


# ── GET BY ID ─────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_buscar_atleta_por_id(client: AsyncClient, atleta_fixture):
    atleta_id = atleta_fixture["id"]
    response = await client.get(f"/atletas/{atleta_id}")
    assert response.status_code == 200
    assert response.json()["id"] == atleta_id


@pytest.mark.asyncio
async def test_buscar_atleta_inexistente(client: AsyncClient):
    response = await client.get("/atletas/00000000-0000-0000-0000-000000000001")
    assert response.status_code == 404


# ── PATCH ─────────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_atualizar_atleta(client: AsyncClient, atleta_fixture):
    atleta_id = atleta_fixture["id"]
    response = await client.patch(f"/atletas/{atleta_id}", json={"nome": "João Atualizado", "idade": 30})
    assert response.status_code == 200
    assert response.json()["nome"] == "João Atualizado"
    assert response.json()["idade"] == 30


@pytest.mark.asyncio
async def test_atualizar_atleta_inexistente(client: AsyncClient):
    response = await client.patch(
        "/atletas/00000000-0000-0000-0000-000000000001",
        json={"nome": "Teste"}
    )
    assert response.status_code == 404


# ── DELETE ────────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_deletar_atleta(client: AsyncClient, categoria_fixture, centro_fixture):
    response = await client.post("/atletas/", json={
        "nome": "Atleta Del",
        "cpf": "55555555555",
        "idade": 28,
        "peso": 80.0,
        "altura": 1.80,
        "sexo": "M",
        "categoria": {"nome": categoria_fixture["nome"]},
        "centro_treinamento": {"nome": centro_fixture["nome"]}
    })
    atleta_id = response.json()["id"]
    delete_response = await client.delete(f"/atletas/{atleta_id}")
    assert delete_response.status_code == 204


@pytest.mark.asyncio
async def test_deletar_atleta_inexistente(client: AsyncClient):
    response = await client.delete("/atletas/00000000-0000-0000-0000-000000000001")
    assert response.status_code == 404