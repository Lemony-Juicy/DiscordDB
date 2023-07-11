class InconsistentKeyError(Exception):
    """A key has not been found in the column keys"""

    def __init__(self, msg="The primary key given is not in the column keys in the dictionary provided as the first "
                           "argument"):
        super().__init__(msg)
