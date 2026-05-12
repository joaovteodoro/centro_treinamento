from typing import Annotated
#typing serve para adicionar informações e considerações sobre as tipagens em python
from pydantic import UUID4, Field

from app.contrib.schemas import BaseSchema 
#pydantic serve para validar se os dados inseridos na API estão corretos



class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]
 
 
class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]
 