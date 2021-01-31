# Work with Python 3.6
import discord

TOKEN = 'ODA0ODkwNTQ1NzU5NTg0Mjg3.YBS6vA.I4NMFK2t7FyGzMFQpTe_HnYX1RM'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Nome e Cognome') and\
            (('porto' in message.content.lower() and 'armi' in message.content.lower()) or
             ('certificato' in message.content.lower() and ('porto' in message.content.lower() or
                                                            'armi' in message.content.lower()))):
        await message.delete()
        embed = discord.Embed(title="AVVISO IMPORTANTE",
                              description="Ciao, ti scrivo per ricordarti che secondo le nuove norme in vigore non"
                                          " bisogna più prenotare le visite per il porto d'armi.",
                              color=discord.Color.green())
        embed.add_field(name="ORARI PORTI D'ARMI", value="Dalle 15:00 alle 17:30\nDalle 20:00 alle 21:00",
                        inline=False)
        embed.set_footer(text="Cordialmente lo Staff Medico di Impero.")
        await message.author.send(embed=embed)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)