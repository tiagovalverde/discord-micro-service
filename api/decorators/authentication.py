import os

from flask import request
from dotenv import load_dotenv


def authenticated(fn):
    """
    Decorator to check if an HTTP request is done with a valid api key
    """

    def valid_token(*args, **kwargs):
        if request.headers.get("Authorization") == f"Bearer {os.getenv('API_KEY')}":
            return fn(*args, **kwargs)
        else:
            return {"message": "Permission denied"}, 401

    return valid_token
