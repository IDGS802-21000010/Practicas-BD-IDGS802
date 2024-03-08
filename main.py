from flask import Flask, request,render_template, Response, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

from flask import flash
from models import db
from flask import g
from models import Alumnos, Maestros, Pizzeriadominos
from datetime import datetime, date

import forms
app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
#app.secret_key="esta es la clave secreta"
csrf=CSRFProtect()
Pizzas = []

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

@app.route("/pizzeria", methods=["GET", "POST"])
def pizza():
    pz_form=forms.PizzaForm(request.form)
    global Pizzas 
    Pedidos = Pizzeriadominos.query.filter(db.func.date(Pizzeriadominos.fechaPedido) == date.today()).all()
    ingre = {
        'Pinia':10,
        'Jamon':10,
        'Champiniones':10
    }
    tam = {
        'Chica':40,
        'Mediana':80,
        'Grande':120
    }
    filtradoDia = {
        'na':'na',
        'Lunes':'Monday',
        'Martes':'Tuesday',
        'Miercoles':'Wednesday',
        'Jueves':'Thursday',
        'Viernes':'Friday',
        'Sabado':'Saturday',
        'Domingo':'Sunday'
    }
    insertDia = {
        'Monday':'Lunes',
        'Tuesday':'Martes',
        'Wednesday':'Miercoles',
        'Thursday':'Jueves',
        'Friday':'Viernes',
        'Saturday':'Sabado',
        'Sunday':'Domingo'
    }
    filtradoMes = {
        'na':'na',
        'Enero':'January',
        'Febrero':'February',
        'Marzo':'March',
        'Abril':'April',
        'Mayo':'May',
        'Junio':'June',
        'Julio':'July',
        'Agosto':'August',
        'Septiembre':'September',
        'Octubre':'October',
        'Noviembre':'November',
        'Diciembre':'December',
    }
    insertMes = {
        'January':'Enero',
        'February':'Febrero',
        'March':'Marzo',
        'April':'Abril',
        'May':'Mayo',
        'June':'Junio',
        'July':'Julio',
        'August':'Agosto',
        'September':'Septiembre',
        'October':'Octubre',
        'November':'Noviembre',
        'December':'Diciembre',
    }
    tamP=''
    ingdP=''
    numPizzas=0
    subT=0
    diaBuscar=''
    mesBuscar=''
    fecha=''
    totalD = sum(pedido.total for pedido in Pedidos)
    Registros = Pizzeriadominos.query.filter(db.func.date(Pizzeriadominos.fechaPedido) == date.today()).all()
    day = ''

    if request.method=='POST' and pz_form.validate:
        if request.form['buttonP'] == "btnAgregar":
            tamP=pz_form.tamP.data
            ingdP=pz_form.ingdP.data
            numPizzas=pz_form.numPizzas.data
            tmV = tam[tamP]
            totalI = sum(ingre.get(option, 0) for option in ingdP)
            subT=(numPizzas*(int(tmV)+totalI))

            Pizzas.append({ 
                           'tamP': tamP, 
                           'ingdP':ingdP, 
                           'numPizzas': numPizzas, 
                           'subT':subT
                           }
            )
            pz_form.tamP.data = None
            pz_form.ingdP.data = None
            pz_form.numPizzas.data = None

        if request.form['buttonP'] == "btnQuitar":
            indexEliminar = request.form.getlist('eliminar[]')
            indexEliminar = [int(index) for index in indexEliminar]
            Pizzas = [pizza for i, pizza in enumerate(Pizzas, 1) if i not in indexEliminar]

        if request.form['buttonP'] == "btnTerminar":
            if Pizzas:
                totalP = sum(pizza['subT'] for pizza in Pizzas)
                #pz_form.fechaRegistro.data
                d = insertDia[pz_form.fechaRegistro.data.strftime("%A")]
                m = insertMes[pz_form.fechaRegistro.data.strftime("%B")]
                ped=Pizzeriadominos(nombre=pz_form.nombreP.data, direccion=pz_form.direccionP.data, telefono=pz_form.telefonoP.data,
                                    total=totalP, fechaPedido=pz_form.fechaRegistro.data, dia=d, mes=m)
                db.session.add(ped)
                db.session.commit()
                Pizzas.clear()
                pz_form.tamP.data = None
                pz_form.ingdP.data = None
                pz_form.numPizzas.data = 1
                pz_form.nombreP.data = None
                pz_form.direccionP.data = None
                pz_form.telefonoP.data = None
                Pedidos = Pizzeriadominos.query.filter(db.func.date(Pizzeriadominos.fechaPedido) == date.today()).all()
                totalD = sum(pedido.total for pedido in Pedidos)
                Pedidos = Pizzeriadominos.query.filter(db.func.date(Pizzeriadominos.fechaPedido) == date.today()).all()

        if request.form['buttonP'] == "btnBuscar":
            '''
            dbq = pz_form.diaB.data
            mbq = pz_form.diaS.data
            
            Registros = Pizzeriadominos.query.filter(Pizzeriadominos.dia == dbq, Pizzeriadominos.mes == mbq).all()
            '''
            diaBuscar=pz_form.diaS.data
            mesBuscar=pz_form.mesS.data

            #day = filtradoDia[diaBuscar]
            #month = filtradoMes[mesBuscar]
            if diaBuscar == 'na' and mesBuscar != 'na':
                fecha = mesBuscar
                Registros = Pizzeriadominos.query.filter(Pizzeriadominos.mes == mesBuscar).all()
            if mesBuscar == 'na'and day != 'na':
                fecha = diaBuscar
                Registros = Pizzeriadominos.query.filter(Pizzeriadominos.dia == diaBuscar).all()
            if diaBuscar != 'na' and mesBuscar != 'na':
                fecha = '{} de {}'.format(diaBuscar, mesBuscar)
                Registros = Pizzeriadominos.query.filter(Pizzeriadominos.dia == diaBuscar, Pizzeriadominos.mes == mesBuscar).all()
            if diaBuscar == 'na' and mesBuscar == 'na':
                fecha = ''
                Registros = Pizzeriadominos.query.filter(Pizzeriadominos.dia == diaBuscar, Pizzeriadominos.mes == mesBuscar).all()
            
    return render_template("dominos.html", form=pz_form, Pizzas=Pizzas, Pedidos=Pedidos, totalD=totalD, Registros=Registros, fecha=fecha)

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