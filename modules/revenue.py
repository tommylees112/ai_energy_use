def calculate_revenue(
    swu_requirements: dict, swu_price: float, market_share: dict
) -> dict:
    """Calculate revenue based on SWU requirements and costs."""

    return {
        "LEU": swu_requirements["LEU"] * swu_price * market_share["LEU"],
        "HALEU": swu_requirements["HALEU"] * swu_price * market_share["HALEU"],
        "total": (
            (swu_requirements["LEU"] * swu_price * market_share["LEU"])
            + (swu_requirements["HALEU"] * swu_price * market_share["HALEU"])
        ),
    }


if __name__ == "__main__":
    swu_results = {"LEU": 100, "HALEU": 100}
    swu_price = {"LEU": 100, "HALEU": 300}
    market_share = {"LEU": 0.5, "HALEU": 0.5}

    revenue_results = calculate_revenue(swu_results, swu_price, market_share)

    print(revenue_results)
