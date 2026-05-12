import pytest
from pydantic import ValidationError

from app.atleta.schemas import AtletaIn
from app.categorias.schemas import CategoriaIn
from app.centro_treinamento.schemas import CentroTreinamentoIn


# ── CategoriaIn ───────────────────────────────────────────────────────────────

def test_categoria_schema_valido():
    c = CategoriaIn(nome="Scale")
    assert c.nome == "Scale"


def test_categoria_schema_nome_muito_longo():
    with pytest.raises(ValidationError):
        CategoriaIn(nome="NomeMuitoLongoParaCategoria")


def test_categoria_schema_campo_extra_proibido():
    with pytest.raises(ValidationError):
        CategoriaIn(nome="Scale", campo_extra="valor")


# ── CentroTreinamentoIn ───────────────────────────────────────────────────────

def test_centro_schema_valido():
    c = CentroTreinamentoIn(nome="CT King", endereco="Rua A, 1", proprietario="Marcos")
    assert c.nome == "CT King"


def test_centro_schema_campo_faltando():
    with pytest.raises(ValidationError):
        CentroTreinamentoIn(nome="CT King")


def test_centro_schema_nome_muito_longo():
    with pytest.raises(ValidationError):
        CentroTreinamentoIn(
            nome="Nome muito longo para um centro",
            endereco="Rua A, 1",
            proprietario="Marcos"
        )


# ── AtletaIn ──────────────────────────────────────────────────────────────────

def test_atleta_schema_valido():
    a = AtletaIn(
        nome="João",
        cpf="12345678900",
        idade=25,
        peso=75.5,
        altura=1.75,
        sexo="M",
        categoria={"nome": "Scale"},
        centro_treinamento={"nome": "CT King"}
    )
    assert a.nome == "João"


def test_atleta_schema_peso_negativo():
    with pytest.raises(ValidationError):
        AtletaIn(
            nome="João",
            cpf="12345678900",
            idade=25,
            peso=-10.0,
            altura=1.75,
            sexo="M",
            categoria={"nome": "Scale"},
            centro_treinamento={"nome": "CT King"}
        )


def test_atleta_schema_altura_negativa():
    with pytest.raises(ValidationError):
        AtletaIn(
            nome="João",
            cpf="12345678900",
            idade=25,
            peso=75.0,
            altura=-1.0,
            sexo="M",
            categoria={"nome": "Scale"},
            centro_treinamento={"nome": "CT King"}
        )


def test_atleta_schema_nome_muito_longo():
    with pytest.raises(ValidationError):
        AtletaIn(
            nome="N" * 51,
            cpf="12345678900",
            idade=25,
            peso=75.0,
            altura=1.75,
            sexo="M",
            categoria={"nome": "Scale"},
            centro_treinamento={"nome": "CT King"}
        )


def test_atleta_schema_cpf_muito_longo():
    with pytest.raises(ValidationError):
        AtletaIn(
            nome="João",
            cpf="123456789001",
            idade=25,
            peso=75.0,
            altura=1.75,
            sexo="M",
            categoria={"nome": "Scale"},
            centro_treinamento={"nome": "CT King"}
        )