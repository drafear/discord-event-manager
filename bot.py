import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BG_BOT_TOKEN')

assert(TOKEN != "", "DISCORD_BG_BOT_TOKEN is required")


def make_client():
  intents = discord.Intents.default()
  intents.message_content = True

  return discord.Client(intents=intents)

client = make_client()

def quote(text):
  return f"`{text}`"

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  await msg.channel.send(msg.content)
  print(msg.content)

  await msg.edit(content=quote(msg.content))

client.run(TOKEN)
