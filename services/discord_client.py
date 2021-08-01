import discord


class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

    # async def on_message(self, message):
    #    if message.author == self.user:
    #        return
    #    await message.channel.send('Bot reply')
