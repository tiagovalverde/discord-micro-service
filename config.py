import json


class Config:
    """
    Class containing any necessary configuration date for the application
    """

    def __init__(self):
        with open("config/discord_channels.json") as file:
            self.channels = json.load(file)
