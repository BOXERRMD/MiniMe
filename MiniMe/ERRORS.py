class MiniMeErrors(Exception):
    """
    Basic Exception for the module MiniMe
    """
    pass

class PathError(MiniMeErrors):
    def __init__(self, path: str):
        super().__init__(f"The path {path} doesn't exist !")