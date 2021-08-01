import requests
from discord import Webhook, RequestsWebhookAdapter

from flask_apispec import use_kwargs, marshal_with
from flask_apispec.views import MethodResource
from api.schemas.messages_schemas import MessageRequestSchema, MessageResponseSchema


@marshal_with(MessageRequestSchema)
class MessageResource(MethodResource):

    @use_kwargs(MessageRequestSchema)
    @marshal_with(MessageResponseSchema)
    def post(self, **kwargs):
      # TODO: allow api requester to indicate channel to send message through 'channel_name' 
      # TODO: catch exceptions when 'from_url' throws an exception
      webhook = Webhook.from_url(
        url="https://discord.com/api/webhooks/871370704459792394/UDIw8stmLixE8TNQHhjujj-2ZajGmE0yOciBUt0KPHapnTIPrlhqwiuTarbdxiFQEvc-",
        adapter=RequestsWebhookAdapter()
      )

      result = webhook.send(kwargs["message"])

      print(kwargs)
      print(result)
      return {
        "message": "message sent!"
      }
