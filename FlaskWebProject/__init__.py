import logging
from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
wsgi_app = app.wsgi_app

# Add logging levels and handlers with app.logger
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

Session(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskExercise.views
