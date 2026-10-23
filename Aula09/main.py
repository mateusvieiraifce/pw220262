from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MALHADAO_DO_NORDESTE'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from models import Usuario, Produto, Cliente, Fornecedor
from models.Conexao import engine, Base

Session = sessionmaker(bind=engine)

#1. Crie uma rota que retorne 
# uma mensagem Escrito "Olá Mundo"

@login_manager.user_loader
def load_user(user_id):
    session = Session()
    return session.get(Usuario.Usuario, int(user_id))

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("email")
        password = request.form.get("senha")

        session = Session()
        user = session.query(Usuario.Usuario).filter_by(usuario=username).first()
        if user and check_password_hash(user.senha, password):
            login_user(user)
            return render_template("index.html")
        else:
            return render_template("login.html", error="Usuário ou senha inválidos.")
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


@app.route("/produto/cadastro", methods=["GET", "POST"])
def cadastro_produto():
    return render_template("/produtos/cad.html")

@app.route("/produtos", methods=["GET", "POST"])
def list_produto():
    session = Session()
    all = session.query(Produto.Produtos).all() 

    return render_template("/produtos/list.html", produtos=all)


from controllers.UsuarioController import *
from controllers.PacienteController import *
from controllers.TipoMaterialController import *

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True, port=5001)