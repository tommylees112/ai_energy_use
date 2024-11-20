import pint


def burnup_to_fuel_requirement(burnup: float, efficiency: float) -> float:
    # given in MWd/tU = MW * 24h / 1000kg Uranium
    # How many MWd per tU?
    ureg = pint.UnitRegistry()

    # A. Convert burnup [MWd/tU] to 1kgU/MWd (1tU = 1e3kgU)
    # how many kgU per MWd?
    kgU_MWd = 1e3 / burnup

    # B. Convert kgU/MWd to kgU/MWh
    # how many kgU per MWh?
    kgU_MWh = kgU_MWd * (1 / 24)

    # C. convert kgU/MWh to kgU/TWh
    # how many kgU per TWh? (MWh -> TWh)
    kgU_TWh = kgU_MWh * 1e6

    # D. Apply thermal efficiency of plants
    # if efficiency is 1/3 then we need 3x as much fuel
    kgU_TWh *= 1 / efficiency

    unit = ureg.kilogram / ureg.terawatt_hour

    return kgU_TWh * unit


if __name__ == "__main__":
    import sys

    sys.path.append(".")  # Add project root to Python path
    from utils.calculator import to_e_notation

    leu = 4.5e4
    efficiency = 1 / 3

    assert (
        to_e_notation(
            burnup_to_fuel_requirement(burnup=leu, efficiency=efficiency).magnitude
        )
        == "2.78e+03"
    ), f"expected 2.78e+03 got {to_e_notation(burnup_to_fuel_requirement(burnup=leu, efficiency=efficiency))}"
