import discord 
from discord.ext import commands 
import keys 
import requests 
import json
import time

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Esperando o BBBasco'))
    print('Bot is ready')

@client.command()
async def pedro(ctx):
    await ctx.send('Foda-se o Pedro')

@client.command(aliasses=['campeonato', 'Campeonato'])
async def campeonato(ctx):
    #Fazendo a requisição com a chave da api 
    url = 'https://api.api-futebol.com.br/v1/campeonatos'
    head = {'Authorization': 'Bearer ' + keys.get_api_key()}
    r = requests.get(url, headers=head)

    #Transformando a requisição em uma lista com um dicionário 
    #Primeiro eu passo para texto, e dps transformo em dicionário
    r = r.text
    datastore = json.loads(r)
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.set_author(name="Campeonato", icon_url='https://logodownload.org/wp-content/uploads/2018/10/copa-do-brasil-logo-1.png')
    embed.add_field(name='Nome do campeonato', value=datastore[0]['nome_popular'])
    embed.add_field(name='Edição', value=datastore[0]['edicao_atual']['temporada'])
    embed.add_field(name='Edição', value=datastore[0]['fase_atual']['nome'])
    embed.set_footer(text=time.strftime("%X %d/%m/%Y"))
    await ctx.send(embed=embed)


client.run(keys.get_bot_key())

