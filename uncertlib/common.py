from typing import Union
from typing import Tuple


NUM_TYPE = Union[float, int]


def round_to_sf(number: float, sf: int = 1) -> float:
    """Rounds a number to a given number of significant figures

    Args:
        number (float): Number in question
        sf (int, optional): Significant figures. Defaults to 1.

    Returns:
        float: Rounded number
    """
    return float(f"%.{int(sf)}g" % number)


def get_scientific(number: float) -> Tuple[float, int]:
    """Uses built-in scientific notation to get the value and exponent

    Args:
        number (float): Number in question

    Returns:
        Tuple[float, int]: Value and exponent of the number in sci. notation
    """
    value, _, exp = f"{number:E}".rpartition("E")
    return float(value), int(exp)


def get_superscript(number: int) -> str:
    """Converts a number to a superscript string

    Args:
        number (int): Number in question

    Returns:
        str: Superscripted string of the number
    """
    str_num = str(abs(number))
    # Conversion to superscript
    superscript_num = list("⁰¹²³⁴⁵⁶⁷⁸⁹")
    for i in range(10):
        str_num = str_num.replace(str(i), superscript_num[i])
    if abs(number) == number:
        sign = "\u207a"
    else:
        sign = "\u207b"
    return f"{sign}{str_num}"
    
