import discord
from discord.ext import commands
import json
import os

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]
	ver_channel_id = data["verification_channel_id"]


class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print(discord.__version__)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))
	embed = discord.Embed(
		title = "Statue Of Liberty Cemetery",
		description = "Welcome to the realm of the dead and the living, Statue of Liberty Cemetery. To proceed and see all the channels add a reaction to verification emoji below!",
		color = discord.Color.purple()
	)
	Channel = bot.get_channel(ver_channel_id)
	Moji = await Channel.send(embed = embed)
	await Moji.add_reaction('✅')
	

@bot.event
async def on_reaction_add(reaction, user):
	channel = bot.get_channel(ver_channel_id)
	if reaction.message.channel.id != channel.id:
		return
	if reaction.emoji == "✅":
		Role = discord.utils.get(user.guild.roles, name = "Everyone")
		await user.add_roles(Role)

bot.run(token)