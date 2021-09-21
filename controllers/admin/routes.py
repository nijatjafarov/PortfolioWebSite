from flask.globals import request
from app import app
from model import Source, UserMessage, db, AdditionalInfo, Technology, Task, Review, Blog, Project, \
    Photo, MyWorkOnProject
from flask import render_template, redirect, url_for
from form import AdditionalInfoForm, TechnologyForm, SourceForm, TaskForm, ReviewForm, BlogForm, ProjectForm, \
    PhotoForm, MyWorkOnProjectForm
import os
from werkzeug.utils import secure_filename


def checkLogin(parameter):
    loginStat = request.cookies.get("loginStatus")
    if loginStat == "True":
        return parameter
    else:
        return redirect(url_for("login"))


@app.route("/admin")
def admin():
    info = AdditionalInfo.query.all()
    techs = Technology.query.all()
    tasks = Task.query.all()
    reviews = Review.query.all()
    blogs = Blog.query.all()
    projects = Project.query.all()
    works = MyWorkOnProject.query.all()
    messages = UserMessage.query.all()
    photos = Photo.query.all()
    sources = Source.query.all()
    template = render_template("admin/admin.html", info = info, techs = techs, tasks = tasks, 
    technologies = Technology(), reviews = reviews, blogs = blogs, projects = projects,
    works = works, projs = Project(), messages = messages, photos = photos, sources = sources)
    return checkLogin(template)

