from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, DateField, TextAreaField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Optional, Email

class AdditionalInfoForm(FlaskForm):
    info = TextField("Məlumat", validators = [DataRequired(), Length(max=250)])

class TechnologyForm(FlaskForm):
    name = TextField("Ad", validators = [DataRequired(), Length(max=30)])
    usageCase = TextField("İstifadə vəziyyəti", validators = [Length(max=100)])
    startDate = DateField("Başlama tarixi", format='%d/%m/%Y')
    finishDate = DateField("Bitmə tarixi", format='%d/%m/%Y', validators=[Optional()])
    superTech = TextField("Üst texnologiya", validators = [Length(max=30)])

class TaskForm(FlaskForm):
    name = TextField("Ad", validators = [DataRequired(), Length(max=150)])
    url = TextField("URL", validators = [Length(max=150)])

class ReviewForm(FlaskForm):
    review = TextField("Rəy", validators = [DataRequired(), Length(max=250)])
    review_owner = TextField("Rəy sahibi", validators = [DataRequired(), Length(max=30)])
    owner_profession = TextField("Rəy sahibinin vəzifəsi", validators = [DataRequired(), Length(max=50)])

class BlogForm(FlaskForm):
    header = TextField("Başlıq", validators = [DataRequired(), Length(max=150)])
    content = TextField("Məzmun", validators = [DataRequired()])
    date = DateField("Tarix", format='%d/%m/%Y')
    url = TextField("URL", validators = [DataRequired()])

class ProjectForm(FlaskForm):
    name = TextField("Ad", validators = [DataRequired(), Length(max=70)])
    about = TextField("Haqqında", validators = [DataRequired()])
    code_url = TextField("Kod URL", validators = [Length(max=150)])
    real_url = TextField("Hazır layihənin URL", validators = [Length(max=150)])
    startDate = DateField("Başlama tarixi", format='%d/%m/%Y')
    finishDate = DateField("Bitmə tarixi", format='%d/%m/%Y', validators=[Optional()])

class PhotoForm(FlaskForm):
    name = FileField("Şəkil seç", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Ancaq şəkil!'), FileRequired()])

class MyWorkOnProjectForm(FlaskForm):
    name = TextField("Ad", validators = [DataRequired(), Length(max=150)])

class MessageForm(FlaskForm):
    userName = TextField("Ad və soyad", validators = [DataRequired(), Length(max=30)])
    userMail = EmailField("Elektron poçt", validators=[DataRequired(), Email()])
    message = TextAreaField("Mesaj", validators=[DataRequired()])

class LoginForm(FlaskForm):
    adminname = TextField("Admin adı", validators=[DataRequired(), Length(max=20)])
    password = PasswordField("Şifrə", validators=[DataRequired()])
    submit = SubmitField("Daxil ol")

class SourceForm(FlaskForm):
    name = TextField("Ad", validators = [DataRequired(), Length(max=30)])