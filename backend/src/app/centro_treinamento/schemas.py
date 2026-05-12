from typing import Annotated
#typing serve para adicionar informações e considerações sobre as tipagens em python
from pydantic import UUID4, Field

from app.contrib.schemas import BaseSchema 
#pydantic serve para validar se os dados inseridos na API estão corretos



class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT king', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua x, 02', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do centro de treinamento', example='Marcos', max_length=30)]
  
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT king', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]