# Additional Info
@app.route("/admin/addinfo", methods = ["GET", "POST"])
def addinfo():
    form = AdditionalInfoForm()
    if form.validate_on_submit():
        db.session.add(AdditionalInfo(
            info = form.info.data
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template =  render_template("admin/additionalInfo/addInfo.html", form = form)
    return checkLogin(template)

@app.route("/admin/updateinfo/<int:id>", methods = ["GET", "POST"])
def updateinfo(id):
    form = AdditionalInfoForm()
    additionalInfo = AdditionalInfo.query.get(id)
    if form.validate_on_submit():
        additionalInfo.info = form.info.data
        db.session.commit()
        return redirect(url_for("admin"))
    template =  render_template("admin/additionalInfo/updateInfo.html", form = form, info = additionalInfo)
    return checkLogin(template)

@app.route("/admin/deleteinfo/<int:id>", methods = ["GET", "POST"])
def deleteinfo(id):
    db.session.delete(AdditionalInfo.query.get(id))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)


# Technology   
@app.route("/admin/addtech", methods = ["GET", "POST"])
def addtech():
    form = TechnologyForm()
    if form.validate_on_submit():
        db.session.add(Technology(
            name = form.name.data,
            usageCase = form.usageCase.data,
            startDate = form.startDate.data,
            finishDate = form.finishDate.data,
            superTech = form.superTech.data
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/technology/addTech.html", form = form)
    return checkLogin(template)

@app.route("/admin/updatetech/<int:id>", methods = ["GET", "POST"])
def updatetech(id):
    form = TechnologyForm()
    tech = Technology.query.get(id)
    if form.validate_on_submit():
        tech.name = form.name.data
        tech.usageCase = form.usageCase.data
        tech.startDate = form.startDate.data
        tech.finishDate = form.finishDate.data
        tech.superTech = form.superTech.data
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/technology/updateTech.html", form = form, tech = tech)
    return checkLogin(template)

@app.route("/admin/deletetech/<int:id>", methods = ["GET", "POST"])
def deletetech(id):
    db.session.delete(Technology.query.get(id))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)
    
    
 # Source
@app.route("/admin/addsource", methods = ["GET", "POST"])
def addsource():
    form = SourceForm()
    if form.validate_on_submit():
        db.session.add(Source(name = form.name.data))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/source/addSource.html", form = form)
    return checkLogin(template)

@app.route("/admin/updatesource/<int:id>", methods = ["GET", "POST"])
def updatesource(id):
    form = TechnologyForm()
    source = Source.query.get(id)
    if form.validate_on_submit():
        source.name = form.name.data
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/source/updateSource.html", form = form, source = source)
    return checkLogin(template)

@app.route("/admin/deletesource/<int:id>", methods = ["GET", "POST"])
def deletesource(id):
    db.session.delete(Source.query.get(id))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)


# Task of technology   
@app.route("/admin/addtask", methods = ["GET", "POST"])
def addtask():
    form = TaskForm()
    technologies = Technology.query.all()
    if form.validate_on_submit():
        db.session.add(Task(
            name = form.name.data,
            url = form.url.data,
            technology_id = request.form["technology_id"],
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/task/addTask.html", form = form, technologies = technologies)
    return checkLogin(template)

@app.route("/admin/updatetask/<int:id>", methods = ["GET", "POST"])
def updatetask(id):
    form = TaskForm()
    task = Task.query.get(id)
    technologies = Technology.query.all()
    selected_technology = Technology.query.get(task.technology_id)
    if form.validate_on_submit():
        task.name = form.name.data
        task.url = form.url.data
        task.technology_id = request.form["technology_id"]
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/task/updateTask.html", form = form, task = task, 
    technologies = technologies, selected_technology = selected_technology)
    return checkLogin(template)

@app.route("/admin/deletetask/<int:id>", methods = ["GET", "POST"])
def deletetask(id):
    db.session.delete(Task.query.get(id))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)
    
# Review   
@app.route("/admin/addreview", methods = ["GET", "POST"])
def addreview():
    form = ReviewForm()
    if form.validate_on_submit():
        db.session.add(Review(
            review = form.review.data,
            review_owner = form.review_owner.data,
            owner_profession = form.owner_profession.data,
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/review/addReview.html", form = form)
    return checkLogin(template)

@app.route("/admin/updatereview/<int:id>", methods = ["GET", "POST"])
def updatereview(id):
    form = ReviewForm()
    review = Review.query.get(id)
    if form.validate_on_submit():
        review.review = form.review.data
        review.review_owner = form.review_owner.data
        review.owner_profession = form.owner_profession.data
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/review/updateReview.html", form = form, review = review)
    return checkLogin(template)

@app.route("/admin/deletereview/<int:id>", methods = ["GET", "POST"])
def deletereview(id):
    db.session.delete(Review.query.get(id))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)

# Blog   
@app.route("/admin/addblog", methods = ["GET", "POST"])
def addblog():
    form = BlogForm()
    if form.validate_on_submit():
        db.session.add(Blog(
            header = form.header.data,
            content = form.content.data,
            date = form.date.data,
            url = form.url.data,
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/blog/addBlog.html", form = form)
    return checkLogin(template)

@app.route("/admin/updateblog/<int:id>", methods = ["GET", "POST"])
def updateblog(id):
    form = BlogForm()
    blog = Blog.query.get(id)
    if form.validate_on_submit():
        blog.header = form.header.data
        blog.content = form.content.data
        blog.date = form.date.data
        blog.url = form.url.data
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/blog/updateBlog.html", form = form, blog = blog)
    return checkLogin(template)

@app.route("/admin/deleteblog/<int:id>", methods = ["GET", "POST"])
def deleteblog(id):
    db.session.delete(Blog.query.get(id))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)

# Project   
@app.route("/admin/addproject", methods = ["GET", "POST"])
def addproject():
    form = ProjectForm()
    if form.validate_on_submit():
        db.session.add(Project(
            name = form.name.data,
            about = form.about.data,
            code_url = form.code_url.data,
            real_url = form.real_url.data,
            startDate = form.startDate.data,
            finishDate = form.finishDate.data,
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/project/addProject.html", form = form)
    return checkLogin(template)

@app.route("/admin/updateproject/<int:id>", methods = ["GET", "POST"])
def updateproject(id):
    form = ProjectForm()
    project = Project.query.get(id)
    if form.validate_on_submit():
        project.name = form.name.data
        project.about = form.about.data
        project.code_url = form.code_url.data
        project.real_url = form.real_url.data
        project.startDate = form.startDate.data
        project.finishDate = form.finishDate.data
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/project/updateProject.html", form = form, project = project)
    return checkLogin(template)

@app.route("/admin/deleteproject/<int:id>", methods = ["GET", "POST"])
def deleteproject(id):
    db.session.delete(Project.query.get(id))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)

# Project photo  
@app.route("/admin/addphoto", methods = ["GET", "POST"])
def addphoto():
    form = PhotoForm()
    projects = Project.query.all()
    if form.validate_on_submit():
        images = request.files.getlist('name')

        for img in images:
            image = img
            image_name = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
            db.session.add(Photo(
                name = image_name,
                project_id = request.form["project_id"]
            ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/photo/addPhoto.html", form = form, projects = projects)
    return checkLogin(template)

@app.route("/admin/updatephoto/<int:id>", methods = ["GET", "POST"])
def updatephoto(id):
    form = PhotoForm()
    photo = Photo.query.get(id)
    projects = Project.query.all()
    if form.validate_on_submit():
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], photo.name)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], photo.name))
        image = form.name.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        photo.name = image_name
        photo.project_id = request.form["project_id"]
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/photo/updatePhoto.html", form = form, projects = projects)
    return checkLogin(template)

@app.route("/admin/deletephoto/<int:id>", methods = ["GET", "POST"])
def deletephoto(id):
    photo = Photo.query.get(id)
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], photo.name)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], photo.name))
    db.session.delete(photo)
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)

