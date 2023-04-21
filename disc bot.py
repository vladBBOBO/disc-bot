

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'we have lagged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("")
