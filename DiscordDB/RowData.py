from DiscordDB.TableHeading import TableHeading


class RowData:
    """A class that stores data about a row in a table. you can look up keys in it

    `example`

    ``rowdata['username']``"""
    def __init__(self, row: list, th: TableHeading):
        self.__row = row
        self.__th = th

    def __getitem__(self, key):
        return self.__row[self.__th.get_index(key)]

    def __setitem__(self, key, value):
        self.__row[self.__th.get_index(key)] = value

    def get_row(self) -> list:
        return self.__row

