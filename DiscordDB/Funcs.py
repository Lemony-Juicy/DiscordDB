import json
import discord
from DiscordDB.TableHeading import TableHeading


async def GetTableHeading(channel: discord.TextChannel) -> TableHeading:
    async for m in channel.history(limit=1, oldest_first=True):
        raw = json.loads(m.content[:-1])
        data = raw['column_headings']
        for key in data:
            data[key] = eval(data[key])
        return TableHeading(data, raw['primary_key'])
