from flask import Flask, render_template
from .routes import main



@main.errorhandler(404)
def page_not_found():
	return render_template('404.html'),404