from typing import Annotated, Optional
#typing serve para adicionar informações e considerações sobre as tipagens em python
from pydantic import Field, PositiveFloat

from app.categorias.schemas import CategoriaIn
from app.centro_treinamento.schemas import CentroTreinamentoAtleta
from app.contrib.schemas import BaseSchema, OutMixin 
#pydantic serve para validar se os dados inseridos na API estão corretos



class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]
 
 
class AtletaIn(Atleta):
    pass
 
 
class AtletaOut(Atleta, OutMixin):
    pass
 
 
class AtletaOutCustom(BaseSchema, OutMixin):
    """Schema para GET ALL — retorna apenas nome, centro de treinamento e categoria."""
    nome: Annotated[str, Field(description='Nome do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
 
 
class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='João', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]