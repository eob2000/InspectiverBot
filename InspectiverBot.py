#eobBot v0.2a
import discord
import asyncio
client = discord.Client()
member = ('')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='MSG me to MSG the mods!'))
@client.event
async def on_message(message):
        if message.content.startswith('/aboutme'):
            await client.send_message(message.channel,'Inspectiver Bot 0.2a')
            print('aboutme command called by',str(message.author))
        elif message.content.startswith('/status'):
            mention1 = str(message.author.mention)
            role = discord.utils.get(message.server.roles, name='status')
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, mention1+' You are now set up for status alerts')
            print('status alert registered by',str(message.author))
        elif message.author != client.user and message.channel.is_private == True:
            channel1 = client.get_channel('modmailchannel')
            await client.send_message(channel1, str(message.author.mention)+' wrote: '+message.content)
            print('modmessage sent by',str(message.author))
@client.event
async def on_member_join(member):
        name1 = str(member.name)
        mention1 = str(member.mention)
        server = str(member.server)
        print('User joined',str(member.name))
        await client.send_message(member, 'Welcome To server '+name1)
        await client.send_file(member, 'serverlogo.png')
        await client.send_message(member, '(Click or tap to enlarge)')
        channel2 = client.get_channel('lobbychannel')
        await client.send_message(channel2, 'Welcome '+mention1+' to '+server)
client.run('clientid')
