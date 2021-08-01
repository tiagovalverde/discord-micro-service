from flask_marshmallow import Schema
from marshmallow import fields


class MessageRequestSchema(Schema):
    channel_name = fields.Str()
    message = fields.Str()


class MessageResponseSchema(Schema):
    message = fields.Str()
