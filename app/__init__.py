from json import JSONEncoder
from flask import Flask, render_template
from config import Config
from .authentication.routes import auth
from .api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


app.register_blueprint(auth)
app.register_blueprint(api)


    

app.config['SECRET_KEY'] = 'any secret string'
app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

