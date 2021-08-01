import json


class Config:
    def __init__(self):
        with open("config/discord_channels.json") as file:
            self.channels = json.load(file)
