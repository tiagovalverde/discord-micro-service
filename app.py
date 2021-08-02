from flask import Flask, Blueprint
from flask_apispec import FlaskApiSpec

from dotenv import load_dotenv
from helpers.app_helper import logger

from api.blueprints.messages import MessageResource

# load environment variables
load_dotenv()

# init flask
app = Flask(__name__)

# register api endpoints
blueprint = Blueprint("messages", __name__, url_prefix="/api")
app.add_url_rule(
    "/api/messages", view_func=MessageResource.as_view("messages"), methods=["POST"]
)
app.register_blueprint(blueprint)

# add endpoints to swagger
docs = FlaskApiSpec(app)
docs.register(MessageResource, endpoint="messages")

if __name__ == "__main__":
    app.run()
