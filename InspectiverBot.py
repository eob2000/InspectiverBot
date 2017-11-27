#eobBot v0.3a
import discord
import asyncio
import random
client = discord.Client()
member = ('')
server = ()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='MSG me to MSG the mods!'))

@client.event
async def on_message(message):
        global server
        completed = 0
        if message.author != client.user and message.content.startswith('/aboutme'):
            completed = 1
            await client.send_message(message.channel,'Inspectiver Bot 0.3a')
            print('aboutme command called by',str(message.author))
        elif message.author != client.user and message.content.startswith('/status'):
            completed = 1
            mention1 = str(message.author.mention)
            role = discord.utils.get(message.server.roles, name='status')
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, mention1+' You are now set up for status alerts')
            print('status alert registered by',str(message.author))
        elif message.author != client.user and message.content.startswith('/neverhaveiever') or message.content.startswith('!neverhaveiever') or message.content.startswith('/neverhaveIever') or message.content.startswith('!neverhaveIever'):
            completed = 1
            random_lines = random.choice(open("neverhaveiever.txt").readlines())
            await client.send_message(message.channel,'**__NeverHaveIEver__** '+random_lines)
            print('neverhaveiever called by',str(message.author))
        elif message.author != client.user and message.author != client.user and message.channel.is_private == True and message.content.startswith('/naughtyAgree'):
            completed = 1
            server1 = client.get_server('serverid')
            role = discord.utils.get(server1.roles, name='naughty')
            member2 = server1.get_member(message.author.id)
            await client.add_roles(member2, role)
            await client.send_message(message.author, 'You now have access to NSFW channels')
            print('User granted NSFW access:',str(message.author))
        elif message.author != client.user and message.content.startswith('/iwanttobenaughty'):
            completed = 1
            print('User requested NSFW access:',str(message.author))
            await client.send_message(message.author, 'To be granted access you must agree to these rules:')
            await client.send_message(message.author, '''
1. Any critisism towards other users in #naughty-stuff (Even if it is non-intentional) will result in a permanent ban.

2. If you disobey an admin (first warning) you will get a permanent ban

3. Any links to anything at all will once again, result in a permanent ban (Unless preapproved)
''')
            await client.send_message(message.author, 'Reply /naughtyAgree to accept')
            print('Rule DM Sent to:',str(message.author))
        elif message.author != client.user and message.content.startswith('/') and message.channel.is_private == True:
            completed = 1
            await client.send_message(message.author, 'Invalid command')
        elif message.author != client.user and message.channel.is_private == True and completed == 0:
            channel1 = client.get_channel('modmailChannel')
            await client.send_message(channel1, str(message.author.mention)+' wrote: '+message.content)
            print('modmessage sent by',str(message.author))
        
            
            
        
@client.event
async def on_member_join(member):
        name1 = str(member.name)
        mention1 = str(member.mention)
        server = str(member.server)
        print('User joined',str(member.name))
        await client.send_message(member, 'Welcome To server '+name1)
        await client.send_file(member, 'image.png')
        await client.send_message(member, '(Click or tap to enlarge)')
        channel2 = client.get_channel('lobbychannel')
        await client.send_message(channel2, 'Welcome '+mention1+' to '+server)
client.run('clientID')
