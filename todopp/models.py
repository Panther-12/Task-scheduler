from .setup import db
import datetime


# Create an sql, postgres, sqlite3 db
#  1. flask db init
#  2. flask db upgrade/downgrade

# To avoid loading the database every time flask shell is started use the command below;
#  	@app.shell_context_processor
#		def make_shell_context_processor():
#			return dict(db=db, models=models)


class TodoTable(db.Model):
	__tablename__ = 'todos'
	id = db.Column(db.Integer, unique=True, primary_key=True)
	task = db.Column(db.String(64))
	date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

	def __repr__(self):
		return "<task %r>" % self.task