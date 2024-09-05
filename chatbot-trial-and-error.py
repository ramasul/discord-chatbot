import discord
import random


class MyClient(discord.Client):
    async def on_ready(self):
        """Triggered when connecting to Discord."""
        print(f'Connected as {self.user}.')

    async def on_message(self, message: discord.Message):
        """Triggered when receiving a message."""
        # Ignore messages sent by the bot itself
        if message.author == self.user:
            return

        print(f'Received a message from {message.author}: {message.content}')

        if message.content == '!pull':
            choice = random.choice([
                "Jangan bang", "Bang udah Bang", "Gas dapet b5",
                "Keknya dapet bagus deh", "Anjay lesgooo"
            ])
            await message.channel.send(
                f"Your fortune for today is: **{choice}**!"
            )


with open('.discord_token') as f:
    token = f.read().strip()

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
