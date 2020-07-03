from flask import Flask

# app = Flask(__name__)
# "app" mean app directory
app = Flask("app")

from app import routes