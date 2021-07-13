from flask import Flask
upload_folder = "static/uploads"
app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecretkey123"
app.config["UPLOAD_FOLDER"] = upload_folder

from controllers.admin.routes import *
from controllers.app.routes import *
from controllers.authentication.routes import *

if __name__ == "__main__":
    app.run(debug=True)
