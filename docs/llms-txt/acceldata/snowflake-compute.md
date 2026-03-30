# Source: https://docs.acceldata.io/documentation/snowflake-compute.md

# Snowflake Compute

Connecting **Snowflake** to ADOC helps you monitor and optimize the performance and cost of your Snowflake compute resources. Once connected, ADOC can:

- Track **credit consumption** to improve cost efficiency.
- Enable automated alerts and diagnostics for query performance and compute utilization.

## Prerequisites

Before connecting Snowflake to ADOC, you need to set up Snowflake so ADOC can securely monitor your data for quality, performance, and cost. This setup ensures the right users and roles exist, and that they have the permissions needed to access only what’s necessary.

Note All steps in this section must be executed from the **Snowflake Web UI** or a **SQL editor (like SnowSQL or a Snowflake IDE)** using an account with **ACCOUNTADMIN** privileges.

### Users and Roles Overview

Before we start, here’s a quick overview of the users and roles that will be created:

| **Role/User** | **Purpose** | 
| ---- | ---- | 
| `AD_COMPUTE_MONITOR` | Role that grants access to monitor Snowflake credit and performance | 
| `AD_USER` | Authenticates into ADOC for compute observability and cost tracking | 


To set up your Snowflake data source for compute monitoring, you must do the following:

```sql
-- Role for compute reliability monitoring
SET acceldata_role = 'AD_COMPUTE_MONITOR';

-- Warehouse for compute tasks
SET acceldata_warehouse = 'AD_COMPUTE_WH';

-- User for compute reliability tasks
SET acceldata_user = 'AD_USER';

-- Password for the user (replace '<password>' with a strong password)
SET acceldata_password = '<your_secure_password>';

-- Database for monitoring tasks
SET acceldata_database = 'AD_MONITOR_DB';

USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE WAREHOUSE IDENTIFIER($acceldata_warehouse) WAREHOUSE_SIZE = 'X-Small';
ALTER WAREHOUSE IDENTIFIER($acceldata_warehouse) SET AUTO_SUSPEND = 30;

CREATE OR REPLACE ROLE IDENTIFIER($acceldata_role);

GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE IDENTIFIER($acceldata_role);

GRANT MONITOR ON ACCOUNT TO ROLE IDENTIFIER($acceldata_role);

GRANT USAGE ON WAREHOUSE IDENTIFIER($acceldata_warehouse) TO ROLE IDENTIFIER($acceldata_role);

CREATE OR REPLACE USER IDENTIFIER($acceldata_user)
  LOGIN_NAME = $acceldata_user
  PASSWORD = $acceldata_password
  DEFAULT_WAREHOUSE = $acceldata_warehouse
  DEFAULT_ROLE = $acceldata_role
  DEFAULT_NAMESPACE = SNOWFLAKE.ACCOUNT_USAGE;
  
ALTER USER <existing_username>
  SET DEFAULT_ROLE = <your_role>,
      DEFAULT_WAREHOUSE = <your_wh>,
      DEFAULT_NAMESPACE = SNOWFLAKE.ACCOUNT_USAGE;
   
GRANT ROLE IDENTIFIER($acceldata_role) TO USER IDENTIFIER($acceldata_user);

CREATE DATABASE IF NOT EXISTS IDENTIFIER($acceldata_database);

GRANT USAGE ON DATABASE IDENTIFIER($acceldata_database) TO ROLE IDENTIFIER($acceldata_role);

USE DATABASE IDENTIFIER($acceldata_database);

GRANT MONITOR, USAGE, CREATE FILE FORMAT, CREATE STAGE
  ON SCHEMA PUBLIC
  TO ROLE IDENTIFIER($acceldata_role);
  
CREATE OR REPLACE PROCEDURE grant_privileges_to_all_warehouses(ROLE_NAME VARCHAR)
  RETURNS VARCHAR
  LANGUAGE JAVASCRIPT
  AS
  $$
  var warehouses = snowflake.createStatement({sqlText: "SHOW WAREHOUSES"}).execute();
  while (warehouses.next()) {
    var warehouse_name = warehouses.getColumnValue(1);
    snowflake.createStatement({sqlText: "GRANT MONITOR ON WAREHOUSE " + warehouse_name + " TO ROLE " + ROLE_NAME}).execute();
  }
  var resource_monitors = snowflake.createStatement({sqlText: "SHOW RESOURCE MONITORS IN ACCOUNT"}).execute();
  while (resource_monitors.next()) {
    var monitor_name = resource_monitors.getColumnValue(1);
    snowflake.createStatement({sqlText: "GRANT MONITOR ON RESOURCE MONITOR " + monitor_name + " TO ROLE " + ROLE_NAME}).execute();
  }
  return 'Granted monitor privileges';
  $$;

GRANT USAGE ON PROCEDURE grant_privileges_to_all_warehouses(VARCHAR) TO ROLE IDENTIFIER($acceldata_role);

CALL GRANT_PRIVILEGES_TO_ALL_WAREHOUSES($acceldata_role);

GRANT CREATE INTEGRATION ON ACCOUNT TO ROLE IDENTIFIER($acceldata_role);

USE ROLE ORGADMIN;
ALTER ACCOUNT my_account1 SET IS_ORG_ADMIN = TRUE;

SHOW STAGES;
GRANT OWNERSHIP ON STAGE <stage_name> TO ROLE <role_name>;

GRANT ROLE <role> TO USER <user>;
ALTER USER <user> SET DEFAULT_ROLE = <role>;
```



