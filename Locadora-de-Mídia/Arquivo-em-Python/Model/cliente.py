from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)

    locacoes = relationship("Locacao", back_populates="cliente", cascade="all, delete-orphan")

    def desativar(self):
        self.ativo = False
