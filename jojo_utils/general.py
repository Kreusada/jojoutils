from redbot.core.commands import BadArgument


def positive_int(arg: str) -> int:
    """This is a type hint for Red to require a positive int

    It *can* be used as a function but I wouldn't recommend it :p
    """

    try:
        ret = int(arg)
    except ValueError:  # Raised if it's not an int
        raise BadArgument(f"'{arg}' is not an integer")
    if ret < 1:
        raise BadArgument(f"'{arg}' is not a positive integer")
    return ret
