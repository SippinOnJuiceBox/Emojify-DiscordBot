#Imports
import discord
from emojipasta.generator import EmojipastaGenerator
generator = EmojipastaGenerator.of_default_mappings()

whitelistedIDs = [187320442543931392,234054938928349184,287250659328393216,372192776743288833]
#Token reader
tokenReader = open("token.txt","r")
token = tokenReader.read()
client = discord.Client()

#Client events
@client.event
async def on_message(message):
    content = message.content
    if message.author.bot:
         return
    if len(content) >= 128 and message.author.id in whitelistedIDs:
        print(generator.generate_emojipasta(content))
        await message.channel.send(generator.generate_emojipasta(content))

client.run(token)

