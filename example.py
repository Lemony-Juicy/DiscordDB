import discord
from DiscordDB import Database, TableHeading
from config import TOKEN  # import discord bot's token from another file

GUILD_ID = 1126111734411837480
CATEGORY_ID = 1126113733274505267
db = Database(GUILD_ID, CATEGORY_ID, command_prefix='.', intents=discord.Intents.all())


@db.event
async def on_ready():
    await db.tether()  # Sets everything up when connection to server is made

    new_table_heading = TableHeading({"username": str, "score": int, "is_premium_user": bool}, primary_key="username")
    await db.create_table("scores", new_table_heading)

    await db.insert("scores", ['HexGamer', 12, True])
    await db.insert("scores", ['convolutedorange', 1000, True])
    await db.insert("scores", ['bob', 25, False])
    await db.insert("scores", ['ethyl', 33, False])

    # Updates anyone with username convolutedorange so their score is 15 and is_premium_user is now False.
    # Note this will only ever update one person since username is a primary key.
    await db.update("scores", {'score': 15, 'is_premium_user': False}, lambda x: x['username'] == 'convolutedorange')

    # Deleting any rows with a score of greater than 20.
    await db.delete_rows("scores", lambda x: x['score'] > 20)

    # The parameter in the lambda function takes a RowData object.
    selected_rowDatas = await db.select("scores", lambda x: x['username'] == 'convolutedorange')
    print(list(map(lambda x: x.get_row_list(), selected_rowDatas)))

db.run(TOKEN)
