from DiscordDB.RowData import RowData
from discord.ext import commands
from .Funcs import *
from .TableHeading import TableHeading
from .Errors import TableCreationError, InsertionError, MissingTableError

HEADING_KEY = '|'


class Database(commands.Bot):
    def __init__(self, guild_id: int, category_id: int, **kwargs):
        super().__init__(**kwargs)
        self.guild: discord.Guild | None = None
        self.category: discord.CategoryChannel | None = None

        self.guild_id = guild_id
        self.category_id = category_id

    async def tether(self):
        """This should be used in the main async function before any queries are made, just after an instance of this
        is made"""
        self.guild = self.get_guild(self.guild_id)
        self.category = self.get_channel(self.category_id)

    async def __GetTableChannel(self, table_name: str):
        try:
            return list(filter(lambda x: x.name == table_name.lower() and isinstance(x, discord.TextChannel),
                               self.category.channels))[0]
        except IndexError:
            raise MissingTableError(table_name)

    async def create_table(self, table_name: str, table_heading: TableHeading) -> None:
        """Creating a table will essentially create another channel with the
        table name provided.
        Note - Table names will be converted to lowercase because of how discord manages channel names"""
        if table_name.lower() in tuple(map(lambda x: x.name, self.category.channels)):
            raise TableCreationError(table_name)

        channel = await self.guild.create_text_channel(table_name, category=self.category)
        await channel.send(str(table_heading) + HEADING_KEY)

    async def insert(self, table_name, items: list) -> None:
        """Insert a row (items) into a table"""
        channel = await self.__GetTableChannel(table_name)
        th = await GetTableHeading(channel)
        if not th.compare(items):
            raise InsertionError(f"Cannot insert these values {items} as they do not match with the row types")
        pk = th.get_primary_key()
        index = th.get_index(pk)
        if pk is not None and await self.select(table_name, lambda x: x[pk] == items[index]) != []:
            raise InsertionError(f"Cannot insert these values as the primary key '{pk}' already has this value of "
                                 f"{items[index]}")


        await channel.send(json.dumps(items))

    async def select(self, table_name, where) -> list[RowData]:
        """Retrieve items from a table. The second argument (where) should be a function which takes a RowData
        object"""
        channel = await self.__GetTableChannel(table_name)
        th = await GetTableHeading(channel)
        out = []
        async for m in channel.history(limit=None):
            if m.content[-1] == HEADING_KEY:
                continue

            row = json.loads(m.content)
            if where(RowData(row, th)):
                out.append(RowData(row, th))
        return out

    async def update(self, table_name, key_values: dict, where):
        channel = await self.__GetTableChannel(table_name)
        th = await GetTableHeading(channel)
        async for m in channel.history(limit=None):
            if m.content[-1] == HEADING_KEY:
                continue

            row = json.loads(m.content)
            rowdata = RowData(row, th)
            if where(rowdata):
                for key in key_values:
                    rowdata[key] = key_values[key]

                await m.edit(content=json.dumps(rowdata.get_row_list()))

    async def delete_table(self, table_name):
        channel = await self.__GetTableChannel(table_name)
        await channel.delete(reason="Table delete DiscordDB")

    async def delete_rows(self, table_name, where):
        channel = await self.__GetTableChannel(table_name)
        th = await GetTableHeading(channel)
        await channel.purge(check=lambda x: x.content[-1] != HEADING_KEY and where(RowData(json.loads(x.content), th)))
