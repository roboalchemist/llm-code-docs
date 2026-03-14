# Source: https://docs.acceldata.io/documentation/azure-synapse-analytics.md

# Microsoft Azure Synapse

**Azure Synapse Analytics** is a unified analytics platform that combines data warehousing, big data processing (via Apache Spark), and log/timeseries analysis. It brings together SQL, Spark, and Data Explorer capabilities into a single workspace—helping organizations analyze data efficiently and at scale.

## Prerequisites

Ensure the following requirements are met before you connect Azure Synapse as a data source:

- ADOC access & permissions to add data sources.
- An existing data plane in ADOC or create one for Azure Synapse Analytics ingestion. See the [Data Plane Installation](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) documentation for more information.
- [Azure Synapse workspace details](https://learn.microsoft.com/en-us/azure/synapse-analytics/), including:
    - Workspace name
    - SQL Pool configuration (e.g., Dedicated SQL Pool)
    - Authentication credentials (SQL user/password, Managed Identity, or Service Principal)

## Add Azure Synapse Analytics as a Data Source

### Step 1: Start Setup

1. From the left main menu, select **Register** -&gt; **Add Data Source**.
2. Select **Azure Synapse Analytics** from the list.
3. On the **Data Source Details** page:
    1. Enter a **Data Source Name** and optional **Description** for the data source.

4. Ensure the Data Reliability toggle is enabled and select a data plane.
5. Click **Next**.

### Step 2: Add Connection Details

1. Enter your **Azure Synapse workspace name**.
2. Select a **SQL Pool configuration** method (currently, **Dedicated SQL Pool Name** is supported).
3. Authentication options:
    1. **Username & Password:** Provide the SQL Pool name, username, and password.
    2. **Managed Identity (optional):** Use for secure Azure credential-based access. If enabled, assign a Managed Identity to access Synapse via Azure credentials.
    3. **Service Principal (optional):** Use for Azure AD-based authentication with Client ID, Client Secret, and Tenant ID.
    4. **Secret Manager (optional):** Use when storing credentials in a secure secret store. Provide workspace, SQL Pool details, username, and secret configuration details.

4. Select the **Data Plane Engine**: Choose either **Spark** or **Pushdown** for better performance during profiling and checks.
5. Click **Test Connection**. If successful, proceed. Otherwise, double-check your entries and network connectivity.
6. Click **Next** to proceed to configure observability.

### Step 3: Set Up Observability

1. Set a **scan schedule**, including frequency and time zone, so ADOC can crawl Synapse for metadata and quality metrics.
2. Enable **Notifications** for crawler success or failure alerts.
3. Click **Submit** to finalize the setup.

## Troubleshooting and FAQs

**1. Connection Error After Test Connection**

- **Issue**: ADOC fails to connect.
- **Solution**: Verify workspace and SQL Pool names, authentication credentials, firewall settings, and whether you're using the correct Data Plane Engine.

**2. Performance Slowness in Profiling**

- **Issue**: Profiling or data checks take too long.
- **Solution**: Switch to **Pushdown** engine for faster execution using Synapse’s native compute.

**3. Freshness Metrics Not Visible**

- **Issue**: No freshness or data latency information shows up.
- **Solution**: Use a **Row Count Check** as a proxy metric for freshness, or rely on external solutions like ADF (Azure Data Factory) SLAs.

## What’s Next

- **Profile your Azure Synapse Analytics data source** to begin applying Data Reliability policies.
- **Create and apply observability policies:** Define Data Quality, Schema Drift, and Anomaly Detection checks. _(No dashboards until policies are in place.)_
- **Configure alerts:** Proactively notify your team on quality or pipeline issues.