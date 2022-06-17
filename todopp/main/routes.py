from .forms import TodoForm
from ..models import db, TodoTable
from flask import render_template, flash
from flask import redirect,url_for,session
from . import main
from flask import request
from ..setup import mail, Config
from flask_mail import Message



# Function takes the recipients , subject and template to work with
def send_mail(to,subject,template,**kwargs):
	msg = Message(Config.MAIL_SUBJECT_PREFIX+subject, sender=Config.MAIL_SENDER,recipients=[to])
	msg.body = render_template(template+'.txt',**kwargs)
	msg.html = render_template(template+'.html',**kwargs)
	mail.send(msg)


@main.route('/', methods=['GET','POST'])
def index():
	form = TodoForm()

	# Query the database for all records
	tasks = TodoTable.query.all()

	if request.method == 'POST' and form.validate_on_submit():
		task = form.text.data
		session['name'] = 'Nimrod'

		db.session.add(TodoTable(task=task))
		db.session.commit()

		flash('New task added to the board')

		send_mail('nimrodnyongesa7@gmail.com', 'TASK UPDATE', 'email/confirm', task=task)
		return redirect(url_for('.index'))
	return render_template('index.html',form=form,tasks=tasks,name=session.get('name'))


@main.route('/deleteAll')
def delete_all():
	tasks = TodoTable.query.all()
	for task in tasks:
		db.session.delete(task)
		db.session.commit()
	flash('All records deleted')
	return redirect(url_for('.index'))	

@main.route('/remove')
def remove_completed():
	return redirect(url_for('.index'))