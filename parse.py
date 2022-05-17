import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import itertools

Bot = commands.Bot(command_prefix= '!')
client = discord.Client()


URL = 'http://newworld.com/en-us'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    wwa = soup.find("div", { "id" : "module-47CC4CRWai75nArj88J3pO" }).find("a")

    for item in wwa:
        item_url = wwa.get("href")
        print("http://newworld.com{}".format(item_url))
        items = "http://newworld.com{}".format(item_url)
    #items = soup.find("a")

    #items = soup.find_all_next('div', class_='ags-rich-text-div')
    print(items[1])
    #print(wwa)
    return items
    # ^^^^^^^^^^^^^^^^^

def parse():
    r = get_html(URL)
    r.raise_for_status()
    return get_content(r.content)
    # ^^^^^^^^^^^^^^^^^




@Bot.command(pass_context = True)
async def code(ctx):
    items = parse()
    await ctx.send(items)
@Bot.command(pass_context = True)
async def news(ctx):
    items = parse()
    await ctx.send(items)
    # ^^^^^^^^^^^^^^^^^





Bot.run('BOT_AUTH')