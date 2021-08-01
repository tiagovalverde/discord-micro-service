import os

from flask import Flask, Blueprint
from flask_apispec import FlaskApiSpec

from dotenv import load_dotenv
from services.discord_client import DiscordClient

from api.blueprints.messages import MessageResource

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# initialize
app = Flask(__name__)
discord_client = DiscordClient() 

# api blueprints
blueprint = Blueprint("messages", __name__, url_prefix="/api/")
app.add_url_rule('/messages', view_func=MessageResource.as_view('Messages'))
app.register_blueprint(blueprint)

if __name__ == "__main__":
    discord_client.run(TOKEN)
    app.run()
