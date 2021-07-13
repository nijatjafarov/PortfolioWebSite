from app import app
from flask import redirect, render_template, url_for, make_response, flash
from model import bcrypt
from form import LoginForm


admin_login = {
    "adminname" : "nijatjafarov",
    "password" : bcrypt.generate_password_hash("helloworldprogrammer")
}

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.adminname.data == admin_login["adminname"] and bcrypt.check_password_hash(admin_login["password"], form.password.data):
            resp = make_response(redirect(url_for("admin")))
            resp.set_cookie("loginStatus", "True")
            return resp
        else:
            flash('Uğursuz cəhd. Admin adını və şifrəni yenidən yoxlayın!', 'danger')
    return render_template("authentication/login.html", form = form)

@app.route("/logout", methods = ["GET", "POST"])
def logout():
    resp = make_response(redirect(url_for("admin")))
    resp.set_cookie("loginStatus", "False")
    return resp
