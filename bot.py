import discord 
from discord.ext import commands 
import keys 
import requests 
import json
import time
import random 

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    atividade = [ 
        'Esperando o Vasco cair',
        'Secando o mengão',
        'Acompanhando o Dinizmo',
        'Enxugando lágrimas de um botafoguense',
        'Contratando um novo técnico',
        '[O Fluminense entrou com um recurso e essa mensagem foi retirada.]'
    ]
    rand = random.randint(0, len(atividade)-1)
    print(rand)
    random_atividade = atividade[rand]
    await client.change_presence(activity=discord.Game(random_atividade))
    print('Bot is ready')

@client.command()
async def pedro(ctx):
    await ctx.send('Foda-se o Pedro')

@client.command(aliasses=['Campeonato'])
async def campeonato(ctx, *args):
    arg = ''.join(args).lower();
    if arg == 'copadobrasil':
    #Fazendo a requisição com a chave da api 
        url = 'https://api.api-futebol.com.br/v1/campeonatos/2'
    head = {'Authorization': 'Bearer ' + keys.get_api_key()}
    r = requests.get(url, headers=head)

    #Transformando a requisição em uma lista com um dicionário 
    #Primeiro eu passo para texto, e dps transformo em dicionário
    r = r.text
    datastore = json.loads(r)
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.set_author(name="Campeonato", icon_url='https://logodownload.org/wp-content/uploads/2018/10/copa-do-brasil-logo-1.png')
        embed.add_field(name='Nome do campeonato', value=datastore['nome_popular'])
        embed.add_field(name='Edição', value=datastore['edicao_atual']['temporada'])
        embed.add_field(name='Tipo', value=datastore['tipo'])
        embed.add_field(name='Fase', value=datastore['fase_atual']['nome'])
        embed.add_field(name='Status', value=datastore['status'])
        embed.set_footer(text=time.strftime("%X %d/%m/%Y"))
        await ctx.send(embed=embed)
    elif arg == 'brasileiro' or arg == 'brasileirão' or arg == 'brasileirao':
        url = 'https://api.api-futebol.com.br/v1/campeonatos/10'
        head = {'Authorization': 'Bearer ' + keys.get_api_key()}
        r = requests.get(url, headers=head)
        r = r.text
        datastore = json.loads(r)
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name="Campeonato", icon_url='https://logodownload.org/wp-content/uploads/2018/10/campeonato-brasileiro-logo-brasileirao-logo-5.png')
        embed.add_field(name='Nome do campeonato', value=datastore['nome_popular'])
        embed.add_field(name='Edição', value=datastore['edicao_atual']['temporada'])
        embed.add_field(name='Tipo', value=datastore['tipo'])
        embed.add_field(name='Rodada', value=datastore['rodada_atual']['nome'])
        embed.add_field(name='Status', value=datastore['status'])

    embed.set_footer(text=time.strftime("%X %d/%m/%Y"))
    await ctx.send(embed=embed)


client.run(keys.get_bot_key())

