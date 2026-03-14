# Source: https://docs.acceldata.io/api/discover-assets.md

# Source: https://docs.acceldata.io/documentation/discover-assets.md

# Discover Assets

The **Discover Assets** page is your central workspace for understanding and managing data across your organization. Instead of logging into multiple systems like Snowflake, Oracle, BigQuery, or S3, you can see all datasets in one place. For each dataset, ADOC shows:

- **What the dataset is** (its source, name, and type).
- **Its current health** (policy compliance score, open alerts, and data quality checks).
- **Recent activity** (row counts, update frequency, profiling status).

This view makes it easier to spot valuable datasets and quickly identify where problems exist.

**Example**: Imagine your sales team wants to analyze quarterly revenue data. In the **Discover Assets** page, you search for _“Sales_Transactions”_. You immediately see that it’s stored in Snowflake, but its **policy score is only 62%**, with **two active alerts about missing values**. Instead of waiting until after the data causes errors in reports, you now know this dataset needs attention before being used for analysis.

## Access Control

What you see in Discover Assets depends on your **domain-based access**.

- Access is managed through [Authorization](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/authorization)  in ADOC.
- Roles (such as Viewer, Editor, Manager) and assigned domains decide which assets you can view or manage.

Note If you don’t see certain assets, it may be because you don’t have the right domain permissions.

## Page Layout

The Discover Assets page has five main areas:

1. **Navigator (Left Panel)**
    - Shows a tree of all connected data sources (e.g., Snowflake, Oracle, Kafka).
    - Expand or collapse a source to see the datasets inside.
    - Use this when you want to browse starting from a specific system.

2. **Filter Bar (Top)**
    - Search directly by asset name.
    - Apply filters such as:
        - **Tags**: assets with specific labels.
        - **Watched Assets**: assets you marked for closer tracking.
        - **Profiled**: assets where profiling has been run.
        - **Policy Configured**: assets with active monitoring policies.
        - **Example**: filter by “Profiled + Snowflake” to only see Snowflake datasets that have already been profiled.

Note If you click into an asset to open the **Asset Details page** and then return, your filters remain applied. This makes it easy to explore multiple datasets without losing your current search or filter settings.

3. **Main Panel (Asset List)**
    - Displays all assets that match your search or filters.
    - Each row shows: 
        - **Name**: the dataset’s name and source icon (click to open details). 
        - **Avg Policy Score**: how well the dataset complies with monitoring rules. 
        - **Open Alerts**: unresolved issues needing attention. 
        - **Policies Applied**: the number of Data Quality, Freshness, or Reconciliation policies. 
        - **Profile**: whether the asset has been statistically profiled. 
        - **Total Rows**: approximate data volume. 
        - **30-Day Update Count**: how often the dataset changed recently. 
        - **Recommendations**: system suggestions to improve monitoring.

Note  For **new assets**, these columns may be empty. This just means monitoring hasn’t started yet.

4. **Actions Menu (Top-Right)**
Use the Actions button to create or enhance assets:
    - **Add SQL View**: create a **virtual asset** defined by a custom SQL query. This behaves like a standard dataset but is computed dynamically from underlying data.
    - **Add Visual View**: build a **virtual asset** graphically by combining multiple datasets with joins or transformations. 
    - **Query Lineage**: upload SQL to trace data origin and dependencies.

Note Virtual assets can be profiled, monitored, and have policies applied just like physical datasets, without duplicating the underlying data.

5. **View Switcher (Top-Right)**
    - Switch between **Discover Assets view** (with the Navigator) or **Data Catalog view** (a simplified layout without the left panel).
    - Use the Catalog view if you already know what you’re looking for and want a cleaner screen.

## How to Find Assets

There are three main ways to locate assets:

1. **Browse by Source**: Open a system in the Navigator (e.g., Snowflake) and drill into its datasets.
    - Best when you know the source but not the exact name. 

2. **Filter by Details**:
Narrow the asset list by applying filters such as “Profiled” or “Has Open Alerts.”
    - Best when you don’t know the name but know some characteristics. 

3. **Search by Name**:
Type the dataset name (or part of it) in the search bar. Combine with filters for speed.
    - Best when you know the dataset’s name already. 

## Common Actions on Assets

Once you’ve located a dataset, you can:

- **Profile the dataset**: Run profiling to generate statistics (row counts, distinct values, anomalies). This is usually the first step before applying policies.
- **Start Monitoring**: Apply data quality, freshness, or reconciliation policies.
- **Investigate Issues**: If there are open alerts, click the dataset name to see details and suggested fixes.
- **Enrich the Asset**: Create virtual assets such as SQL Views or Visual Views, or add Query Lineage to reshape and trace data.

## What’s Next

- **For new datasets**: Run **profiling first**. Profiling creates the baseline statistics that ADOC uses for quality checks and monitoring.
- **For monitored datasets**: Open the Asset Details page to dive deeper into scores, alerts, and history.
- **For priority datasets**:  Use recommendations to decide where to add policies or governance.