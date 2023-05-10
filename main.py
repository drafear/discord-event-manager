import os

import discord
from dotenv import load_dotenv
from config import Config

load_dotenv()
TOKEN = os.getenv("DISCORD_EVENT_MANAGER_TOKEN")

assert TOKEN != "", "DISCORD_EVENT_MANAGER_TOKEN is required"

config = Config()


def make_client() -> discord.Client:
    intents = discord.Intents.default()
    intents.message_content = True

    return discord.Client(intents=intents)


client = make_client()


def quote(text: str) -> str:
    return f"`{text}`"


@client.event
async def on_message(msg: discord.Message) -> None:
    if msg.author == client.user:
        return

    await msg.channel.send(msg.content)
    print(msg.content)

    await msg.edit(content=quote(msg.content))


client.run(TOKEN)
