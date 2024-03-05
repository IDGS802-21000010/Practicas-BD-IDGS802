from flask import Flask, request,render_template, Response, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

from flask import flash
from models import db
from flask import g
from models import Alumnos, Maestros

import forms
app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
#app.secret_key="esta es la clave secreta"
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index", methods=["GET", "POST"])
def indexAlum():
    alum_form=forms.UserForm2(request.form)
    if request.method=='POST' and alum_form.validate():
        alum=Alumnos(nombre=alum_form.nombre.data, apaterno = alum_form.apaterno.data,
                 email = alum_form.email.data)
        #insert into alumnos values()
        db.session.add(alum)
        db.session.commit()
    return render_template("index2.html", form=alum_form)

@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABCCompleto():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    maestro = Maestros.query.all()

    return render_template("ABC_Completo.html", Alumnos=alumno, Maestros=maestro)

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    nom=""
    correo=""
    apa=""
    alum_form=forms.UserForm(request.form)
    if request.method=='POST'and alum_form.validate():
        nom=alum_form.nombre.data
        correo=alum_form.email.data
        apa=alum_form.apaterno.data
        mensaje = 'Bienvenido: {}'.format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom))
        print("apaterno: {}".format(apa))
        print("correo: {}".format(correo))
    return render_template("alumnos.html", form=alum_form, nom=nom, correo=correo, apa=apa)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    #app.run(debug=True)
    app.run()