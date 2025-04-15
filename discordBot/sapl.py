#importing packages
import discord
import random
from discord.ext import commands
import os


#command prefix - .
client = commands.Bot(command_prefix = '.')

#on_ready function
@client.event
async def on_ready():
  print('Bot is ready')

#latency function
@client.command()
async def latency(ctx):
  await ctx.send(f'{round(client.latency * 1000)}ms')

#8ball function
@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
  responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#bookLookup function
@client.command(aliases=['sapl', 'lookup'])
async def book(ctx, rawPath):
  rawPath = rawPath.replace('_','%20')
  await ctx.send(f'https://mysapl.bibliocommons.com/v2/search?query={rawPath}&searchType=smart')

#home function
@client.command(aliases=['homePage'])
async def home(ctx):
  await ctx.send("https://www.mysapl.org/")

#eventsNews function
@client.command(aliases=['events','news'])
async def eventsNews(ctx):
  await ctx.send("https://www.mysapl.org/Events-News")

#eventCalendar function
@client.command()
async def eventCalendar(ctx):
  await ctx.send("https://www.mysapl.org/Events-News/Events-Calendar")

#about function
@client.command()
async def about(ctx):
  await ctx.send("https://www.mysapl.org/About")

#service function
@client.command()
async def service(ctx):
  await ctx.send("https://www.mysapl.org/Services")

#library near me function
@client.command(aliases=['location','nearMe'])
async def findLibrary(ctx):
  await ctx.send("https://www.mysapl.org/Visit/Locations#0-library-locations---find-a-library")

#holidays function
@client.command(aliases=['holidays','closures'])
async def holiday(ctx):
  await ctx.send("https://www.mysapl.org/Visit/Locations#0-closuresholidays")

#login dashboard function
@client.command(aliases=['loginPage','dashboard'])
async def login(ctx):
  await ctx.send("https://mysapl.bibliocommons.com/user/login?destination=%2Fdashboard%2Fuser_dashboard")

#ask question function
@client.command(aliases=['question','askmysapl'])
async def askQuestion(ctx):
  await ctx.send("https://ask.mysapl.org/")

#full info function
@client.command(aliases=['information','commands'])
async def info(ctx):
  await ctx.send("```.latency - Same as .ping but does not return Pong!\n.8ball - Ask a question and you will receive an answer\n.book - Book lookup through the SAPL website utilizing a smart search algorithm developed by SAPL\n.home - Provides link for the SAPL homepage\n.eventsNews - Provides link for SAPL website's upcoming events and news\n.eventCalender - Provides link for SAPL calendar showing upcoming events and news\n.about - Provides link for additional information on SAPL \n.service - Provides link for the SAPL services\n.findLibrary - Provides link for geographic lookup of nearby SAPL libraries \n.holiday - Provides link which provides days in which the SAPL library is in a state of enclosure\n.login - Provides link to the SAPL login dashboard\n.askQuestion - Provides link to the library's online reference site\n.info - The command which is a legend for all other commands; Provides information on all other commands\n.tictactoe - Allows you to play tictactoe with another person (2 player), and you evoke the command with the @ of yourself and the other person you want to play with\n.rps - Allows you to play rock, paper, scissors, with the bot (Singleplayer), and you evoke the command by .rps and pick rock, paper, or scissors```")

#tictactoe function
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the .tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

#rock paper scissors function
@client.command()
async def rps(ctx,message):
  answer = message.lower()
  choices = ["rock","paper","scissors"]
  computer_answer = random.choice(choices)
  if answer not in choices:
    await ctx.send("That is not a valid option; Pick rock, paper, or scissors.")
    return
  else:
    if computer_answer == answer:
      await ctx.send(f"Tie! We both picked {answer}")
    if computer_answer == "rock":
      if answer == "paper":
        await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "paper":
      if answer == "rock":
        await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "scissors":
      if answer == "rock":
        await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "rock":
      if answer == "scissors":
        await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "paper":
      if answer == "scissors":
        await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "scissors":
      if answer == "paper":
        await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")

client.run("#key")