### 1. Define Variables

Start by defining variables for reuse across the setup steps. This makes the script portable and easier to manage or rerun later.

### 2. Create Role and Warehouse

Ensure you’re using the **ACCOUNTADMIN** role for full privileges:

1. **Create a dedicated warehouse**: This ensures low-cost, temporary compute for ADOC to run metadata queries. This warehouse is used for lightweight metadata queries by ADOC. It isolates observability compute from your production workloads, helping you manage cost and reduce risk.
2. **Create a custom monitoring role**: This role is scoped specifically to monitor performance and usage. It ensures least-privileged access and easier audit tracking.

### 3. Grant Required Priveleges

1. **Grant access to Snowflake’s Account Usage schema**: Required to access views like `QUERY_HISTORY`_,_ and __`WAREHOUSE_METERING_HISTORY`, etc.
2. **Enable monitoring of Snowflake resources**: Allows access to credit usage, performance stats, query behavior, and warehouse efficiency.
3. **Allow role to use the monitoring warehouse**

### 4. Create User for Monitoring

Create a new user that ADOC will use to query Snowflake metadata. This ensures the user automatically starts with the right role and namespace. If reusing an existing user, update defaults.

1. **Assign role to user**

### 5. Create Monitoring Database and Grant Schema Access

1. **Create the monitoring database**
2. **Grant usage on database**
3. **Switch to the new database**
4. **Grant schema-level privileges**: These permissions are needed to manage internal stages, formats, and collect metadata.

### 6. Use Store Procedure to Grant Monitro Priveleges on All Warehouses

This script ensures the monitoring role has access to all current and future warehouses and resource monitors.

1. **Create the procedure**
2. **Grant usage on the procedure**
3. **Run the procedure**

### Optional Steps

**Optional 1: Allow storage integrations**

Required if ADOC will use external stages (like S3 or Azure Blob) through secure integrations.

**Optional 2: Enable ORGADMIN Role**

Allows access to `ORGANIZATION_USAGE` schema for consolidated org-wide monitoring.

**Optional 3: Troubleshooting & FAQ**

**Stage Creation Failure**

OAuth reauthentication: If default roles/namespaces aren’t set, the user may need to re-authenticate via OAuth.

**Changing role for existing users**

## Add Snowflake as a Data Source

### Step 1: Start Setup

1. In the ADOC UI, click **Register** from the left menu.
2. Click **Add Data Source**.
3. Select **Snowflake**.
4. On the **Basic Details** page:
    1. Enter a name for this data source.
    2. (Optional) Add a description.
    3. Choose your Data Plane or click **Setup Data Plane** to create one.
    4. You must enable at least one or both of the following to continue:
        - Compute Observability
        - Data Reliability Monitoring

5. Click **Next**.

### Step 2: Add Connection Details

