import streamlit as st

from modules import fuel_efficiency, nuclear_supply, revenue, swu, us_demand
from utils.workflow_diagram import draw_workflow

# ================================
# SIDEBAR
# ================================
# Sidebar Inputs
enable_advanced = st.sidebar.checkbox("Enable Advanced Settings", value=False)

st.sidebar.header("2030 Demand Inputs")
base_demand = st.sidebar.number_input(
    "Base Demand 2023 (TWh)[^9]", value=4250, step=10, disabled=not enable_advanced
)
transport = st.sidebar.number_input(
    "Transport 2030 (TWh)[^6]", value=250, step=10, disabled=not enable_advanced
)
buildings = st.sidebar.number_input(
    "Buildings 2030 (TWh)[^6]", value=50, step=10, disabled=not enable_advanced
)
non_data_center_industry = st.sidebar.number_input(
    "non_data_center Industry 2030 (TWh)[^7]",
    value=67,
    step=10,
    disabled=not enable_advanced,
)
data_center = st.sidebar.number_input("Data Center 2030 (TWh)", value=33, step=10)
nuclear_share = st.sidebar.slider("Nuclear Share 2030 (%)", 0.0, 1.0, 0.18)
share_of_nuclear_leu = st.sidebar.slider("LEU % of Nuclear 2030 (%)", 0.0, 1.0, 0.7)

st.sidebar.header("Fuel Efficiency Inputs")
nuclear_thermal_efficiency = st.sidebar.slider(
    "Nuclear Thermal Efficiency (%)", 0.0, 1.0, 0.33, disabled=not enable_advanced
)
leu_burnup = st.sidebar.number_input(
    "LEU Burnup (MWd/tU)", value=4.5e4, disabled=not enable_advanced
)
haleu_burnup = st.sidebar.number_input(
    "HALEU Burnup (MWd/tU)", value=1e5, disabled=not enable_advanced
)

st.sidebar.header("SWU Inputs")
swu_price = st.sidebar.number_input("SWU Price ($/SWU)", value=107)
swu_leu = st.sidebar.number_input(
    "LEU SWUs per kg (SWU/kg)", value=5, disabled=not enable_advanced
)
swu_haleu = st.sidebar.number_input(
    "HALEU SWUs per kg (SWU/kg)", value=30, disabled=not enable_advanced
)

# Computation inputs
market_share_leu = st.sidebar.slider("LEU Market Share (Centrus)", 0.0, 1.0, 0.5)
market_share_haleu = st.sidebar.slider("HALEU Market Share (Centrus)", 0.0, 1.0, 0.8)

# ================================
# CALCULATIONS
# ================================
# Calculate Total Demand
demand_results = us_demand.calculate_demand(
    base_demand, transport, buildings, non_data_center_industry, data_center
)

# Nuclear Demand
nuclear_demand = nuclear_supply.calculate_nuclear_demand(
    demand_results["total"], nuclear_share
)

share_of_nuclear_haleu = 1 - share_of_nuclear_leu
leu_demand = share_of_nuclear_leu * nuclear_demand
haleu_demand = share_of_nuclear_haleu * nuclear_demand

twh_fuel_results = {
    "LEU": leu_demand,
    "HALEU": haleu_demand,
    "total": leu_demand + haleu_demand,
}

# Fuel Efficiency
leu_kg_twh = fuel_efficiency.burnup_to_fuel_requirement(
    burnup=leu_burnup, efficiency=nuclear_thermal_efficiency
).magnitude
haleu_kg_twh = fuel_efficiency.burnup_to_fuel_requirement(
    burnup=haleu_burnup, efficiency=nuclear_thermal_efficiency
).magnitude

fuel_results = {
    "LEU": leu_kg_twh * leu_demand,
    "HALEU": haleu_kg_twh * haleu_demand,
}

