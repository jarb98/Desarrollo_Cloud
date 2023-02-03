from flaskr import create_app
from flask_restful import Api
from .modelos import db, EventoSchema,Evento,Usuario
from .vistas import VistaSignIn, VistaLogIn, VistaEvento, VistaEventos, VistaEventosUsuario
from flask_cors import CORS
import logging
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.StreamHandler()])

api = Api(app)
api.add_resource(VistaEventos, '/eventos/api')
api.add_resource(VistaEvento, '/evento/<int:id_evento>')
api.add_resource(VistaSignIn, '/signin/api')
api.add_resource(VistaLogIn, '/login/api')
#Este con api me suena que va a ser lo que se llama para los eventos. Como le mando el id_usuario?
#Necesitaria un servicio que me retorne el usuario
#El frontend puede ser /usuario/<int:id_usuario>/eventos y así distingo a los diferentes usuarios 
#Tengo que integrar el JWT con las cookies
api.add_resource(VistaEventosUsuario, '/usuario/api/<int:id_usuario>/eventos')


jwt = JWTManager(app)