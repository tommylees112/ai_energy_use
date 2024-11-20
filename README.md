# Nuclear Energy Demand Calculator 2030 ☢️

A Streamlit application for forecasting nuclear energy demand and revenue potential through 2030.

## Modules

- **US Demand Module**: Calculates total energy demand (2023 -> 2030)
    - **Nuclear Supply**: Determines nuclear energy share in total energy mix
- **Fuel Efficiency Module**: Computes LEU/HALEU energy output per unit (TWh/kg)
- **SWU Module**: Converts fuel demand to separative work units (SWU)
- **Revenue Module**: Calculates revenue based on fuel supply and pricing

### Using UV (Recommended) ⚡
```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Run the app
uv run streamlit run app.py
```

## Data Sources

### Historical Data
Ember (2024) and Energy Institute - Statistical Review of World Energy (2024), processed by Our World in Data.

### References
1. [Hannah Ritchie AI Energy Demand](https://www.sustainabilitybynumbers.com/p/ai-energy-demand)
2. [SemiAnalysis AI Datacenter Energy Dilemma Race](https://semianalysis.com/2024/03/13/ai-datacenter-energy-dilemma-race/)
3. [Argonne National Laboratory Study on HALEU Burnup](https://publications.anl.gov/anlpubs/2023/06/182926.pdf)
4. [Nuclear Thermal Efficiency 33%](https://www.nuclear-power.com/nuclear-engineering/thermodynamics/laws-of-thermodynamics/thermal-efficiency/)
5. [LWR (using LEU) Burnup 4.5e4 MWd/tU](https://www.euronuclear.org/glossary/burn-up/)
6. [IEA World Energy Outlook October 2024](https://www.iea.org/reports/world-energy-outlook-2024)
7. Non-data center industry demand assumption: 67 TWh
8. [EIA - 2023 US Electricity Explained](https://www.eia.gov/energyexplained/electricity/electricity-in-the-us-generation-capacity-and-sales.php)

## License
MIT