from flask import  render_template, request
from models import Paciente
from main import app, Session


@app.route("/paciente/cadastro", methods=["GET", "POST"])
def cadastro_paciente():
    return render_template("/pacientes/cad.html")

@app.route("/pacientes/salvar", methods=[ "POST"])
def salvar_paciente():
    obj = Paciente.Paciente(nome=request.form['nome'], 
                   cpf=request.form['CPF'])
    session = Session() 
    session.add(obj)
    session.commit()

    return listar_pacientes("Paciente cadastrado com sucesso!!");
    
@app.route("/pacientes/listar", methods=["GET"])
def listar_pacientes(msg=None):
    
    pacientes = Session().query(Paciente.Paciente).all();
    return render_template("/pacientes/list.html", pacientes=pacientes, msg=msg)

@app.route("/paciente/deletar/<id>", methods=[ "GET"])
def deletar_paciente(id):
    session = Session() 
    paciente = session.get(Paciente.Paciente, id)
    if paciente:
        session.delete(paciente)
        session.commit()
    else:
        return listar_pacientes("paciente nao existe!")
    return listar_pacientes("Paciente apagado com sucesso!!")