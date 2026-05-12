from datetime import datetime
#datatime serve para manipular data e hora
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
#sqlalchemy serve para interagir com bancos de dados relacionais sem precisar escrever SQL puro no código
from sqlalchemy.orm import Mapped, mapped_column, relationship
#sqlalchemy.orm serve para representar as tabelas dos bancos de dados como classes
from app.contrib.models import BaseModel



class AtletaModel(BaseModel):
    __tablename__ = 'atletas'
 
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)    
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)  
    
    #Mapped['XxModel'] permite acessar o objeto de outra classe. back_populates cria o caminho reverso também
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta', lazy='selectin')
    #Necessário criar a linha acima, para poder apontar para a ForeignKey de outra tabela
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
 
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta', lazy='selectin')
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id'))
 