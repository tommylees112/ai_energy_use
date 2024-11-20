def calculate_nuclear_demand(total_demand: float, nuclear_share: float) -> float:
    """Calculate the nuclear power demand based on total demand and nuclear share percentage.

    Args:
        total_demand: Total electricity demand in TWh
        nuclear_share: Percentage of demand to be met by nuclear (0-100)

    Returns:
        Nuclear power demand in TWh
    """
    assert 0 <= nuclear_share <= 1

    return total_demand * nuclear_share
