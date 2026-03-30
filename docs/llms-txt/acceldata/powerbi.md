# Source: https://docs.acceldata.io/documentation/powerbi.md

# Microsoft Power BI

Use Microsoft Power BI to monitor the reliability and integrity of your Power BI dashboards, datasets, and reports. After connecting, ADOC crawls Power BI content, tracks metadata, monitors data lineage, and identifies potential data issues in your Power BI environment.

### Prerequisites

Ensure the following requirements are met before you connect Power BI as a data source:

- **Service Principal Authentication:** Connect ADOC to Power BI by first registering an application in Microsoft Entra ID (formerly Azure Active Directory). This creates a service principal, securely identifying ADOC when accessing Power BI APIs. This involves:
    1. **Create an Azure Service Principal** from Microsoft Entra ID (Azure Active Directory).
        1. Navigate to _Microsoft Entra ID → App registrations → New registration._
        2. Select options as applicable, enter a name for the Service Principal, and register it.
        3. If you do not have sufficient permissions, request your Azure Administrator to perform this step.

    2. **Generate a Client Secret** for the Service Principal and copy the **secret value** (not the secret ID).
        1. Go to _Entra ID → App registrations → Your application → Certificates & secrets → New client secret_.
        2. Provide a description and set an expiry period.
        3. Select **Add**, then copy the secret value for later use.

    3. **Create or Assign to an Azure Security Group**
        - From Azure portal, create a new user group or add the Service Principal to an existing group intended to connect to Power BI workspaces.

    4. **Grant Power BI Admin API Permissions**
        - In the Power BI Admin Portal, allow the group to access **Read-Only Admin APIs** and any other required permissions.

    5. **Enable Admin API Access in Microsoft Fabric**
        - In Microsoft Fabric Admin Portal → _Tenant Settings → Admin API settings_, add the group created in Step 3 to each relevant section.

    6. **Assign Read-Only Workspace Access**
        1. Navigate to _Admin Portal → Workspaces_ in Microsoft Fabric.
        2. Add the group created in Step 3 as a **Viewer** to each Power BI workspace you want to monitor. 

**Note:** Assigning the permission to the Azure Group can take ~1.5–2 hours to propagate. If you are adding a Service Principal to a group that already has workspace permissions, the change is effective immediately.

- Users must be on **Data Plane v4.6.0** to integrate Power BI as a data source.

### Add Power BI as a Data Source

To set up Power BI in ADOC, follow these steps:

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source**.
3. Select **Power BI** from the list of data sources.
4. On the **Data Source Details** page:
    1. Name the data source.
    2. Add a short description (optional).
    3. Enable Data Reliability and choose your data plane from the dropdown.

5. Click **Next**.

### Step 2: Add Connection Details

1. Enter these authentication details from your registered Azure AD application (service principal):
    1. **Power BI Tenant ID**: This is your Microsoft Azure Active Directory tenant's unique ID (also called the Directory ID). To find your Tenant ID, refer this [document](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant).
    2. **Power BI Client ID**: This is the app's ID in Microsoft Entra ID (formerly Azure AD).
    3. **Power BI Secret Key**: This is the app's secret key (password).

2. Add the app to a security group with read-only access to the Power BI workspaces you want to monitor.
3. Select **Test Connection**. If successful, you'll see "Connected." Otherwise, check your credentials and permissions.

### Step 3: Setup Observability

Specify which parts of your Power BI environment to monitor for data reliability and how often. These settings help reduce unnecessary scanning and focus the crawler only on what matters to you.

1. **Select Workspaces**: Select the Power BI workspace(s) to monitor. Only dashboards and reports from these workspaces will be monitored.
2. **Select Source Connections (Optional)**: Select the data source (e.g., BigQuery, Snowflake, Databricks) associated with your Power BI dashboards.

_Why this matters: Selecting a source narrows the crawl scope.__Example: Selecting Snowflake limits the crawler to Power BI assets using Snowflake data, improving speed and accuracy. This significantly reduces processing time and increases the accuracy of the metadata and lineage mapping._

3. **Include Dashboards and Reports (Regex)**: Enter the exact dashboard or report names, or use regular expressions to match patterns.
Examples:
4. Exact match: `sample_powerbi`
5. Regex: .`*powerbi` (finds names ending with "powerbi")
6. Leave blank to include all dashboards and reports in the selected workspaces.
7. **Exclude Dashboards and Reports (Regex)**: Filter out specific dashboards or reports (even those in selected workspaces). Regex is supported here as well. Note: Exclusion rules override inclusion.
8. Use **Crawler Execution Schedule** to set when the crawler scans selected dashboards for reliability issues:
    1. Set the crawler's run frequency (e.g., daily)
    2. Set the time and time zone
    3. Add multiple times as needed

9. **Set Notifications:**
    1. Notify on Crawler Failure: Select one or more channels for failure alerts.
    2. Notify on Success: Receive success notifications (toggle on/off).

