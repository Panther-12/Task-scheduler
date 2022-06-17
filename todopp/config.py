import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'todo.sqlite')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.environ.get('FLASK_ENV') or '47857ruehwafududf989e4yhiuwehf8'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USE_SSL= False
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'nimrodwalwe@gmail.com'
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '12@17y017g3sa?'
	MAIL_SUBJECT_PREFIX = '[Taskify]'
	MAIL_SENDER = os.environ.get('MAIL_SENDER')