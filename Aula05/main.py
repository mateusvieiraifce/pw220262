from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
app = Flask(__name__)

from models import Usuario, Produto, Cliente, Fornecedor
from models.Conexao import engine, Base

Session = sessionmaker(bind=engine)

#1. Crie uma rota que retorne 
# uma mensagem Escrito "Olá Mundo"


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


#2. Crie uma rota que receba como paramento,
#  o nome e retorne "Seja Bem vindo, pararecebido"
@app.route("/param/<nome>")
def nome(nome):
    return " Seja bem vindo: " + nome

#3. crie uma rota que receba o nome, 
# o peso a altura e retorne: 
# Uma pagina html com fundo rosa com a mensagem: 
# "Seu nome, seu imc: ", 


@app.route("/calcular_imc", methods=["GET", "POST"])
def pre_imc():
    if request.method == "POST":
        nome = request.form.get("nome")
        altura = request.form.get("altura")
        peso = request.form.get("peso")
        imc = float(peso)/(float(altura)*float(altura))
        imcF = f"{imc:.2f}"
        return render_template("imcFormulario.html", imc=imcF, nome=nome, altura=altura, peso=peso)
    else:
        return render_template("imcFormulario.html")

@app.route("/imc/<nome>/<altura>/<peso>")
def imc(nome, altura, peso):
    imc = float(peso)/(float(altura)*float(altura))
    imcF = f"{imc:.2f}"
    return render_template("imc.html", 
                           nome=nome, imc=imcF)


@app.route("/usuario/cadastro", methods=["GET", "POST"])
def cadastro():
    return render_template("cadastro_user.html")

@app.route("/usuario/salvar", methods=[ "POST"])
def salvar():
    obj = Usuario.Usuario(nome=request.form['nome'], 
                  usuario=request.form['usuario'], 
                  senha=request.form['senha'])
    session = Session() 
    session.add(obj)
    session.commit()

    return lista_usuarios()

    
@app.route("/usuario/deletar/<id>", methods=[ "GET"])
def deletar(id):
    session = Session() 
    user = session.get(Usuario.Usuario, id)
    if user:
        session.delete(user)
        session.commit()
    else:
        return lista_usuarios("usuário nao existe!")
    return lista_usuarios("Usuário apagado com sucesso!!")

@app.route("/usuarios", methods=["GET", "POST"])
def lista_usuarios(msg=None):
    session = Session() 
    all = session.query(Usuario.Usuario).all()
    return render_template("lista_user.html", usuarios=all, msg = msg)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True, port=5001)