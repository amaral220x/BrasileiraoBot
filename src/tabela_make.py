import discord 

def get_embed(argumento, datastore):
    if argumento == 'g4': 
        num1 = -1
        num2 = 5
        embed = discord.Embed(colour = discord.Colour.green())
        
    elif argumento == 'z4': 
        num1 = 16
        num2 = 20
        embed = discord.Embed(colour = discord.Colour.red())

    elif argumento == 'p2':
        num1 = 8
        num2 = 16
        embed = discord.Embed(colour = discord.Colour.blue())

    elif argumento == 'p3':
        num1 = 15
        num2 = 20 
        embed = discord.Embed(colour = discord.Colour.blue())
    elif argumento == " ":
        num1 = -1
        num2 = 9
        embed = discord.Embed(colour = discord.Colour.blue())

    else: 
        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_author(name="ERRO", icon_url='https://logodownload.org/wp-content/uploads/2018/10/campeonato-brasileiro-logo-brasileirao-logo-5.png')
        embed.add_field(name='ERRO', value= 'Você escolheu nenhuma zona da tabela disponível.')
        return embed
    embed.set_author(name="Brasileirao 2020", icon_url='https://logodownload.org/wp-content/uploads/2018/10/campeonato-brasileiro-logo-brasileirao-logo-5.png')
    for ds in datastore: 
        if ds['posicao'] > num1 and ds['posicao'] < num2 :
            embed.add_field(name='Posição', value= str(ds['posicao']) + 'º')
            embed.add_field(name='Nome do time', value= ds['time']['nome_popular'])
            embed.add_field(name='Nº de pontos', value= ds['pontos'])
            embed.set_footer(text = 'Para alguma zona em específico da tabela, tente usar G4 ou Z4. Para o resto da tabela, tente p2 ou p3', icon_url='https://logodownload.org/wp-content/uploads/2018/10/campeonato-brasileiro-logo-brasileirao-logo-5.png')
    return embed    
