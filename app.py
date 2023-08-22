import random
import os
from dotenv import load_dotenv
from discord.ext import commands
from botdata import query

commandPrefix = 'r!'
bot = commands.Bot(command_prefix=commandPrefix)

# Import the os module.
import os
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
dotenv_path = "./env/.env"
load_dotenv(dotenv_path)
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print ("Bot is online.")
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency * 1000)}ms')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CLEAR THE 100 MESSAGES.
@bot.command()
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit=amount)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DICE ROLLING 
@bot.command()
async def roll100(ctx,die=100):
    await ctx.send(f"You rolled a d{die} and got:{random.randint(1,die)}")  
    
@bot.command()
async def roll20(ctx,die=20):
    roll = random.randint(1,die)
    await ctx.send(f"You rolled a d{die} and got:{roll}")
    
@bot.command()
async def roll12(ctx,die=12):
    await ctx.send(f"You rolled a d{die} and got:{random.randint(1,die)}")    
    
@bot.command()
async def roll10(ctx,die=10):
    await ctx.send(f"You rolled a d{die} and got:{random.randint(1,die)}")    
    
@bot.command()
async def roll8(ctx,die=8):
    await ctx.send(f"You rolled a d{die} and got:{random.randint(1,die)}")
    
@bot.command()
async def roll6(ctx,die=6):
    await ctx.send(f"You rolled a d{die} and got:{random.randint(1,die)}")
    
@bot.command()
async def roll4(ctx,die=4):
    await ctx.send(f"You rolled a d{die} and got:{random.randint(1,die)}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ROLL D20 WITH ATTACK MODIFIER 

@bot.command()
async def attack(ctx,atkmod: int):
    roll = random.randint(1,20)
    await ctx.send(f"You rolled a {roll}: Your roll to hit is {roll+atkmod}")
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#STAT ROLLING

@bot.command()
async def rollstats(ctx):
    stats = getStats()
    await ctx.send(f"You rolled: {stats}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY MOVEMENTS
@bot.command()
async def movements(ctx):    
    movements = query.get_all_movements(connection)
    list = ''
    for row in movements:
        list += row[0] +'\n'
    await ctx.send('This is all the possible movements you could make: \n' + list + 'For more information on these movements use command '+commandPrefix+ 'movement *movement Name*' )

@bot.command()
async def movement(ctx,*,movement):
    movement = (movement.strip()).capitalize()
    
    movement = query.get_movement_by_name(connection,movement)
    for row in movement:
        movementName = row[0]
        movementDesc = row[1]
    print('Movement - ' +movementName +':' + '\n' + movementDesc)
    await ctx.send('Movement - ' +movementName +':' + '\n' + movementDesc)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY REACTION

@bot.command()
async def reactions(ctx):    
    reactions = query.get_all_reactions(connection)
    list = ''
    for row in reactions:
        list += row[0] +'\n'
    await ctx.send('This is all the possible reactions you could make: \n' + list + 'For more information on these reactions use command '+commandPrefix+ 'reaction *reaction Name*' )

@bot.command()
async def reaction(ctx,*,reaction):
    reaction = (reaction.strip()).capitalize()
    
    reaction = query.get_reaction_by_name(connection,reaction)
    for row in reaction:
        reactionName = row[0]
        reactionDesc = row[1]
    print('Reaction - ' +reactionName +':' + '\n' + reactionDesc)
    await ctx.send('Reaction - ' +reactionName +':' + '\n' + reactionDesc)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY BONUS ACTION
@bot.command()
async def bonusActs(ctx):    
    bonus_actions = query.get_all_bonus_actions(connection)
    list = ''
    for row in bonus_actions:
        list += row[0] +'\n'
    await ctx.send('This is all the possible bonus_actions: \n' + list + 'For more information on these bonus_actions use command '+commandPrefix+ 'bonus_action *bonus_actionName*' )
    
@bot.command()
async def bonusAct(ctx,*,bonus_action):
    bonus_action = (bonus_action.strip()).capitalize()
    
    bonus_action = query.get_bonus_action_by_name(connection,bonus_action)
    for row in bonus_action:
        bonus_actionName = row[0]
        bonus_actionDesc = row[1]
    print('Bonus Action - ' +bonus_actionName +':' + '\n' + bonus_actionDesc)
    await ctx.send('Bonus Action - ' +bonus_actionName +':' + '\n' + bonus_actionDesc)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY ACTIONS

@bot.command()
async def actions(ctx):    
    actions = query.get_all_actions(connection)
    list = ''
    for row in actions:
        list += row[0] +'\n'
    await ctx.send('This is all the possible actions you could make: \n' + list + 'For more information on these actions use command '+commandPrefix+ 'action *action Name*' )

@bot.command()
async def action(ctx,*,action):
    action = (action.strip()).capitalize()
    
    action = query.get_action_by_name(connection,action)
    for row in action:
        actionName = row[0]
        actionDesc = row[1]
    print('Action - ' +actionName +':' + '\n' + actionDesc)
    await ctx.send('Action - ' +actionName +':' + '\n' + actionDesc)
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY CONDITIONS
@bot.command()
async def conditions(ctx):    
    conditions = query.get_all_conditions(connection)
    list = ''
    for row in conditions:
        list += row[0] +'\n'
    await ctx.send('This is all the possible conditions: \n' + list + 'For more information on these conditions use command '+commandPrefix+ 'condition *conditionName*' )
    
@bot.command()
async def condition(ctx,*,condition):
    condition = (condition.strip()).capitalize()
    
    condition = query.get_condition_by_name(connection,condition)
    for row in condition:
        conditionName = row[0]
        conditionDesc = row[1]
    print('Condition - ' +conditionName +':' + '\n' + conditionDesc)
    await ctx.send('Condition - ' +conditionName +':' + '\n' + conditionDesc)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY MONSTERS - TO BE IMPLEMENTED

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY SPELLS - TO BE IMPLEMENTED

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY FEATS - TO BE IMPLEMENTED

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY CLASS - TO BE IMPLEMENTED

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY SUBCLASS - TO BE IMPLEMENTED

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# QUERY RACE - TO BE IMPLEMENTED

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS

def getStats():
    stats = [0,0,0,0,0,0]
    for index in range(0,len(stats)):
        stats[index] = getStat()
    return stats

def getStat():
    rolls = [0,0,0,0]
    for x in range(0,len(rolls)):
        rolls[x] = random.randint(1,6)
    rolls = sorted(rolls)
    rolls = rolls[1:]
    stat = 0
    for r in rolls:
        stat += r
    return stat

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
# START BOT            
connection = query.connect()   
bot.run(DISCORD_TOKEN)