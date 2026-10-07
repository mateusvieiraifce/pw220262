from sqlalchemy import  Column, Integer, String
from models.Conexao import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    usuario = Column(String(50))
    senha = Column(String(50))