1. Enter the Snowflake URL (e.g., https://&lt;account&gt;.snowflakecomputing.com)
2. Provide the following Snowflake credentials:
    1. Username
    2. Password
    3. Role (e.g., `AD_COMPUTE_MONITOR`)

3. Select your Data Plane Engine:
    - Spark (for external compute)
    - Pushdown (for in-Snowflake processing)

Note Pushdown is more cost-effective, while Spark provides more control over compute.

4. (Optional) Enable OAuth: If using OAuth, toggle Enable OAuth and provide:
    1. Authorization Endpoint
    2. Token Endpoint
    3. Client ID / Client Secret
    4. (Optional) Enable PKCE

5. (Optional for Pushdown): Configure Global Storage.  If Pushdown is selected, you can optionally toggle Configure Global Storage in Snowflake and enter:
    1. Stage Name
    2. Stage File Format (e.g., PARQUET, CSV)

6. Click **Test Connection**. If the connection is successful, you'll see a “Connected” message. If not, check the credentials and try again.
7. Click **Next**.

### Step 3: Set Up Observability

If you enabled Compute Observability, fill in the Compute Observability section:

| Field | What to Enter | 
| ---- | ---- | 
| Warehouse | Select one or more Snowflake warehouses | 
| Database | Name of the monitoring database (default: AD_MONITOR_DB) | 
| Cost per Credit | Your cost per Snowflake credit (e.g., 2.5) | 
| Query Cost Type | Choose:\n\n\n\n- Acceldata Attributed Query Cost\n- Snowflake Attributed Query Cost | 
| Snowflake Fetch Past Data | Choose data range to backfill (15 days – 1 year) | 
| Polling Schedule | Set time and timezone for scheduled polling | 
| Configure External Stage (Optional) | Enable this if using Snowflake-managed external storage | 


**Why this matters:** These settings allow ADOC to compute credit usage and query-level metrics from Snowflake, giving you visibility into workload costs and efficiency.

If you enabled Data Reliability, fill in the Data Reliability section:

| **Field** | **What to Enter** | 
| ---- | ---- | 
| Warehouse | Select Snowflake warehouse(s) used for crawling | 
| Databases | Choose all applicable databases to monitor | 
| Enable Query Analysis | Turn ON to analyze how datasets are queried | 
| Enable Crawler Execution | Schedule crawlers to check data quality | 
| Timezone & Schedule | Choose when crawlers should run (daily, weekly, etc.) | 


**Why this matters:** These options allow ADOC to scan your Snowflake datasets for freshness, schema drift, null values, and other data quality issues.

Click **Submit** to complete the setup.

You’ll see a new Snowflake card on the **Data Sources** page with connection and crawler details.

---

## Optimizing Data Partitioning

To tune performance for large datasets, you can adjust Snowflake's default parallelism using this environment variable in your ADOC Data Plane configuration:

```bash
SNOWFLAKE_PARTITION_SIZE_IN_MB=10
```



| Field | Description | 
| ---- | ---- | 
| Default Snowflake Partition | 100 MB | 
| ADOC Default | 2000 MB | 
| Use Case | Lower the value to increase parallelism for large datasets | 


Note Smaller partitions = higher concurrency = faster data processing

## Setting Up PrivateLink (Optional)

You can connect Snowflake to ADOC securely over AWS PrivateLink for improved network isolation.

**Prerequisites:**

- AWS account with necessary permissions
- VPC in us-west-2
- Snowflake account ready

### Step 1: Authorize PrivateLink Access

**Why Use PrivateLink?**

AWS PrivateLink allows your Snowflake data to connect with ADOC services over a secure, private network path—without traversing the public internet. This enhances data security, reduces latency, and improves performance.

Share your AWS account ID with the Acceldata support team. Acceldata will use this ID to authorize your account for PrivateLink connectivity.

Note This is a one-time setup per AWS account.

### Step 2: Create VPC Endpoints

In the AWS Management Console:

1. Navigate to VPC.
2. In the navigation pane, choose Endpoints.
3. Select Create Endpoint.
4. Create the following two endpoints:

| Service Name | Endpoint | 
| ---- | ---- | 
| **ADOC Control Plane** | com.amazonaws.vpce.us-west-2.vpce-svc-091c001843d33bbaa | 
| **Secure Relay** | com.amazonaws.vpce.us-west-2.vpce-svc-02830f09899d40f01 | 


Note Make sure the VPC region is set to us-west-2.

### Step 3: Configure DNS Using Route 53

In Amazon Route 53:

1. Navigate to the **Hosted Zones** section for your domain.
2. Add the following A records:

| Record Name | Type | Value | 
| ---- | ---- | ---- | 
| **&lt;tenant&gt;.acceldata.app** | A | IP address of the ADOC Control Plane VPC endpoint. Replace &lt;tenant&gt; with your tenant subdomain. | 
| **dataplane.acceldata.app** | A | IP address of the Secure Relay VPC endpoint. Use the IP address assigned to each endpoint in your VPC. | 


Note These DNS records ensure your traffic is routed directly to the ADOC services via PrivateLink. You’ll need to replace the placeholder values with your actual VPC endpoint IPs.

Security Tip Use least-privileged IAM roles when creating and attaching these endpoints.

### Troubleshooting

| Issue | Possible Cause | Resolution | 
| ---- | ---- | ---- | 
| Stage creation fails | Role doesn’t have ownership privileges | Log in as ACCOUNTADMIN, check the monitoring database, run SHOW STAGES, and use GRANT OWNERSHIP to fix role access | 
| OAuth fails | User role/namespace not set | Ensure the Snowflake user does not have ACCOUNTADMIN role; re-authenticate via ADOC | 
| Connection test fails | Invalid credentials, missing grants, or wrong role | Double-check Snowflake URL, credentials, warehouse, and role permissions | 


## What’s Next

After you’ve connected Snowflake Compute in ADOC:

- Visit the **Compute tab** to view warehouse performance and query execution metrics.
- Track **credit usage trends** to identify cost-saving opportunities.
- Set up **alerts** for spikes in compute usage, query slowdowns, or unusual activity.
- Explore **usage patterns** to optimize warehouse sizing and scheduling.