# # SWU Required to produce kg of fuel
swu_results = swu.calculate_number_swu(
    fuel_results, {"LEU": swu_leu, "HALEU": swu_haleu}
)

# Revenue
market_share = {"LEU": market_share_leu, "HALEU": market_share_haleu}
revenue_results = revenue.calculate_revenue(swu_results, swu_price, market_share)

# ================================
# SUMMARY
# ================================
st.markdown("# Centrus Opportunity in 2030")

revenue_fmt = f"{revenue_results['total'] / 1e9:.2f}"
nuclear_demand_fmt = f"{nuclear_demand:.1f}"

# Display summary statistics
st.subheader("Summary")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Data Center Demand 2030", f"{data_center:,.0f} TWh")
with col2:
    st.metric("Total Nuclear Demand 2030", f"{nuclear_demand_fmt} TWh")
with col3:
    st.metric("Total Revenue 2030", f"{revenue_fmt}B$")

# ================================
# WORKFLOW DIAGRAM
# ================================
# Create the diagram
st.subheader("Workflow Diagram")
diagram = draw_workflow(
    base_demand=base_demand,
    demand_results=demand_results,
    nuclear_share=nuclear_share,
    fuel_results=fuel_results,
    revenue_results=revenue_results,
)

# Display the diagram
st.graphviz_chart(diagram)

# ================================
# BODY OF RESULTS
# ================================
st.subheader("Computations")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Energy Demand")
    st.write("2030 Total Demand (TWh):", demand_results["total"])
    st.write("Nuclear Demand (TWh):", nuclear_demand)
    st.write("Fuel Demand (TWh):", twh_fuel_results)

with col2:
    st.markdown("#### Fuel Requirements")
    st.write("Fuel Requirement (kg):", fuel_results)
    st.write("SWU Results (# SWUs):", swu_results)

with col3:
    st.markdown("#### Revenue")
    st.write("Revenue Results ($):", revenue_results)


# ================================
# MARKDOWN REFERENCES
# ================================

references = {
    "1": "[Hannah Ritchie AI Energy Demand](https://www.sustainabilitybynumbers.com/p/ai-energy-demand)",
    "2": "[SemiAnalysis AI Datacenter Energy Dilemma Race](https://semianalysis.com/2024/03/13/ai-datacenter-energy-dilemma-race/)",
    "3": "[Argonne National Laboratory Study on HALEU Burnup](https://publications.anl.gov/anlpubs/2023/06/182926.pdf)",
    "4": "[Nuclear Thermal Efficiency 33%](https://www.nuclear-power.com/nuclear-engineering/thermodynamics/laws-of-thermodynamics/thermal-efficiency/)",
    "5": "[LWR (using LEU) Burnup 4.5e4 MWd/tU](https://www.euronuclear.org/glossary/burn-up/) and [here too](https://www.nuclear-power.com/nuclear-power/reactor-physics/reactor-operation/fuel-burnup/)",
    "6": "[IEA World Energy Outlook October 2024](https://www.iea.org/reports/world-energy-outlook-2024)",
    "7": "We set the non-data center industry demand to 67 TWh because we assume that the data center demand will grow by 33 TWh by 2030[^6]",
    "8": "[EIA - 2023 US Electricity Explained](https://www.eia.gov/energyexplained/electricity/electricity-in-the-us-generation-capacity-and-sales.php#:~:text=At%20the%20end%20of%202023,electricity%2Dgeneration%20capacity%20in%202023.)",
    "9": "[Our World in Data - Energy Consumption](https://ourworldindata.org/energy)",
    "10": "[Ember Energy Yearly Electricity Data](https://ember-climate.org/data-catalogue/yearly-electricity-data/)",
    "11": "[]()",
}


# Then wrap your references in a div
st.markdown('<div class="reference-section">', unsafe_allow_html=True)
st.markdown("## References")
for num, ref in references.items():
    st.markdown(f"{num}. {ref}")
st.markdown("</div>", unsafe_allow_html=True)
