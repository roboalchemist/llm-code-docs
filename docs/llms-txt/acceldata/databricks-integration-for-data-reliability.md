# Source: https://docs.acceldata.io/documentation/databricks-integration-for-data-reliability.md

# Databricks Reliability

Acceldata Data Observability Cloud (ADOC) allows you to integrate with Databricks to ensure data reliability by monitoring dataset freshness, schema drift, and anomalies. This guide provides step-by-step instructions to connect your Databricks workspace (on AWS or Azure) to ADOC for Data Reliability, enabling you to maintain high-quality data for analytics and pipelines.

## Prerequisites

Ensure the following requirements are met before you connect Databricks as a data source.

### Common Prerequisites

- **Access to ADOC Platform**: Ensure you have login credentials for ADOC.
- **Databricks Workspace**: A running Databricks workspace on AWS or Azure.
- **Databricks Workspace ID**: Find in the workspace properties page (e.g., 1234567890).
- **Databricks Warehouse ID**: Obtain from the SQL Warehouse URL (e.g., your-warehouse-id from **https://&lt;instance&gt;/sql/1.0/warehouses/your-warehouse-id**).
- **Personal Access Token**: A secure key for Databricks API access.

### AWS-Specific Prerequisites

1. **Create a Databricks Personal Access Token**
    1. In your Databricks workspace, navigate to **User avatar &gt; User Settings &gt; Access Tokens**.
    2. Click **Generate New Token**, assign a nickname (e.g., “ADOC-Token”), and set an expiration date (e.g., 90 days).
    3. Copy the token (displayed only once) and store it securely.

2. **(Optional) Use AWS Secrets Manager**
    1. Store the **Personal Access Token** in AWS Secrets Manager.
    2. Reference the secret by Amazon Resource Name (ARN) in ADOC for enhanced security.

### Azure-Specific Prerequisites

1. **Create an Azure Service Principal**
    1. In Azure Portal, navigate to **Azure Active Directory &gt; App Registrations &gt; New Registration**.
    2. Name the app (e.g., “ADOC-Databricks-SP”) and click **Register**.
    3. Copy the **Application (Client) ID**, **Directory (Tenant) ID**, and create a **Client Secret** (under **Certificates & secrets**).
    4. Save these values securely.

2. **Create and Assign a Custom Role**
    1. In Azure Portal, navigate to **Subscription** or **Databricks Resource Group &gt; Access Control (IAM)**.
    2. Click **Add &gt; Add custom role** and define permissions:

```json
{
  "permissions": [
    {
      "actions": [
        "Microsoft.Databricks/workspaces/*/read",
        "Microsoft.Databricks/workspaces/clusters/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ]
}
```



c. Assign the role to your Service Principal.

3. **Add Service Principal to Databricks Workspace:** In Databricks, navigate to **Admin Settings &gt; Users or Groups**, add the Service Principal using its Client ID, and assign roles (e.g., Contributor).
4. **Grant Workspace Admin Access:** In the Databricks user list, locate the Service Principal and enable the **Workspace Admin** toggle for deep monitoring.
5. **Gather Workspace Details**: Collect your Databricks **workspace URL** (e.g., [https://adb-xxxxxx.azuredatabricks.net](https://adb-xxxxxx.azuredatabricks.net)) and **workspace ID**.

### Prerequisite Comparison Table

| Requirement | AWS | Azure | 
| ---- | ---- | ---- | 
| Identity / Auth | Personal Access Token | Service Principal + Personal Access Token | 
| Key Permissions | Workspace / API Read | Custom RBAC Role, Admin Workspace Acess | 
| Secret Management | AWS Secret Manager (optional) | Azure Key Vault (optional) | 


---

## Add Databricks as a Data Source

Follow these steps to connect your Databricks workspace to ADOC for Data Reliability. Steps are identical for AWS and Azure unless specified.

### Step 1: Start Setup

1. In ADOC, select **Register** from the left menu.
2. Click **Add Data Source** and choose **Databricks**.
3. On the **Data Source Details** page:
    1. Enter a **name** (e.g., “Prod-Databricks-Reliability”).
    2. (Optional) Add a description (e.g., “Data reliability for analytics tables”).
    3. Enable the **Data Reliability** toggle.
    4. Select your data plane (e.g., Spark) from the dropdown.

4. Click **Next**.

### Step 2: Add Connection Details

Provide the following details. Refer to [Databricks Documentation](https://docs.databricks.com) for help finding IDs or URLs.

- **Cloud Provider**: Select AWS or Azure.
- **Workspace Name**: Enter a descriptive name (e.g., “Analytics-Workspace”).
- **Token**: Provide the Personal Access Token.
- **Token Expiry Time**: Set the expiration date (e.g., 90 days).
- **Use Service Principal** (optional, Azure):
- Enter **Client ID**, **Client Secret**, and **Tenant ID**.
- **JDBC URL**: Provide the connection string (e.g., jdbc:spark://adb-1234567890.azuredatabricks.net:443/default;transportMode=http;ssl=1;httpPath=sql/protocolv1/o/0/your-warehouse-id).
- **Data Plane Engine**: Select Spark (***Note**: Pushdown is not supported with Service Principal*).

### Step 3: Validate and Save Connection

1. Click **Test Connection.** If successful, you’ll see “Connected.” If it fails, check:
    - Invalid or expired Personal Access Token.
    - Incorrect Workspace URL or ID.
    - Wrong JDBC URL or SQL Warehouse issues.
    - Insufficient permissions for token or Service Principal.

2. Click **Next**.

### Step 4: Configure Data Reliability

Configure settings for ADOC to monitor data reliability:

- **Unity Catalog Enabled**: Toggle ON if using Unity Catalog to monitor metadata and assets.
- **JDBC Records Fetch Size**: Set records per query (e.g., 1000) based on workspace size for optimal performance.
- **Enable Crawler Execution Schedule**: Toggle ON and set a schedule (e.g., daily at 2 AM UTC) for automated reliability checks.
- Click **Submit** to save. A Databricks card will appear on the ADOC **Data Sources** page, showing connection and crawler status.

---

## What’s Next

With Data Reliability enabled, you can:

- **Monitor Data Quality**: Use ADOC to track dataset freshness, schema drift, and anomalies in your cloud-based platform.
- **Set Policies**: Define rules (e.g., missing-value checks, duplicates) for Unity Catalog or standard tables.
- **Visualize Health**: Use ADOC dashboards to view table and pipeline health trends.

---

## Glossary

- **DBU (Databricks Unit)**: A unit measuring compute usage for Databricks billing.
- **Unity Catalog**: Databricks’ governance solution for metadata and assets.
- **JDBC URL**: A connection string for Databricks SQL Warehouses.
- **Personal Access Token**: A secure key for Databricks API access.
- **Torch**: ADOC’s tool for data reliability, crawling Delta Lake and other sources.

---

## Additional References

1. [Databricks Documentation](https://docs.databricks.com/aws/en)
2. [Azure Custom Roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)
3. [Create or update Azure Custom Roles using the Azure Portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles-portal?source=recommendations)
4. [AWS IAM Setup Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
5. [Azure Service Principal Guide](https://docs.microsoft.com/azure/active-directory)