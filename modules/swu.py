def calculate_number_swu(fuel_requirements: dict, swu_per_kg: dict) -> dict:
    """
    Calculate SWU requirements for each fuel type.

    kg * (#SWU / kg) = #SWU
    """
    return {
        "LEU": fuel_requirements["LEU"] * swu_per_kg["LEU"],
        "HALEU": fuel_requirements["HALEU"] * swu_per_kg["HALEU"],
    }


if __name__ == "__main__":
    calculate_number_swu
