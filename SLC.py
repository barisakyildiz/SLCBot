import discord

bot = discord.Client()
@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    
    print("SLCbot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
    if message.content == "!hello" or message.content == "!hi" or message.content == "!greetings":
        await message.channel.send("Welcome on board {0.author.mention}".format(message))
        
bot.run("")