10. Select **Submit** to save your configuration and begin monitoring the Power BI data source.

### After Integration

After you integrate Power BI with Acceldata using a supported connection (like BigQuery, Snowflake, or Databricks), Acceldata will begin crawling relevant Power BI assets and mapping them to your underlying data sources. Ensure you are upgrade your Data Plane to v4.6.0 and re-crawl existing Power BI data sources to work as expected. Here's how this helps you:

1. **Context Aware Crawling**: When setting up a source connection, Acceldata uses it to focus the analysis. Instead of scanning every Power BI workspace, it will only crawl those linked to your selected source. Acceldata analyzes these Power BI assets:
    - **Power BI Semantic Model** (previously called **Dataset object** in ADOC): Represents a collection of tables and measures, forming the foundation for reports. The terminology change aligns with recent updates from Microsoft Power BI.
    - **Power BI DataFlow Entity**: Includes transformed data from Power BI.
    - **Power BI DataFlow Attributes**: Metadata for each field.
    - **Power BI Report Pages**: Visuals and pages in your Power BI dashboards.

2. **End-to-End Lineage**: Acceldata shows the data lineage starting from the Power BI workspace, providing a complete view.
    - Workspace Contextualization: The lineage starts at the Power BI workspace, helping you track how everything connects.
    - Power BI now links semantic models and dataflows for better visibility.
    - Column-level lineage shows data down to individual columns, including:
        - Column data types (left).
        - Column and table data quality scores (right, where available).

3. **Faster Troubleshooting with Impact Analysis**: Impact analysis speeds troubleshooting: If an upstream dataset fails, the lineage view highlights affected Power BI assets (dashboards, etc.) with red borders. This helps you:
    - Prioritize investigations
    - Understand downstream impact
    - Fix issues faster

#### Lineage vs. Relationships in ADOC

Acceldata provides two views for exploring data asset connections: Lineage and Relationships. Although they may look similar at first glance, they serve different purposes.

| Feature | Lineage Tab | Relationships Tab | 
| ---- | ---- | ---- | 
| **Purpose** | Visualize the actual **data flow** from source to dashboard. | Understand **asset-level hierarchy and ownership** within the platform. | 
| **Use Case** | When you want to answer: *"Where does this data come from, and where does it go?"* | When you want to answer: *"Which workspace, report, or project does this asset belong to?"* | 
| **Level of Detail** | Fine-grained. Supports **column-level tracing** across assets. | High-level. Shows **logical grouping and hierarchy**, such as workspace → report → semantic model. | 
| **View Type** | Directed flow graph with upstream/downstream paths. | Parent-child tree or DAG view showing asset relationships. | 
| **Best for...** | - Impact analysis- Root cause analysis- Tracing upstream/downstream lineage | - Navigating organizational structure- Understanding report/report page/component relationships | 
| **Examples** | - BigQuery table → Power BI Dataflow → Semantic Model → Report Page- Data quality issues impacting dashboards | - Workspace &gt; Report &gt; Semantic Model &gt; Report Pages- Knowing which assets are grouped under which workspace | 


**When to use each tab:**

- **Use the Lineage tab when:**
    - You're troubleshooting **data quality issues**.
    - Trace the data flow.
    - Find details like data type, score, and dependencies for each column.

- **Use the Relationships tab to**:
    - Understand your Power BI ecosystem's structure.
See how workspaces, reports, dashboards, and pages relate.
    - Explore how assets are organized across projects or domains.

#### Viewing Power BI Lineage in ADOC

After Power BI integration and crawling, view its lineage to see data flow across source connections and Power BI items (semantic models, dataflows, reports).

**How to Access Lineage**

1. In the left navigation menu, select Discover Assets under Reliability.
2. Use the search bar to look for your Power BI asset by its data source name.
3. Click on the asset. The Lineage view appears.

**What You Can Do in the Lineage View**

- **Visualize Data Flow**: See how data flows between BigQuery/Snowflake tables and Power BI Dataflows, Semantic Models, Report Pages, and Dashboards.
- **Lineage Details**: Point to any column name in a table to see how it connects to other columns in upstream or downstream assets.
- **See column-level mappings** (names, data types, and data quality scores, if available) by toggling Show Sub-Level Lineage.
    - Column names
    - Column data types
    - Column-level data quality scores (if available)

- **Add Lineage**: To add a missing or custom relationship, click Add Lineage.
- **Search Within Tables**: Find columns quickly using the search bar.
- **Explore Asset Relationships**: Click any asset to see its metadata, related assets, and relationship/dependency trees (Relationships tab).
    - See its metadata
    - View related assets
    - Access relationship or dependency trees in the Relationships tab

### What’s Next

1. Use the Lineage Graph to understand how Power BI assets connect to your data warehouse.
2. Impact Analysis helps identify at-risk reports and dashboards.
3. Check Power BI's dataflows for improved model design and management.