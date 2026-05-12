from uuid import uuid4
# gera um ID único universal aleatório para identificar registros
from sqlalchemy import UUID
# tipo de coluna UUID genérico do SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# DeclarativeBase: classe base para criar os modelos de tabela (ORM)
# Mapped: define o tipo Python da coluna
# mapped_column: configura as propriedades da coluna no banco
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)