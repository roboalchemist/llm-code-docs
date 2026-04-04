# Source: https://docs.acceldata.io/api/data-drift.md

# Data Drift

Data Drift Policies in Acceldata allow you to **detect unexpected shifts in data distributions** over time.  

These policies help ensure that data pipelines continue to behave reliably, even as underlying datasets evolve.  

You can use Data Drift checks to:

- Detect drift between training and inference datasets
- Monitor operational data for significant changes over time

- Trigger alerts or downstream workflows when thresholds are breached

Like other policy types, Data Drift policies are composed of rules and can be created, managed, executed, and monitored through the API.