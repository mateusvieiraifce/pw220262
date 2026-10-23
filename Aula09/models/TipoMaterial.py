from sqlalchemy import  Column, Integer, String
from models.Conexao import Base

class TipoMaterial(Base):
    __tablename__ = "tipoMaterial"
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(50))
   