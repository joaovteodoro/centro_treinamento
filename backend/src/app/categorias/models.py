from sqlalchemy import Integer, String
#sqlalchemy serve para interagir com bancos de dados relacionais sem precisar escrever SQL puro no código
from sqlalchemy.orm import Mapped, mapped_column, relationship
#sqlalchemy.orm serve para representar as tabelas dos bancos de dados como classes
from app.contrib.models import BaseModel
#BaseModel é uma classe interna, que está dentro da pasta contrib


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'
    pk_id: Mapped[int] = mapped_column (Integer, primary_key = True)
    nome: Mapped[str] = mapped_column (String(50), unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
    
