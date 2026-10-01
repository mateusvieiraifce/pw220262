from flask import  render_template, request
from models import Usuario
from main import app, Session


@app.route("/usuario/cadastro", methods=["GET", "POST"])
def cadastro():
    return render_template("/usuarios/cad.html")

@app.route("/usuario/salvar", methods=[ "POST"])
def salvar():
    
    if request.form.get('id'):
        session = Session() 
        user = session.get(Usuario.Usuario, request.form.get('id'))
        if user:
            user.nome = request.form['nome']
            user.usuario = request.form['usuario']
            session.commit()
            return lista_usuarios("Usuário editado com sucesso!!")
    else:
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

@app.route("/usuario/editar/<id>", methods=[ "GET"])
def pre_editar(id):
    session = Session() 
    user = session.get(Usuario.Usuario, id)
    if user:
        return render_template("/usuarios/cad.html", usuario=user)
    else:
        return lista_usuarios("usuário nao existe!")
    
@app.route("/usuarios", methods=["GET", "POST"])
def lista_usuarios(msg=None):
    session = Session() 
    all = session.query(Usuario.Usuario).all()
    return render_template("usuarios/list.html", usuarios=all, msg = msg)