from discord import Webhook, RequestsWebhookAdapter
from helpers.app_helper import config, logger


class DiscordWebHook(Webhook):
    @classmethod
    def from_url(cls, channel_name: str):
        """
        Get webhook url from a channel name provided before discord.Webhook intialization

        Args:
            class_name (string): channel_name corresponding to correct webhook url

        Returns:
            Webhook: discord Webhook class instance
        """
        channel_config = config.channels[channel_name]
        return super().from_url(
            url=channel_config["webhook"], adapter=RequestsWebhookAdapter()
        )
