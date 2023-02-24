import openai
import discord
from discord.ext import commands

openai.api_key = "YOUR_API_KEY"

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ask(ctx, *, question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=30,
        temperature=0.9,
        stop='.'
    )

    embed = discord.Embed(title="OpenAI API Result", description=response.choices[0].text)
    await ctx.send(embed=embed)

bot.run("YOUR_BOT_TOKEN")
