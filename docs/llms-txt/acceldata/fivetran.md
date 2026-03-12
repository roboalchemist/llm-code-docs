# Source: https://docs.acceldata.io/documentation/fivetran.md

# Fivetran

Acceldata introduces **Fivetran integration** in ADOC v4.9.0, enabling users to observe, analyze, and visualize Fivetran data replication pipelines. This integration provides column-level lineage between Fivetran source and destination systems, allowing you to understand how data moves and transforms across your replication jobs.

**Fivetran** is a data replication service that automates data movement between heterogeneous systems—such as databases, APIs, and data warehouses—using an **ELT (Extract, Load, Transform)** approach.
ADOC’s integration focuses on the **Extract and Load** phases, capturing metadata and lineage from your Fivetran platform connections.

With this integration, users can:

- View end-to-end **pipeline lineage** between Fivetran source and destination systems.
- Access **column-level lineage** for detailed visibility into replicated data.
- Understand relationships between **Fivetran sync jobs**, source assets, and downstream analytics tools (such as Power BI or Tableau).
- Gain deeper operational insights into Fivetran replication behavior and schedule frequency.

Fivetran’s native UI provides limited visibility into the assets involved in replication. The ADOC integration bridges this gap by reading metadata that Fivetran platform connectors write to the associated destination (e.g., Snowflake). ADOC parses this metadata to:

- Construct **data pipelines**.
- Display **asset lineage and dependencies**.
- Surface metadata for operational observability.

This integration is designed for Fivetran customers using **SaaS deployments**, supporting both **account-level** and **destination-level** Fivetran platform connectors.

## Prerequisites

Before adding Fivetran as a data source in ADOC:

1. Ensure you have a valid **Fivetran API Key** and **Secret** **Key**.
2. Confirm that a **Fivetran Platform Connector** is already configured in your Fivetran environment.
3. The **Fivetran Platform Connector** must write metadata to a **destination data warehouse** (currently **Snowflake** is supported).
4. The Snowflake data source associated with this destination must be registered in ADOC and accessible using appropriate credentials.
5. Note that the metadata schema (e.g., `fivetran_metadata`) does **not** need to be crawled as a separate asset in ADOC.

## Adding Fivetran as a data source

1. Navigate to **Register** -&gt; **Data Sources**.
2. Click **Add Data Source** and select **Fivetran** from the list.
3. Enter the **Data Source Name** and optional **Description**.
4. Ensure the **Data Reliability** toggle is enabled.
5. Select a data plane or create a new one and click **Next** to proceed to the **Connection Details** page.
6. Enter the **API Key** and **Secret Key** for programmatic access.
7. Click **Test Connection** to verify access to the Fivetran account and click **Next**.
8. In the **Set Up Observability** page, select a **Fivetran Platform Connector** from the list displayed. The list shows all available connectors associated with your Fivetran account.
9. Map the **ADOC Snowflake data source** corresponding to the destination where Fivetran writes its metadata.
10. Enter the **Database** and **Schema** (for Snowflake) where metadata is stored. Example: `database_name:schema_name`.
11. Click **Validate** to confirm that ADOC can access the specified schema. Validation ensures that the database and schema exist and are readable.
12. Once validated, click **Submit** to register the data source.

## Metadata Collection and Scheduling

- ADOC retrieves pipeline metadata from the **destination database** where the Fivetran platform connector writes data.
- The internal Fivetran scheduler within ADOC aligns with Fivetran Platform Connector's own sync frequency, ensuring efficient and synchronized metadata collection.
- When a sync frequency changes in Fivetran, ADOC automatically adjusts its polling schedule during the next run.

## Viewing Lineage and Pipelines

After the integration is complete and metadata is synced:

1. Navigate to **Reliability** -&gt; **Discover Assets** and locate your Fivetran data source.
2. Open the Fivetran asset to view the **Details** page and click the **Lineage** tab.
    - Displays replication pipelines from **source to destination**, along with column-level lineage.

3. Open the **Lineage** tab to visualize the end-to-end flow.
    - Shows Fivetran replication steps between systems such as S3 &gt; Snowflake or BigQuery &gt; Snowflake.
    - Lineage extends downstream into BI tools (e.g., Power BI, Tableau), allowing you to trace data from origin to report.

4. Column-level lineage icons (Fivetran logos) indicate specific replication jobs between source and destination tables.

## Supported Configurations

| Category | Support | 
| ---- | ---- | 
| Deployment Mode | Fivetran SaaS | 
| Connector Type | Account-level and Destination-level Fivetran Platform Connectors | 
| Destination Systems | Snowflake (current release) | 
| Lineage Scope | Source-to-Destination table lineage and Column-level lineage | 
| Real-Time Monitoring | Not supported (metadata fetched per sync schedule) | 
