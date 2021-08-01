from discord import InvalidArgument
from discord.errors import HTTPException
import requests

from helpers.app_helper import logger

from flask_apispec import use_kwargs, marshal_with
from flask_apispec.views import MethodResource
from api.schemas.messages_schemas import MessageRequestSchema, MessageResponseSchema

from services.discord_webhook import DiscordWebHook


@marshal_with(MessageRequestSchema)
class MessageResource(MethodResource):
    @use_kwargs(MessageRequestSchema)
    @marshal_with(MessageResponseSchema)
    def post(self, **kwargs):
        try:
            webhook = DiscordWebHook.from_url(kwargs["channel_name"])
            webhook.send(kwargs["message"])
            return {"message": "Message sent!"}, 200
        except KeyError:
            logger.warning(f"Channel {kwargs['channel_name']} not found!")
            return {"message": f"Channel {kwargs['channel_name']} not found!"}, 400
        except (InvalidArgument, HTTPException):
            logger.error("Invalid webhook URL given!")
            return {"message": "Server Error"}, 500
