from flask import Flask, render_template, request
app = Flask(__name__)

#1. Crie uma rota que retorne 
# uma mensagem Escrito "Olá Mundo"

@app.route("/")
def index():
    return "ola mundo"


#2. Crie uma rota que receba como paramento,
#  o nome e retorne "Seja Bem vindo, pararecebido"
@app.route("/param/<nome>")
def nome(nome):
    return " Seja bem vindo: " + nome

#3. crie uma rota que receba o nome, 
# o peso a altura e retorne: 
# Uma pagina html com fundo rosa com a mensagem: 
# "Seu nome, seu imc: ", 

@app.route("/imc/<nome>/<altura>/<peso>")
def imc(nome, altura, peso):
    imc = float(peso)/(float(altura)*float(altura))
    imcF = f"{imc:.2f}"
    return render_template("imc.html", 
                           nome=nome, imc=imcF)


app.run(debug=True)