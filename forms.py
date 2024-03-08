from wtforms import Form
from wtforms import SearchField, TextAreaField, RadioField, StringField, SelectField, IntegerField, BooleanField, SelectMultipleField, widgets, DateField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre=StringField('nombre',[validators.DataRequired(message='El campo es requerido'),
                                 validators.length(min=4, max=10, message='Ingresa nombre valido')
    ])
    email=EmailField('email')
    apaterno=StringField('apaterno')
    edad=IntegerField('edad', [validators.number_range(min=1,max=20, message='valor no valido')])
    correo=EmailField('correo',[validators.Email(message='Ingrese un correo valido')])
    materias=SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingels', 'ING')])
    radios=RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])

class UserForm2 (Form):
    nombre = StringField("nombre", [
        validators.DataRequired(message='El campo es requerido'), 
        validators.length(min=4, max=10, message='Ingrese un nombre valido')
    ])
    email = EmailField('correo', [validators.Email(message='Ingrese un correo valido')])
    apaterno = StringField('apaterno')

class UserFormMaestros (Form):
    nombre = StringField("nombre", [
        validators.DataRequired(message='El campo es requerido'), 
        validators.length(min=4, max=10, message='Ingrese un nombre valido')
    ])
    email = EmailField('correo', [validators.Email(message='Ingrese un correo valido')])
    apaterno = StringField('apaterno')
    amaterno = StringField('amaterno')
    materia = StringField('materias')

class PizzaForm(Form):
    nombreP=StringField('Nombre',[validators.DataRequired(message='El campo es requerido'),
                                 validators.length(min=4, max=100, message='Ingresa nombre valido')
    ])
    direccionP=StringField('Direccion',[validators.DataRequired(message='El campo es requerido'),
                                 validators.length(min=4, max=100, message='Ingresa direccion valido')
    ])
    telefonoP=StringField('Telefono',[validators.DataRequired(message='El campo es requerido'),
                                 validators.length(min=4, max=20, message='Ingresa telefono valido')
    ])
    numPizzas=IntegerField('Num. de Pizzas', [validators.number_range(min=1,max=100, message='valor no valido')])
    
    tamP=RadioField('Tamaño Pizza',choices=[('Chica','Chica $40'),('Mediana','Mediana $80'),('Grande','Grande $120')])

    ingdP = SelectMultipleField('Ingredientes', choices=[('Jamon','Jamon $10'),('Pinia','Piña $10'),('Champiniones', 'Champiñones $10')], widget=widgets.ListWidget(prefix_label=False), option_widget=widgets.CheckboxInput())
    
    diaS=SelectField(choices=[('na','NA'),('Lunes','Lunes'),('Martes','Martes'),('Miercoles', 'Miercoles'),('Jueves', 'Jueves'),('Viernes', 'Viernes'),('Sabado', 'Sabado'),('Domingo', 'Domingo')])

    mesS=SelectField(choices=[('na','NA'),('Enero','Enero'),('Febrero','Febrero'),('Marzo', 'Marzo'),('Abril', 'Abril'),('Mayo', 'Mayo'),('Junio', 'Junio'),('Julio', 'Julio'),('Agosto', 'Agosto'),('Septiembre', 'Septiembre'),('Octubre', 'Octubre'),('Noviembre', 'Noviembre'),('Diciembre', 'Diciembre')])

    fechaRegistro = DateField('Fecha de Registro', format='%Y-%m-%d')

    diaB = StringField('')
    mesB = StringField('')