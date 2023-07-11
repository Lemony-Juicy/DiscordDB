import asyncio
import json
import time
import discord
from colorama import Fore
from discord.ext import commands


async def GetRowInfo(channel):
    async for m in channel.history(limit=1, oldest_first=True):
        return json.loads(m.content)


class Database:
    def __init__(self, guild_id: int, category_id: int, bot: commands.Bot):
        self.guild: discord.Guild = bot.get_guild(guild_id)
        self.category: discord.CategoryChannel = bot.get_channel(category_id)
        self.bot = bot

    async def __GetTableChannel(self, table):
        return list(filter(lambda x: x.name == table and isinstance(x, discord.TextChannel), self.category.channels))[0]

    async def create_table(self, table_name: str, row_info: dict):
        start = time.time()
        if table_name in tuple(map(lambda x: x.name, self.category.channels)):
            print(Fore.RED + f"[Debug] Unsuccessful, this channel (table) name '{table_name}' already exists")
            return

        channel = await self.guild.create_text_channel(table_name, category=self.category)
        await channel.send(json.dumps(row_info) + '|')
        print(Fore.GREEN + f"[Debug] Successfully created table channel in {round(time.time() - start, 3)} seconds")

    async def insert(self, table, items: list):
        channel = await self.__GetTableChannel(table)
        row_info = await GetRowInfo(channel)

        for i, key in enumerate(row_info):
            if not isinstance(items[i], eval(row_info[key])):
                print(Fore.RED + f"[DEBUG]: Cannot insert these values as they do not match with the row types")
                return

        content = json.dumps(items) + '\n'  # The content we are going to push into the channel
        if len(content) > 2000:
            print(Fore.RED + f"[DEBUG]: Cannot insert these values as they exceed 2000 character limit on discord")

        await channel.send(content)

    async def select(self, table, where):
        channel = await self.__GetTableChannel(table)
        out = []
        async for m in channel.history(limit=None):
            if m.content[-1] == '|':
                continue
            row = json.loads(m.content)
            if where(row):
                out.append(row)
        return out

