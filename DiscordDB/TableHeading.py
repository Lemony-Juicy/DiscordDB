from DiscordDB.Errors import InconsistentKeyError


class TableHeading:
    def __init__(self, table_heading_dict: dict[str, type], primary_key: str = None):
        """The ``table_heading_dict`` parameter should take keys as the column names, and the values as the type of data
        the columns will hold.

        *example of what table_heading_dict can be*

        ``{"username": str, "score": int, "is_premium_user": bool}``"""

        if primary_key not in table_heading_dict.keys():
            raise InconsistentKeyError()

        self.__table_heading_dict = table_heading_dict
        self.__primary_key = primary_key

    def __str__(self):
        string = str(self.__table_heading_dict).replace(' <class', '').replace('>', '').replace("'", '"')
        print(string)
        if self.__primary_key is None:
            return '{"column_headings": ' + string + f', "primary_key": null' + '}'
        else:
            return '{"column_headings": ' + string + f', "primary_key": "{self.__primary_key}"' + '}'

    def get_primary_key(self):
        return self.__primary_key

    def compare(self, row_items: list):
        for i, key in enumerate(self.__table_heading_dict):
            if type(row_items[i]) != self.__table_heading_dict[key]:
                return False
        return True

    def get_index(self, column_name):
        return list(self.__table_heading_dict.keys()).index(column_name)


if __name__ == '__main__':
    a = TableHeading({"user": str, "score": int}, "user")
    print(str(a))
