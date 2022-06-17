from flask_migrate import Migrate
from .setup import db,create_app
import os
from .main.routes import TodoTable


app = create_app()

# migrate the database to production
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context_processor():
	return dict(db=db,TodoTable=TodoTable)