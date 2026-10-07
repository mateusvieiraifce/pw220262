from sqlalchemy import  Column, Integer, String
from models.Conexao import Base

class Produtos(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(50))
    descricao = Column(String(50))
    preco = Column(String(50))