# Source: https://docs.acceldata.io/documentation/tableau.md

# Tableau

Integrate **Tableau** with **Acceldata Data Observability Cloud (ADOC)** to extend observability to your visualization layer. The Tableau connector allows users to catalog Tableau assets, understand data lineage, and ensure visibility into how data from various sources is represented and consumed in Tableau dashboards.

**Tableau** is a leading analytics and business intelligence platform known for its rich visualization capabilities. Integrating Tableau with ADOC enables teams to analyze the relationships between visualized data and its upstream sources, ensuring trustworthy insights and accurate reporting.

ADOC’s Tableau integration supports metadata ingestion, **automatic lineage generation**, and relationship mapping—helping users trace data from external systems to Tableau visualizations.

## Supported Authentication Methods

| Authentication Method | Description | 
| ---- | ---- | 
| Personal Access Token (PAT) | Authenticate using a Tableau Personal Access Token (PAT) name, secret key, server host, and site ID. | 


## Prerequisites

Before integrating Tableau with ADOC, ensure the following:

- You have valid **Tableau credentials** (PAT name, PAT secret key, Server URL, and Site ID).
- You have access to Tableau **REST and Metadata APIs**.
- The required **permissions** are granted to your Tableau account for metadata access.

### Required Permissions

| Permission | Description | 
| ---- | ---- | 
| **View Metadata API** | Allows access to Tableau metadata (workbooks, dashboards, sheets, etc.). | 
| **Read Projects and Workbooks** | Required to crawl Tableau projects and extract metadata. | 
| **Access REST API** | Enables connection validation and interaction with Tableau Server/Cloud. | 


### Configuration Parameters

| Parameter | Description | Mandatory | Example | 
| ---- | ---- | ---- | ---- | 
| **Data Source Name** | Unique name for the Tableau connection. | ✅ | `Tableau_Production` | 
| **Description** | Optional notes about the data source. | ❌ | `Metadata from Tableau Cloud` | 
| **Data Plane** | The ADOC Data Plane where processing occurs. | ✅ | `dp-us-east` | 
| **Server Host** | Tableau Server hostname or Cloud URL. | ✅ | `https://10az.online.tableau.com` | 
| **PAT Name** | Personal Access Token Name for authentication. | ✅ | `ADOCConnector` | 
| **PAT Secret Key** | Secret token associated with the PAT. | ✅ | `abcd1234xyz...` | 
| **Site ID** | Tableau Site identifier. | ✅ | `my-site` | 


## Adding Tableau as a Data Source

Follow these steps to register Tableau in ADOC:

1. Navigate to **Register -&gt; Data Sources**.
2. Click **Add Data Source -&gt; Tableau** from the list of data sources.
3. Enter the **Data Source Name** and optional **Description**.
4. Ensure the **Data Reliability** toggle is enabled.
5. Select a **Data Plane** or create a new one if required.
6. Click **Next** to open the **Connection Details** page.
7. Provide the following:
    - PAT Name
    - PAT Secret Key
    - Tableau Server Host
    - Tableau Site ID

8. Click **Test Connection** to validate the credentials.
    - If successful, a “Connected” status appears.
    - If unsuccessful, verify the credentials and access permissions.

9. Click **Next** to configure **Observability Settings**.
10. (Optional) Enable **Crawler Execution Schedule** to automatically refresh Tableau metadata.
11. Click **Submit** to register Tableau as a data source.

## Tableau Entities in ADOC

Once connected, Tableau metadata is mapped into ADOC as structured entities.

| Tableau Entity | Mapped ADOC Asset | Description | 
| ---- | ---- | ---- | 
| Site | TABLEAU_SITE | Tableau site containing projects. | 
| Project | TABLEAU_PROJECT | Logical grouping of related content. | 
| Workbook | TABLEAU_WORKBOOK | Collection of sheets and dashboards. | 
| Sheet | TABLEAU_SHEET | Single visualization view. | 
| Dashboard | TABLEAU_DASHBOARD | Group of visualizations and sheets. | 
| Data Source | TABLEAU_DATASOURCE | Connection to the underlying data. | 
| Field | TABLEAU_FIELD | Column or attribute within a dataset. | 


## Data Lineage for Tableau

ADOC automatically builds **end-to-end data lineage** between Tableau and upstream data systems. To view Tableau lineage:

1. Navigate to **Reliability** -&gt; **Discover Assets**.
2. Select the registered **Tableau** data source.
3. Choose a workbook or dashboard.
4. Click the **Lineage** tab to visualize the data flow from source systems to Tableau.

You can toggle between **Structure**, **Lineage**, and **Relationship** views to explore dependencies and connections across your environment.

### Auto Lineage Discovery (v4.9.0 and later)

Starting with **ADOC v4.9.0**, the Tableau connector now supports **automatic lineage generation** between Tableau’s internal and external assets.

Using Tableau’s **GraphQL Metadata APIs**, ADOC automatically fetches and builds lineage relationships based on asset connections and data dependencies.
 This enhancement eliminates the need for manual lineage creation and ensures that Tableau visualizations and flows are contextually connected to their underlying data sources.

#### Key Highlights

- **Internal and External Lineage Coverage:** ADOC now auto-generates lineage across Tableau’s internal assets (sites, projects, workbooks, dashboards, sheets, and data sources) and external data systems (e.g., Snowflake, BigQuery, etc.).
- **New Asset Type – Tableau Flow:** A new entity called **Tableau Flow** is now discovered during metadata crawling. Tableau Flows represent data preparation workflows within Tableau, and their **input and output fields** are now captured in ADOC lineage views.
- **Automated GraphQL-Based Lineage:** Lineage relationships are derived directly from Tableau’s GraphQL metadata APIs, ensuring more accurate and up-to-date relationships across Tableau environments.

#### Viewing Tableau Lineage

Once the Tableau data source is successfully crawled:

1. Navigate to **Reliability** -&gt; **Discover Assets.**
2. Click on your Tableau data source. The **Relationships** tab is displayed.
3. Select a **Workbook**, **Dashboard**, **Sheet**, or **Flow**.
4. Open the **Lineage** tab to view connected Tableau entities and their upstream data sources.

Lineage visualizations now show both Tableau-internal dependencies and external system relationships (e.g., Snowflake tables feeding Tableau data sources).

## Next Steps

- Enable scheduled crawlers to keep Tableau metadata in sync.
- Explore lineage views to trace data from source systems to visualizations.
- Combine Tableau lineage with upstream data sources (e.g., Snowflake) for a complete visibility chain.