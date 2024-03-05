from wtforms import Form
from wtforms import SearchField, TextAreaField, RadioField, StringField, SelectField, IntegerField
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
