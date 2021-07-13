from datetime import datetime
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
from app import app
from flask import render_template
from model import db, AdditionalInfo, Technology, Task, Review, Blog, \
    UserMessage, Project
from form import MessageForm
from flask_mail import Mail, Message
mail = Mail(app)

@app.route("/")
def index():
    infoList = AdditionalInfo.query.all()
    techs = Technology.query.all()
    tasks = Task.query.all()
    reviews = Review.query.all()
    return render_template("app/index.html", infoList = infoList, techs = techs, 
    tasks = tasks, reviews = reviews)

@app.route("/works")
def works():
    projects = Project.query.all()
    return render_template("app/works.html", projects = projects)

@app.route("/blogs")
def blogs():
    blogs = Blog.query.all()
    return render_template("app/blogs.html", blogs = blogs)

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    form = MessageForm()
    if form.validate_on_submit():
        db.session.add(UserMessage(
            userName = form.userName.data,
            userMail = form.userMail.data,
            message = form.message.data,
            date = datetime.now()
        ))
        db.session.commit()
        msg = Message(form.message.data,
                  sender=form.userMail.data,
                  recipients=["nicat.ceferov14@gmail.com"])
        mail.send(msg)
        return redirect(url_for("contact"))
    return render_template("app/contact.html", form = form)