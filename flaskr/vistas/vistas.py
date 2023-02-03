from flask import request
from ..modelos import db, Usuario, UsuarioSchema, Evento, EventoSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token
evento_schema = EventoSchema()
usuario_schema = UsuarioSchema()

class VistaEventos(Resource):
    def post(self):
        nuevo_evento = Evento(titulo=request.json["titulo"],
        categoria=request.json["categoria"], 
        lugar=request.json["lugar"],
        direccion=request.json["direccion"],
        fecha_inicio = request.json["fecha_inicio"],
        fecha_fin = request.json["fecha_fin"],
        presencialidad = request.json["presencialidad"])
        db.session.add(nuevo_evento)
        db.session.commit()
        return evento_schema.dump(nuevo_evento)
    def get(self):
        return [evento_schema.dump(ca) for ca in Evento.query.all()]

class VistaEvento(Resource):

    def get(self, id_evento):
        return evento_schema.dump(Evento.query.get_or_404(id_evento))

    def put(self, id_evento):
        evento = Evento.query.get_or_404(id_evento)
        evento.titulo = request.json.get("titulo",evento.titulo)
        evento.categoria = request.json.get("minutos",evento.minutos)
        evento.lugar = request.json.get("segundos",evento.segundos)
        evento.direccion = request.json.get("interprete",evento.interprete)
        evento.fecha_inicio = request.json.get("fecha_inicio",evento.fecha_inicio)
        evento.fecha_fin = request.json.get("fecha_fin",evento.fecha_fin)
        evento.presencialidad = request.json.get("presencialidad",evento.presencialidad)
        db.session.commit()
        return evento_schema.dump(evento)

    def delete(self, id_evento):
        evento = Evento.query.get_or_404(id_evento)
        db.session.delete(evento)
        db.session.commit()
        return '',204

class VistaLogIn(Resource):
    def post(self):
            
            u_mail = request.json["mail"]
            u_contrasena = request.json["contrasena"]
            #Error si hay mas de un usuario con mismo mail y contraseña
            usuario = Usuario.query.filter_by(mail=u_mail, contrasena = u_contrasena).all()
            if usuario:
                token_de_acceso = create_access_token(identity=u_mail)
                id_usuario = usuario[0].id
                return {'mensaje':'Inicio de sesión exitoso','token_de_acceso':token_de_acceso,'id_usuario':id_usuario}, 200
            else:
                return {'mensaje':'Nombre de usuario o contraseña incorrectos'}, 401


class VistaSignIn(Resource):

    def post(self):
        nuevo_usuario = Usuario(mail=request.json["mail"], contrasena=request.json["contrasena"])
        token_de_acceso = create_access_token(identity = request.json['mail'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        id_usuario = nuevo_usuario.id
        print(id_usuario)
        print('id_usuario es:',id_usuario )
        return {'mensaje':'usuario creado exitosamente','token de acceso':token_de_acceso,'id_usuario':id_usuario}
    #Update password
    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.contrasena = request.json.get("contrasena",usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)

    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return '',204


#Revisar si este me sirve (En el frontend sería lo que mueve los botones de agregar cancion)
class VistaEventosUsuario(Resource):
    #Metodo de añadir un evento 
    #Tengo un problema con el jwt
    @jwt_required()
    def post(self, id_usuario):
        print(id_usuario)
        nuevo_evento = Evento(
        titulo=request.json["titulo"],
        categoria = request.json["categoria"],
        lugar = request.json["lugar"],
        direccion = request.json["direccion"],
        fecha_inicio = request.json["fecha_inicio"],
        fecha_fin = request.json["fecha_fin"],
        presencialidad = request.json["presencialidad"]
        )
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.eventos.append(nuevo_evento)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return 'El usuario ya tiene un evento con dicho nombre',409

        return evento_schema.dump(nuevo_evento)
    #Metodo de ver eventos  
    
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [evento_schema.dump(al) for al in usuario.eventos]
