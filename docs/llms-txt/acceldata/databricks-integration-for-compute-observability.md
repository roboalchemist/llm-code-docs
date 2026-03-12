# Source: https://docs.acceldata.io/documentation/databricks-integration-for-compute-observability.md

# Databricks Compute

Acceldata Data Observability Cloud (ADOC) integrates with Databricks to provide compute observability, monitoring cluster health, job performance, and costs. This guide provides step-by-step instructions to connect your Databricks workspace (on AWS or Azure) to ADOC for Compute Observability, enabling you to optimize resources and reduce costs.

## Prerequisites

Ensure the following requirements are met before you connect Databricks as a data source.

### Common Prerequisites

- **Access to ADOC Platform**: Ensure you have login credentials for ADOC.
- **Databricks Workspace**: A running Databricks workspace on AWS or Azure.
- **Databricks Workspace ID**: Find in the workspace properties page (e.g., 1234567890).
- **Databricks Warehouse ID**: Obtain from the SQL Warehouse URL (e.g., `your-warehouse-id from https://<instance>/sql/1.0/warehouses/your-warehouse-id`).
- **Personal Access Token**: A secure key for Databricks API access.

### AWS-Specific Prerequisites

1. **Create an IAM User for Cost Explorer**:
    1. Log in to the AWS Console and go to **IAM &gt; Users &gt; Add user**.
    2. Enable **Programmatic access**.
    3. Attach this custom policy for cost retrieval:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ce:GetCostAndUsage",
        "ce:GetCostCategories",
        "ce:GetTags"
      ],
      "Resource": "*"
    }
  ]
}
```



- Save the Access Key and Secret Keys securely.

2. **Create a Databricks Personal Access Token**:
    1. In your Databricks workspace, go to **User avatar &gt; User Settings &gt; Access Tokens**.
    2. Click **Generate New Token**, assign a nickname (e.g., “ADOC-Token”), and set an expiration date (e.g., 90 days).
    3. Copy the token (displayed only once) and store it securely.

3. **Set Up Global Init Script for Automated Agent Deployment**:
    - Use Acceldata’s script to deploy the Pulse agent:

```none
#!/bin/bash
curl -o /tmp/acceldata-agent.sh https://agent.acceldata.io/install
bash /tmp/acceldata-agent.sh --install-dir /opt/acceldata --api-key <your-adoc-api-key>
```



- In Databricks, go to **Admin Console &gt; Clusters &gt; Init Scripts**, paste or upload the script, and apply to relevant clusters.
- Restart clusters to activate the agent (automated thereafter). 

Note Replace`<your-adoc-api-key>`with your ADOC-provided API key (contact Acceldata support)

4. **Provide DBU Pricing**:
    - Check your Databricks billing console for DBU rates (e.g., $0.20/DBU for Jobs Compute).
    - Note these for accurate cost reporting.

5. **(Optional) Use AWS Secrets Manager**:
    1. Store credentials (e.g., Access Key, Token) in AWS Secrets Manager.
    2. Reference secrets by ARN in ADOC.

### Azure-Specific Prerequisites

1. **Create an Azure Service Principal**:
    1. In Azure Portal, go to **Azure Active Directory &gt; App Registrations &gt; New Registration**.
    2. Name the app (e.g., “ADOC-Databricks-SP”) and click **Register**.
    3. Copy the **Application (Client) ID**, **Directory (Tenant) ID**, and create a **Client Secret**.
    4. Save these values securely.

2. **Create and Assign a Custom Role**:
    1. In Azure Portal, go to **Subscription** or **Databricks Resource Group &gt; Access Control (IAM)**.
    2. Click **Add** &gt; Add custom role and define permissions:

```json
{
  "permissions": [
    {
      "actions": [
        "Microsoft.Databricks/workspaces/*/read",
        "Microsoft.Databricks/workspaces/clusters/read",
        "Microsoft.CostManagement/exports/read",
        "Microsoft.CostManagement/query/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ]
}
```



- Assign the role to the Service Principal.

3. **Add Service Principal to Databricks Workspace**:
    - In Databricks, go to **Admin Settings &gt; Users or Groups**, add the Service Principal using its Client ID, and assign roles (e.g., Contributor).

4. **Grant Workspace Admin Access**:
    - In the Databricks user list, locate the Service Principal and enable the **Workspace Admin** toggle.

5. **Gather Workspace Details**:
    - Collect your Databricks **workspace URL** (e.g., https://adb-xxxxxx.azuredatabricks.net) and **workspace ID**.

### Prerequisite Comparison Table

| Requirement | AWS | Azure | 
| ---- | ---- | ---- | 
| **Identity/Auth** | IAM User + Personal Access Token | Service Principal + Personal Access Token | 
| **Key Permissions** | Cost Explorer, Workspace/API Read | Custom RBAC Role, Admin Workspace Access, Cost Management | 
| **Secret Management** | AWS Secrets Manager (optional) | Azure Key Vault (optional) | 
| **Advanced Observability** | Global Init Script, DBU Configuration | Admin Role, Custom Role | 
| **Cost Retrieval** | API or System Table method | API or System Table method | 


---

## Add Databricks as a Data Source

Follow these steps to connect your Databricks workspace to ADOC for Compute Observability. Steps are identical for AWS and Azure unless specified.

### Step 1: Start Setup

1. In ADOC, select **Register** from the left menu.
2. Click **Add Data Source** and choose **Databricks**.
3. On the **Data Source Details** page:
    1. Enter a **name** (e.g., “Prod-Databricks-Compute”).
    2. (Optional) Add a description (e.g., “Compute monitoring for analytics clusters”).
    3. Enable the **Compute Observability** toggle.

4. Click **Next**.

### Step 2: Add Connection Details

Provide the following details. Refer to the [Databricks Documentation](https://docs.databricks.com/aws/en) for help.

- **Cloud Provider**: Select AWS or Azure.
- **Cloud Region**: Enter your region (e.g., us-west-2 for AWS, eastus for Azure).
- **Workspace Name**: Enter a descriptive name (e.g., “Analytics-Workspace”).
- **Databricks URL**: Provide the full URL (e.g., `[https://adb-1234567890.cloud.databrickssmile](https://adb-1234567890.cloud.databrickssmile) emoticon).
- **Warehouse ID**: Find in the SQL Warehouse URL (e.g., your-warehouse-id).
- **Workspace ID**: Obtain from workspace properties (e.g., 1234567890).
- **Token**: Enter the Personal Access Token.
- **Auto-Renew Token**: Enable to avoid manual updates (if supported).
- **Advanced Options (AWS)**:
    - Enable **AWS Actual Cost** and select **API** method.
    - Enter **AWS Access Key ID** and **Secret Access Key**.

- **Advanced Options (Azure)**:
    - (Optional) Use **Service Principal** with **Client ID**, **Client Secret**, and **Tenant ID**.
    - Enable **Azure Actual Cost** for cost retrieval.

### Step 3: Validate and Save Connection

1. Click **Test Connection.** If successful, you’ll see “Connected.” If it fails, check:
    - Invalid or expired Personal Access Token.
    - Incorrect Workspace URL or ID.
    - Insufficient permissions for token or Service Principal.

2. Click **Next**.

### Step 4: Configure Compute Observability

Configure settings for Pulse to monitor compute resources:

- **Enable Global Init Script**:
    - Toggle ON to apply the Pulse agent script to all clusters for monitoring CPU, memory, and Spark metrics.
    - Paste the script from the prerequisites (replace &lt;your-adoc-api-key&gt;).

- **Compute Cost Parameters**:
    - Enter per-DBU costs (e.g.):
        - Jobs Compute: $0.20/DBU
        - Jobs Photon Compute: $0.25/DBU
        - Delta Live Tables: $0.30/DBU
        - All-Purpose Photon Compute: $0.22/DBU
        - All-Purpose Cluster: $0.18/DBU

    - Enter **Cloud Provider Cost Discount** (e.g., 10%) if applicable.
    - Enable **Tag-Based Chargebacks** to allocate costs by project or team.

- **Enable Private S3 Bucket** (AWS only):
    - Toggle ON and configure for log/data storage.

- Click **Submit** to save. A Databricks card will appear on the ADOC **Data Sources** page, showing connection status.

---

## What’s Next

With Compute Observability enabled, you can:

- **Monitor Clusters with ADOC**: View cluster health, resource utilization, and job statuses (e.g., running, failed).
- **Analyze Performance**: Use JVM flame graphs to identify bottlenecks.
- **Optimize Costs**: Set budget alerts and use tag-based chargebacks for cost allocation.
- **Use Query Studio**: View real-time/historical queries, abort long-running queries, and explore heatmaps.
- **Check Guardrails**: Visualize terminated clusters and usage limits.

---

## Known Limitations

| Limitation | Details | Recommendation | 
| ---- | ---- | ---- | 
| System Time Adjustment | Cost data requires UTC system time for Azure Portal alignment. | Set system time to UTC. | 
| Job Studio Page Mismatch | Filter facet counts may differ due to update frequencies. | Expect minor discrepancies in job counts. | 
| Cloud Vendor Cost Delay | Azure Portal cost calculations may take 24-48 hours. | Allow up to 48 hours for accurate costs. | 
| Initial API Data Retrieval | First-time API cost data takes 24 hours for 30-day history. | Plan for delayed historical data. | 
| All-Purpose Cluster Cost Display | Costs shown daily; ≤24-hour ranges may not display data. | Select date ranges &gt;24 hours. | 


---

## Troubleshooting and FAQs

#### Common Issues:

- **“Connection Failed”**:
    - Verify token validity and permissions.
    - Check Workspace URL/ID accuracy.
    - Ensure network access to Databricks APIs.

- **Global Init Script Not Running**:
    - Confirm script is applied and clusters are restarted.

- **Cost Data Missing**:
    - Verify DBU pricing and Cost Explorer (AWS) or API access (Azure).

#### FAQs

1. **Do I need admin access?**

Yes, for init script or Service Principal setup. Non-admins should coordinate with their Databricks admin.

2. **How do I find my DBU pricing?**

Check your Databricks billing console or consult your account manager.

---

## Glossary

- **DBU (Databricks Unit)**: A unit measuring compute usage for Databricks billing.
- **Personal Access Token**: A secure key for Databricks API access.

---

## Additional References

1. [Databricks Documentation](https://docs.databricks.com/aws/en)
2. [Azure Custom Roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)
3. [Create or update Azure Custom Roles using the Azure Portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles-portal?source=recommendations)
4. [AWS IAM Setup Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
5. [Azure Service Principal Guide](https://docs.microsoft.com/azure/active-directory)