from flask import Flask
from config import Config

# app = Flask(__name__)
# "app" mean app directory
app = Flask("app")
app.config.from_object(Config)

from app import routes