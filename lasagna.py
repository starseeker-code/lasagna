"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(time:int) -> int:
    """Calculate the bake time remaining.

    :param time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time if EXPECTED_BAKE_TIME - time >= 0 else 0


def preparation_time_in_minutes(layers:int) -> int:
    """Calculate the preparation time of the lasagna.

    :param layers: int - layers of the lasagna.
    :return: int - total time needed for all the layers of the lasagna (derived from PREPARATION_TIME).
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers:int, time:int) -> int:
    """Calculate the elapsed time of the lasagna.

    :param layers: int - layers of the lasagna.
    :param time: int - time of baking in the oven.
    :return: int - total elapsed time (derived from PREPARATION_TIME).
    """
    return PREPARATION_TIME * layers + time
