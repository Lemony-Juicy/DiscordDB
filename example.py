import asyncio
import random
import time

import discord

from DiscordDB import Database, TableHeading
from config import TOKEN  # import discord bot's token from another file

GUILD_ID = 1126111734411837480
CATEGORY_ID = 1126113733274505267
db = Database(GUILD_ID, CATEGORY_ID, command_prefix='.', intents=discord.Intents.all())


@db.event
async def on_ready():
    await db.tether()

    new_table_heading = TableHeading({"username": str, "score": int, "is_premium_user": bool}, primary_key="username")
    await db.create_table("scores", new_table_heading)

    await db.insert("scores", ['bobster2004', 12, False])
    await db.insert("scores", ['convolutedorange', 1000, True])

    await asyncio.sleep(10)

    t = time.time()
    print(await db.select("scores", lambda x: x[0] == 'convolutedorange'))
    print(f"Selected in {time.time()-t}s")

db.run(TOKEN)



