def calculate_demand(
    base_demand: float,
    transport: float,
    buildings: float,
    non_data_centre_industry: float,
    data_center: float,
) -> dict:
    """Calculate total US electricity demand for 2030."""
    total = base_demand + transport + buildings + non_data_centre_industry + data_center
    return {
        "total": total,
        "base": base_demand,
        "transport": transport,
        "buildings": buildings,
        "non_data_centre_industry": non_data_centre_industry,
        "data_center": data_center,
    }
