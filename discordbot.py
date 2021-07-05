from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.event
 async def on_message(self, message):
        if "" in message.content:
            with open("log.txt", "a") as w:
                w.write("[NAME]:" + message.author.name + " [MESSAGE]:" + message.content + "\n")
            print("[NAME]:" + message.author.name + " [MESSAGE]:" + message.content)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
