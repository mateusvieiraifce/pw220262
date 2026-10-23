from sqlalchemy import  Column, Integer, String
from models.Conexao import Base
from flask_login import UserMixin

class Usuario(Base, UserMixin):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    usuario = Column(String(50))
    senha = Column(String(200))
    def __init__(self, id, usuario, nome, senha):
        self.id = id
        self.usuario = usuario
        self.nome = nome
        self.senha = senha