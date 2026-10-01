from sqlalchemy import  Column, Integer, String
from models.Conexao import Base

class Paciente(Base):
    __tablename__ = "paciente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    cpf = Column(String(50))
    