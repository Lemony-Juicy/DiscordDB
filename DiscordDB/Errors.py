class MissingKeyError(Exception):
    """A key has not been found in the column keys"""

    def __init__(self):
        super().__init__("The primary key given is not in any of the keys for this table (in the dictionary provided as"
                         " the first argument)")


class TableCreationError(Exception):
    """The table cannot be created because the name already exists"""

    def __init__(self, table_name: str):
        super().__init__(f"Unable to create table '{table_name}' since this channel (table) name already exists")


class MissingTableError(Exception):
    """The table cannot be created because the name already exists"""

    def __init__(self, table_name: str):
        super().__init__(f"Unable to find table '{table_name}'. Ensure this table name exists before trying to query "
                         f"it")


class InsertionError(Exception):
    """Raised when a row cannot be added to a table - inconsistent data, or primary key already exists"""

    def __init__(self, error: str):
        super().__init__(error)


class UnacceptableTypeError(Exception):
    """Raised when data type that is not acceptable to be stored in the database is used"""

    def __init__(self, data_type):
        super().__init__(f"Object from {data_type} cannot be used in the database. This is an unacceptable data type")

