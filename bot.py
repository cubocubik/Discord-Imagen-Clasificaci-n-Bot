import discord
from discord.ext import commands
from utils import get_class

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def check(ctx):
    
    if not ctx.message.attachments:
        await ctx.send("Olvidaste la imagen")
        return
    
    for attachment in ctx.message.attachments:
        filename = attachment.filename
        await attachment.save(filename)
        
        try:
            result = get_class(
                model_path="model.tflite",
                labels_path="labels.txt",
                image_path=filename
            )
        
        except Exception as e:
            
            await ctx.send(f"Error: {e}")
        
        await ctx.send(f"El modelo predice: {result}")





bot.run("TU_TOKEM_AQUÍ")
