from DiscordDB.TableHeading import TableHeading


class RowData:
    """A class that stores data about a row in a table. You can look up or set values by the keys like in a dictionary.

    example: rowdata['username']"""
    def __init__(self, row: list, th: TableHeading):
        self.__row = row
        self.__th = th

    def __getitem__(self, key):
        return self.__row[self.__th.get_index(key)]

    def __setitem__(self, key, value):
        self.__row[self.__th.get_index(key)] = value

    def get_row_list(self) -> list:
        """Returns the list version of the items stored in this object"""
        return self.__row

