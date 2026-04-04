# Source: https://docs.acceldata.io/documentation/atlan.md

# Atlan

Atlan is a modern data collaboration and governance platform that enables teams to easily discover, understand, and trust their data. With Acceldata Data Observability Cloud (ADOC), you can seamlessly publish data reliability insights—such as Data Quality Scores, Reliability Scores, and policy execution results—directly into Atlan’s metadata framework.

This integration gives governance and analytics users complete visibility into data health without leaving Atlan, helping them make confident and timely decisions.

## What this Integration Enables

Once integrated, ADOC can automatically push the following metadata into Atlan:

- **Data Reliability Score**
- **Data Quality Score**
- **Reconciliation Score (if applicable)**
- **Policy execution results & status**
- **Direct navigation link back to ADOC for detailed insights**
- **Trust indicators (via Trust Badge configuration)**

This ensures that Atlan users always see up-to-date data health information for assets coming from Acceldata-observed systems.

## Prerequisites

Before you begin, ensure the following:

### In Atlan

- Atlan Base URL 
- Atlan API Token (via Service Principal)
- A Persona with required access policies
- Permissions to read/write custom metadata
- Admin access to configure API credentials

### In Acceldata (ADOC)

- ADOC environment with Data Reliability enabled
- The data source you want to link is already registered
- Access rights to add new external connectors

### Configure API Access in Atlan

Before connecting Atlan to ADOC, set up secure API access.

#### 1. Create an API Key (Service Principal)

1. Log in to Atlan with an admin account.
2. Navigate to **Admin → API Tokens**.
3. Generate a new API Token.

#### 2. Create a Persona for ADOC

1. Go to **Governance → Personas**.
2. Create a Persona (e.g., _ADOC Integration User_).

#### 3. Assign Access Policies

Ensure the Persona has policies that allow:

- Reading metadata
- Updating custom metadata fields
- Writing custom attributes from ADOC

> These permissions allow ADOC to push policy metadata into Atlan assets.

## Add Atlan as a Data Source

Follow these steps to add Atlan as a data source:

1. Navigate to **Register** -&gt; **Add Data Source** and select Atlan from the list of data sources.
2. In the **Basic Details** page, provide a **Data Source Name** and **Description** (optional).
3. Click **Next** to proceed to the **Connection Details** page.
4. Enter the **Atlan Base URL**.
5. Enter the **API Token**.
6. Click **Test Connection** to validate the connection. If the connection fails, verify the entered connection details and try again.
7. Click Next to proceed to the **Observability Set Up** page. 
8. Configure how ADOC metadata appears in Atlan:
    1. **Enable Trust Badge**
    2. **Warning Threshold** and **Deprecated Threshold**
    3. **Add Mapping** – map the Atlan asset to the corresponding ADOC data source.

9. Click **Submit** to complete the registration of the data source.

## Map ADOC Assets to Atlan Assets

Mappings determine where ADOC will publish reliability scores.

For each Atlan asset, specify the corresponding ADOC data source based on:

- Asset name
- Data source type
- Schema or table-level alignment

> Without mapping, ADOC will not publish metadata to Atlan.
> 
> ## View ADOC Scores and Policy Results in Atlan
> 
> Once you integrate the Atlan data catalog with an ADOC data source, they can seamlessly access policy scores, and metadata of the ADOC asset within the Atlan workspace. Any policies executed on the mapped Acceldata data source, such as reconciliation or data quality policies, will have their execution status, results, and metadata reflected in Atlan.
> 
> For example, if a reconciliation policy runs on an Acceldata data source mapped to Atlan, its execution status (successful or failed) and data quality assessment (reliable or unreliable) can be viewed directly in Atlan. Users can also drill down into execution details for further analysis.
> 
> Additionally, asset details and an ADOC summary, including the Data Reliability Score, Data Quality Score, and Reconciliation Score, can be viewed within the Atlan asset overview workspace. This integration ensures data reliability insights from Acceldata are accessible within Atlan, helping users make informed decisions about data quality, freshness, and drift.