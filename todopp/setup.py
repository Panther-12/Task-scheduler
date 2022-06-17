from flask import Flask 
from .config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail



bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

def create_app():

	app = Flask(__name__)
	app.config.from_object(Config)

	bootstrap.init_app(app)
	db.init_app(app)

	mail.init_app(app)

	from .main import main
	app.register_blueprint(main)

	return app