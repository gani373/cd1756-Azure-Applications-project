import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)

# Read configuration from environment variables
# Note: You must set these in your Azure Web App's "Configuration" settings
app.config.update(
    CLIENT_ID=os.environ.get("CLIENT_ID"),
    CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
    AUTHORITY=os.environ.get("AUTHORITY"),
    REDIRECT_PATH=os.environ.get("REDIRECT_PATH", "/redirect"),
    SCOPE=os.environ.get("SCOPE", "User.ReadBasic.All").split(' '),
    SQLALCHEMY_DATABASE_URI=os.environ.get("DB_URI"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    BLOB_ACCOUNT=os.environ.get("BLOB_ACCOUNT"),
    BLOB_CONTAINER=os.environ.get("BLOB_CONTAINER"),
    SESSION_TYPE=os.environ.get("SESSION_TYPE", "filesystem"),
    SECRET_KEY=os.environ.get("SECRET_KEY")
)

# Add logging levels and handlers
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
