# Source: https://docs.acceldata.io/documentation/azure-mssql.md

# Microsoft Azure MSSQL

**Azure MSSQL** is a fully managed, cloud-based relational database service that brings the power of SQL Server to the cloud. It offers scalability, security, and performance without infrastructure overhead—ideal for businesses seeking reliable and managed database solutions in Microsoft Azure.

## Prerequisites

Ensure the following requirements are met before you connect Azure MSSQL as a data source:

- **Azure MSSQL Credentials:** JDBC connection details (URL format, username, password)
- **ADOC Account & Permissions:** Access rights to add new data sources in your ADOC environment.
- **Data Plane:** An existing data plane in ADOC or readiness to create one for Azure MSSQL ingestion. See the [Data Plane Installation Guide](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) for more information.

### Authentication prerequisites (pick the one you plan to use)

- **Username/Password**: SQL authentication user with read access to target schemas.
- **Managed Identity**: A system-assigned or user-assigned Managed Identity with appropriate Azure role assignments.
- **Service Principal (Azure AD App Registration)**
    - Client ID (Application ID), Client Secret, and Azure Tenant ID.
    - The Service Principal must be granted database access and read permissions.

## Add Azure MSSQL as a Data Source

### Step 1: Start Setup

1. From the main menu, select **Register** -&gt; **Add Data Source**.
2. Select **Azure MSSQL** from the list.
3. On the **Data Source Details** page:
    1. Enter a name and optional Description for the data source.
    2. Ensure the Data Reliability toggle is enabled and select the data plane.

4. Click **Next**.

### Step 2: Configure Authentication

#### Option A  - Username / Password

1. Enter the **JDBC URL** in the format: `jdbc:sqlserver://<hostname>:<port>;databaseName=<database>`
2. Enter **Username** and **Password**.
3. Click **Test Connection**. If it fails, check the URL, credentials, and firewall rules.
4. Click **Next**.

#### Option B - Azure Managed Identity

Use Managed Identity to avoid storing credentials.

**B1. Grant Access in Azure**

1. In **Azure Portal**, open your Azure SQL Database (or server).
2. In **Access control (IAM)**, assign a suitable role (for example, **SQL DB Contributor**) to the Managed Identity (system- or user-assigned).
3. Ensure Azure AD admin is configured for the server so Azure AD identities can be granted DB access.

**B2. Create a Database User for the Identity**

Run the following as the **Azure AD admin** in the target database (replace the bracketed value with your identity display name):

```sql
CREATE USER <ManagedIdentityName> FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER <ManagedIdentityName>;
GRANT VIEW DATABASE STATE TO <ManagedIdentityName>;
```



**B3. Configure in ADOC**

1. In the **Azure MSSQL Connection Details** page, select **Use Managed Identities**.
2. Click **Test Connection**, then **Next**.

#### Option C - Service Principal

Use a Service Principal when you need an app-scoped identity with a **Client ID / Client Secret / Tenant ID**.

**C1. Prepare the Service Principal**

1. In **Azure Portal**, register an application (App registration).
2. Capture the **Client ID (Application ID)** and **Tenant ID**.
3. Create a **Client Secret** and note its value.

**C2. Grant Azure and database access**

1. Ensure the Azure SQL Server has an **Azure AD admin** configured.
2. In the target database, create a contained user for the Service Principal and grant read permissions: A contained user is a database-level identity not tied to the SQL Server instance, allowing easier mapping to Azure AD applications.

```sql
CREATE USER <ServicePrincipalDisplayName-or-AppID> FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER <ServicePrincipalDisplayName-or-AppID>;
GRANT VIEW DATABASE STATE TO <ServicePrincipalDisplayName-or-AppID>;
```



Tip _You can use the display name or the app’s Object ID in the `CREATE USER` statement, depending on your directory configuration._

**C3. Configure in ADOC**

1. Toggle **Use Service Principal**.
Enter:
    1. **Service Principal Client ID**
    2. **Service Principal Client Secret**
    3. **Azure Tenant ID**

2. Click **Test Connection**, then **Next**.

### Step 3: Set Up Observability

1. Select the schemas or databases you want ADOC to monitor.
2. Use **Crawler Execution Schedule (**how often ADOC scans your database) to set when background jobs scan files and collect metadata for observability:
    1. Select how often the crawler runs (e.g., daily)
    2. Set execution time and time zone
    3. Add multiple execution schedules if needed

3. Configure Notifications
    1. **Notify on Crawler Failure**: Select one or more channels for failure alerts.
    2. **Notify on Success**: Receive success notifications (toggle on/off)

4. Click **Submit** to save your configuration and start monitoring your Azure MSSQL data source.

Your Azure MSSQL source appears on the **Data Sources** page. ADOC will scan and collect metadata and metrics based on your schedule.

## Troubleshooting and FAQs

### Common Issues

**1. Managed Identity not recognized in Azure MSSQL**

- **Issue:** The managed identity is not successfully authenticated by Azure MSSQL.
- **Solution:** Verify that the managed identity has been assigned the correct role (such as **SQL DB Contributor**) in Azure IAM. Also, ensure that the managed identity details (Tenant ID and Client ID, if applicable) are entered correctly in ADOC’s data source configuration.

**2. Permission denied error**

- **Issue:** ADOC displays a “permission denied” error when attempting to access Azure MSSQL.
- **Solution:** Ensure that the identity (managed identity, service principal, or SQL user) has the required database permissions. At a minimum, the identity must be a member of **db_datareader** and have **VIEW DATABASE STATE** privileges. Update role assignments in Azure or grant the necessary permissions inside the database.

**3. Connectivity issues in ADOC**

- **Issue:** ADOC cannot establish a connection to Azure MSSQL when using Managed Identity.
- **Solution:** Confirm that Azure firewall and network rules allow inbound connections from ADOC. Also, ensure that your ADOC environment has outbound internet access to connect with Azure SQL endpoints.

---

### Frequently Asked Questions

**Q1: What roles are required for a managed identity to access Azure MSSQL in ADOC?**

Typically, roles like **SQL DB Contributor** or **SQL Server Contributor** are needed, depending on whether you’re assigning the role at the database or server level.

**Q2: How do I configure Azure Managed Identity in ADOC for Azure MSSQL?**

When registering Azure MSSQL in ADOC, select **Managed Identity Authentication** and test the connection.

**Q3: Can I use the same managed identity for multiple Azure services in ADOC?**

Yes. A user-assigned managed identity can be shared across multiple Azure services and resources, including Azure MSSQL.

**Q4: What should I do if my managed identity is not recognized by Azure MSSQL?**

Ensure that the managed identity is assigned correctly in the Azure portal, and that all necessary permissions are granted on the Azure MSSQL database. Double-check that the identity details in ADOC match the identity in Azure.

**Q5: Where can I find logs for troubleshooting Azure Managed Identity issues in ADOC?**

- Review ADOC errors related to the Azure MSSQL connection when testing the connection.
- In Azure, use the **Auditing and Diagnostic Logs** features to track managed identity login attempts and access issues.

## What’s Next

- **Create and apply policies:** Define **data quality**, **reconciliation**, **schema drift**, **data drift**, and **anomaly detection** policies. _(Dashboards remain empty until policies are applied.)_
- **Monitor dashboards:** Review applied policy results and key health indicators for Azure MSSQL.
- **Set up alerts:** Notify teams on policy failures, drift, or anomalies.