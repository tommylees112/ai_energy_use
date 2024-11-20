from graphviz import Digraph


def draw_workflow(
    base_demand, demand_results, nuclear_share, fuel_results, revenue_results
):
    dot = Digraph()

    dot.attr(rankdir="LR")
    dot.attr("node", shape="rectangle", style="rounded,filled", fillcolor="lightblue")

    base_demand_fmt = f"{base_demand:,.0f}"
    total_demand_fmt = f"{demand_results['total']:,.0f}"
    nuclear_demand_fmt = f"{demand_results['total'] * nuclear_share:,.0f}"
    revenue_fmt = f"{revenue_results['total'] / 1e9:.1f}"

    leu_fmt = f"{fuel_results['LEU'] / 1e6:.1f}"
    haleu_fmt = f"{fuel_results['HALEU'] / 1e6:.1f}"

    dot.node("A", f"Base Demand (2023)\n{base_demand_fmt} TWh")
    dot.node(
        "B1",
        f"Data Center Demand (2030)\n{demand_results['data_center']:,.0f} TWh",
    )
    dot.node(
        "B2",
        f"Other Additional Demand\n{demand_results['transport'] + demand_results['buildings'] + demand_results['non_data_centre_industry']:,.0f} TWh",
    )
    dot.node("C", f"Total Demand (2030)\n{total_demand_fmt} TWh")
    dot.node("D", f"Nuclear Share\n{nuclear_share * 100}%\n{nuclear_demand_fmt} TWh")
    dot.node("E", f"Fuel Requirements\nLEU: {leu_fmt}M kg\nHALEU: {haleu_fmt}M kg")
    dot.node("F", f"Revenue\n{revenue_fmt}B$")

    dot.edge("A", "C")
    dot.edge("B1", "C")
    dot.edge("B2", "C")
    dot.edge("C", "D")
    dot.edge("D", "E")
    dot.edge("E", "F")

    return dot


if __name__ == "__main__":
    print("workflow diagram")