# My work on project  
@app.route("/admin/addwork", methods = ["GET", "POST"])
def addwork():
    form = MyWorkOnProjectForm()
    if form.validate_on_submit():
        db.session.add(MyWorkOnProject(
            name = form.name.data,
            project_id = request.form["project_id"]
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/work/addWork.html", form = form, projects = Project.query.all())
    return checkLogin(template)

@app.route("/admin/updatework/<int:id>", methods = ["GET", "POST"])
def updatework(id):
    form = MyWorkOnProjectForm()
    work = MyWorkOnProject.query.get(id)
    if form.validate_on_submit():
        work.name = form.name.data
        work.project_id = request.form["project_id"]
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/work/updateWork.html", form = form, work = work, 
    selected_project = Project.query.get(work.project_id), projects = Project.query.all())
    return checkLogin(template)

@app.route("/admin/deletework/<int:id>", methods = ["GET", "POST"])
def deletework(id):
    db.session.delete(MyWorkOnProject.query.get(id))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)


# Tech of Project 
@app.route("/admin/addtechtoproj", methods = ["GET", "POST"])
def addtechtoproj():
    projects = Project.query.all()
    technologies = Technology.query.all()
    if request.method == "POST":
        techs_id = request.form.getlist('technology_id')
        project = Project.query.get(request.form["project_id"])
        for id in techs_id:
            project.technologies.append(Technology.query.get(id))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/projsAndTechs/addTechToProj.html", projects = projects, technologies = technologies)
    return checkLogin(template)

@app.route("/admin/updatetechofproj/<int:proj_id>/<int:tech_id>", methods = ["GET", "POST"])
def updatetechofproj(proj_id, tech_id):
    projects = Project.query.all()
    technologies = Technology.query.all()
    selected_project = Project.query.get(proj_id)
    selected_technology = Technology.query.get(tech_id)
    if request.method == "POST":
        project = Project.query.get(request.form["project_id"])
        index = project.technologies.index(selected_technology)
        project.technologies.remove(selected_technology)
        project.technologies.insert(index, Technology.query.get(request.form["technology_id"]))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/projsAndTechs/updateProjOfTech.html", projects = projects, 
    technologies = technologies, selected_project = selected_project, selected_technology = selected_technology)
    return checkLogin(template)

@app.route("/admin/deletetechofproject/<int:proj_id>/<int:tech_id>", methods = ["GET", "POST"])
def deletetechofproject(proj_id, tech_id):
    selected_project = Project.query.get(proj_id)
    selected_technology = Technology.query.get(tech_id)
    selected_project.technologies.remove(selected_technology)
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)


# Source of Tech 
@app.route("/admin/addsourcetotech", methods = ["GET", "POST"])
def addsourcetotech():
    technologies = Technology.query.all()
    sources = Source.query.all()
    if request.method == "POST":
        sources_id = request.form.getlist('source_id')
        technology = Technology.query.get(request.form["technology_id"])
        for id in sources_id:
            technology.sources.append(Source.query.get(id))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/sourceAndTech/addSourceToTech.html", technologies = technologies,  sources = sources)
    return checkLogin(template)

@app.route("/admin/updatesourceoftech/<int:tech_id>/<int:source_id>", methods = ["GET", "POST"])
def updatesourceoftech(tech_id, source_id):
    technologies = Technology.query.all()
    sources = Source.query.all()
    selected_technology = Technology.query.get(tech_id)
    selected_source = Source.query.get(source_id)
    if request.method == "POST":
        technology = Technology.query.get(request.form["technology_id"])
        index = technology.sources.index(selected_source)
        technology.sources.remove(selected_source)
        technology.sources.insert(index, Source.query.get(request.form["source_id"]))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/sourceAndTech/updateSourceOfTech.html",
    technologies = technologies, sources = sources, selected_technology = selected_technology, selected_source = selected_source)
    return checkLogin(template)

@app.route("/admin/deletesourceoftech/<int:tech_id>/<int:source_id>", methods = ["GET", "POST"])
def deletesourceoftech(tech_id, source_id):
    selected_technology = Technology.query.get(tech_id)
    selected_source = Source.query.get(source_id)
    selected_technology.sources.remove(selected_source)
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)
