import os

from flask import Flask, Blueprint
from flask_apispec import FlaskApiSpec

from dotenv import load_dotenv
from helpers.app_helper import logger

from api.blueprints.messages import MessageResource

# initialize
app = Flask(__name__)

# api blueprints
blueprint = Blueprint("messages", __name__, url_prefix="/api/")
app.add_url_rule("/api/messages", view_func=MessageResource.as_view("Messages"))
app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run()
    logger("Application initalize")
