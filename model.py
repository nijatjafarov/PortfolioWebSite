from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

class AdditionalInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    info = db.Column(db.String(250), unique = True, nullable = False)

class Technology(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    startDate = db.Column(db.DateTime)
    finishDate = db.Column(db.DateTime)
    usageCase = db.Column(db.String(100))
    source = db.Column(db.String(70))
    tasks = db.relationship("Task", backref = "technology", lazy = True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    url = db.Column(db.String(150))
    technology_id = db.Column(db.Integer, db.ForeignKey('technology.id'), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    review = db.Column(db.String(250), nullable = False)
    review_owner = db.Column(db.String(30), nullable = False, unique = True)
    owner_profession = db.Column(db.String(50))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    header = db.Column(db.String(150), nullable = False)
    content = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime)
    url = db.Column(db.String(150))

class UserMessage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(30), nullable = False)
    userMail = db.Column(db.String(50), nullable = False)
    message = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime)

projectAndTech = db.Table("projectAndTech",
    db.Column("project_id", db.Integer, db.ForeignKey("project.id")),
    db.Column("tech_id", db.Integer, db.ForeignKey("technology.id"))
)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70), nullable = False)
    about = db.Column(db.Text, nullable = False)
    code_url = db.Column(db.String(150))
    real_url = db.Column(db.String(150))
    startDate = db.Column(db.DateTime)
    finishDate = db.Column(db.DateTime)
    photos = db.relationship("Photo", backref = "project", lazy = True)
    my_works = db.relationship("MyWorkOnProject", backref = "project", lazy = True)
    technologies = db.relationship("Technology", secondary=projectAndTech)

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70), nullable = False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

class MyWorkOnProject(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# s = Student()
# c = Class()
# c.students.append(s)
# db.session.add(c)
# db.session.commit()

