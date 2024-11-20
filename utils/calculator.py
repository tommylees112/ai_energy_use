import fractions

import pint


def twh_to_gw(twh: float) -> float:
    ureg = pint.UnitRegistry()
    twh = twh * ureg.terawatt_hour
    tw = twh / ureg.Quantity("8760 hours")
    return tw.to("gigawatt")


def gw_to_twh(gw: float) -> float:
    ureg = pint.UnitRegistry()
    gw = gw * ureg.gigawatt
    twh = gw * ureg.Quantity("8760 hours")
    return twh.to("terawatt_hour")


def EJ_to_TWh(EJ: float) -> float:
    ureg = pint.UnitRegistry()
    EJ = EJ * ureg.Quantity("EJ")
    twh = EJ.to("TWh")
    return twh


def float_to_fraction(f: float) -> fractions.Fraction:
    """Convert a float to a Fraction object."""
    return fractions.Fraction(f).limit_denominator()


def to_e_notation(value: float) -> str:
    """Convert a float to scientific notation with 2 decimal places.

    Args:
        value: The float value to convert

    Returns:
        String representation in scientific notation with 2 decimal places

    Example:
        >>> to_e_notation(1234.5678)
        '1.23e+03'
    """
    return f"{value:.2e}"


if __name__ == "__main__":
    ureg = pint.UnitRegistry()
    # terawatt_hour  terawatt_hour
    # print(1 * ureg.terawatt_hour)
    to_e_notation((1 * ureg.terawatt_hour).to("megawatt_hour"))
    ...
