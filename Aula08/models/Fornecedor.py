from sqlalchemy import  Column, Integer, String
from models.Conexao import Base

class Fornecedor(Base):
    __tablename__ = "fornecedor"
    id = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String(50))
    fantasia = Column(String(50))
    cnpj = Column(String(18))
    IE = Column(String(18))
    endereco = Column(String(300))
    tel = Column(String(20))
    email = Column(String(50))
    