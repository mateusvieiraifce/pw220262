from sqlalchemy import  Column, Integer, String
from models.Conexao import Base

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    cpf = Column(String(14))
    endereco = Column(String(300))
    tel = Column(String(20))
    email = Column(String(50))
    