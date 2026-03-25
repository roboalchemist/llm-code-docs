# Source: https://docs.acceldata.io/api/policy-executions-and-results.md

# Policy Executions & Results

Once Data Quality, Reconciliation, Drift, Freshness, and Anomaly policies are created, the next step is to **monitor policy runs, understand execution status, and analyze detailed results**.
 The Monitoring & Execution Visibility APIs let you:

- Track reliability checks across your entire data ecosystem
- Retrieve execution status for individual policies
- Analyze detailed results for failures, warnings, and SLA breaches
- View policy coverage and health at the asset level
- Fetch persistence paths for stored good/bad results
- Surface notifications and alerting metadata

These endpoints mirror the visibility tools in the ADOC UI and are essential for operationalizing data reliability.

## When to Use These APIs

Use these APIs when you need to:

- Build dashboards showing latest health of assets/policies
- Pull detailed execution results for investigations
- Integrate reliability results with observability or incident tools
- Identify which assets are protected by which policies
- Retrieve stored output files / persistence paths for failed checks

## Available Endpoints

| Action | Description | 
| ---- | ---- | 
| **List Executions** | List and filter executions across all policies or for a specific policy. | 
| **Execution Details** | Retrieve high-level metadata for a single execution. | 
| **Execution Results** | Fetch detailed rule-level or item-level results. | 
| **Asset-Centric Reliability View** | View all policies and latest execution results for an asset. | 
| **Persistence Path Configuration** | Retrieve and update where good/bad results are stored. | 
| **Notification Settings** | Understand notification groups, severity, alert settings tied to policies. | 
