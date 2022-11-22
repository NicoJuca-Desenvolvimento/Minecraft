from definições import frases, estados, Canais_de_voz
import discord
from discord.ext import commands
from random import choice
from re import fullmatch
from os import getenv
from os.path import exists
from dotenv import load_dotenv
import pymongo
#
#
load_dotenv()
#
#
usuario = getenv('MONGODB_USERNAME', default='')
senha = getenv('MONGODB_PASSWORD', default='')
cluster = getenv('MONGODB_CLUSTER', default='')
uri = ''.join(['mongodb+srv://', usuario, ':', senha, '@', cluster, '/?retryWrites=true&w=majority'])
mongo_client = pymongo.MongoClient(uri)
database = mongo_client.chatbot
#
#partidas
partidas_db = database.partidas

#
intents = discord.Intents.default()
intents.message_content = True
prefix = '%'
bot = commands.Bot(intents=intents, command_prefix='')


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    #
    #
    #
    if msg.author.bot:
        return
    autor = msg.author.id
    #
    #
    if msg.content.strip()[0] == prefix:
        mensagem = msg.content.strip()[1:]
    else:
        return
    #
    #
    if fullmatch('[rR]einiciar?', mensagem):
        #
        # Pesquisar e apagar o registro no banco - e informar o usuário
        partidas_db.find_one_and_delete({'jogador': autor})
        await msg.channel.send(frases['reiniciado'])
        return
    #
    #
    if fullmatch('[sS]ing it for me.?', mensagem):
        #
        # Fechar todos os canais de voz
        [await canais_de_voz[i].disconnect() for i in canais_de_voz.keys()]
        await msg.channel.send(frases['saindo'])
        return
    #
    #
    if partidas_db.count_documents({'jogador': autor}) == 0:
        #
        #
        partidas_db.insert_one({'jogador': autor, 'estado': 0})
        #
        #
    partida = partidas_db.find_one({'jogador': autor})
    #
    #
    # 
    if msg.channel.type.name == 'private':
        #
        #
        if partida['estado'] == 0:
            await msg.channel.send(frases['canal_privado'])
            await msg.channel.send(frases['sem_canal_de_voz'])
    #
    #
    #
    #
    if msg.channel.type.name != 'private':
        if msg.author.voice:
            if msg.guild.me not in msg.author.voice.channel.members:
                canais_de_voz[autor] = await msg.author.voice.channel.connect()
        else:
            await msg.channel.send(frases['sem_canal_de_voz'])
            return
    #
    #
    estado_do_jogador = estados[partida['estado']]
    #
    #
    for key, value in estado_do_jogador['proximos_estados'].items():
        if fullmatch(key, mensagem):
            #
            # Atualiza o estado do jogador
            partida = partidas_db.find_one_and_update(
                {'jogador': autor},
                {'$set': {'estado': value}},
                return_document=pymongo.ReturnDocument.AFTER
            )
            #
            # Se houver um som referente ao estado,
            # toca no canal de voz do jogador
            if msg.channel.type.name != 'private':
                arquivo_de_som = str(value) + '.mp3'
                if exists(arquivo_de_som):
                    #
                    # Conectar no canal de áudio e emitir o som
                    som_opus = await discord.FFmpegOpusAudio.from_probe(arquivo_de_som)
                    canais_de_voz[autor].play(som_opus)
            #
            # Se houver uma imagem referente ao estado, enviar
            arquivo_de_imagem = str(value) + '.png'
            if exists(arquivo_de_imagem):
                await msg.channel.send(file=discord.File(arquivo_de_imagem))
            #
            # Criar uma lista de frases usando o delimitador '|' e enviar uma a uma
            [await msg.channel.send(i) for i in choice(estados[value]['frases']).split('|')]
            return
    #
    # Sempre responder ao usuário (dica ou não)
    if partida['estado'] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send(frases['erro'])

bot.run(getenv('DISCORD_TOKEN', default=''))