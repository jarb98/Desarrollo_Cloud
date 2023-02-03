from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()

class Categoria(enum.Enum):
   CONFERENCIA = 1
   SEMINARIO = 2
   CONGRESO = 3
   CURSO = 4

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    #categoria = db.Column(db.Enum(Categoria))
    categoria = db.Column(db.String(128))
    lugar = db.Column(db.String(128))
    direccion = db.Column(db.String(128))
    fecha_inicio = db.Column(db.String(128))
    fecha_fin = db.Column(db.String(128))
    presencialidad = db.Column(db.String(128))
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))
    eventos = db.relationship('Evento', cascade='all, delete, delete-orphan')

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}

class EventoSchema(SQLAlchemyAutoSchema):
    #categoria = EnumADiccionario(attribute=("categoria"))
    class Meta:
         model = Evento
         include_relationships = True
         load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Usuario
         include_relationships = True
         load_instance = True
 