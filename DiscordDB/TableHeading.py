from DiscordDB.Errors import MissingKeyError, UnacceptableTypeError

ALLOWED_TYPES = [str, int, float, bool, list[str], list[int], list[float], list[bool]]


class TableHeading:
    def __init__(self, table_heading_dict: dict[str, type], primary_key: str = None):
        """The ``table_heading_dict`` parameter should take keys as the column names, and the values as the type of data
        the columns will hold. Any lists must be consistent with the data types within them, and the data types must be
        valid.

        example of what table_heading_dict can be:
        {"username": str, "score": int, "is_premium_user": bool}"""

        if primary_key not in table_heading_dict.keys():
            raise MissingKeyError()

        for data_type in table_heading_dict.values():
            if data_type not in ALLOWED_TYPES:
                raise UnacceptableTypeError(data_type)

        self.__table_heading_dict = table_heading_dict
        self.__primary_key = primary_key

    def __str__(self):
        string = str(self.__table_heading_dict).replace(' <class', '').replace('>', '').replace("'", '"')
        if self.__primary_key is None:
            return '{"column_headings": ' + string + f', "primary_key": null' + '}'
        else:
            return '{"column_headings": ' + string + f', "primary_key": "{self.__primary_key}"' + '}'

    def get_primary_key(self):
        return self.__primary_key

    def compare(self, row_items: list):  # compares the row items to the heading in the table to check the consistency
        for i, key in enumerate(self.__table_heading_dict):
            type_str = str(self.__table_heading_dict[key])
            if 'list' in type_str and isinstance(row_items, list):
                if len(set(row_items[i])) != 1 or type_str[5:-1] not in str(row_items[i][0]):
                    return False
            elif type(row_items[i]) != self.__table_heading_dict[key]:
                return False
        return True

    def get_index(self, column_name):
        return list(self.__table_heading_dict.keys()).index(column_name)
