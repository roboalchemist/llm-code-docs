# Source: https://docs.acceldata.io/documentation/snowflake-reliability.md

# Snowflake Reliability

Connecting Snowflake to ADOC helps you monitor your data infrastructure for performance and reliability. Once connected, ADOC can:

- Monitor the health of your Snowflake schemas and datasets
- Track data quality and freshness across tables
- Generate alerts and diagnostics when reliability issues arise

## Prerequisites

Before connecting Snowflake to ADOC, you need to set up Snowflake so ADOC can securely monitor your data for quality, performance, and cost. This setup ensures the right users and roles exist, and that they have the permissions needed to access only what’s necessary.

Note All steps in this section must be executed from the **Snowflake Web UI** or a **SQL editor (like SnowSQL or a Snowflake IDE)** using an account with **ACCOUNTADMIN** privileges.

### Users and Roles Overview

Before we start, here’s a quick overview of the users and roles that will be created:

| **Role/User** | **Purpose** | 
| ---- | ---- | 
| `AD_DATA_RELIABILITY_ROLE` | Read-only role for monitoring your business data | 
| `adoc_user` | Authenticates into ADOC to analyze schema, freshness, and data quality | 


ADOC needs access to your actual data — not to change it, but to analyze it for things like freshness, schema drift, and data quality. This part sets up a read-only role and user that ADOC uses to scan your data safely.

**Who Should Perform These Steps?**

- Snowflake Admins: Set up users, roles, and grants  
- Cloud/Network Admins: Configure PrivateLink and DNS  
- Data Owners: Choose databases and tables to monitor  
- ADOC Users: Complete setup in the ADOC UI

```sql
CREATE ROLE IF NOT EXISTS AD_DATA_RELIABILITY_ROLE COMMENT = 'Used by ADOC to monitor data health and quality.';
GRANT USAGE ON WAREHOUSE <your_warehouse_name> TO ROLE AD_DATA_RELIABILITY_ROLE;
GRANT USAGE ON DATABASE <your_database> TO ROLE AD_DATA_RELIABILITY_ROLE;
GRANT USAGE ON SCHEMA <your_database>.<your_schema> TO ROLE AD_DATA_RELIABILITY_ROLE;
GRANT SELECT ON ALL TABLES IN SCHEMA <your_database>.<your_schema> TO ROLE AD_DATA_RELIABILITY_ROLE;
CREATE USER IF NOT EXISTS adoc_user DEFAULT_ROLE = AD_DATA_RELIABILITY_ROLE;
ALTER USER adoc_user SET PASSWORD = '<your_secure_password>';
GRANT ROLE AD_DATA_RELIABILITY_ROLE TO USER adoc_user;
```



1. ### Create a Custom Role

This role limits access to just what's needed for monitoring. Using a separate role improves security and auditing.

2. ### Allow Warehouse Usage

ADOC runs lightweight queries to check data freshness, row counts, and run profiling jobs. It needs a Snowflake warehouse to do this.

3. ### Grant Access to Your Data

ADOC does not write to your tables — it only needs **SELECT** access to:

- Profile column statistics
- Validate data quality rules
- Detect schema drift
- Repeat these grants for each database and schema you want ADOC to observe.

Note ADOC uses read-only access and only queries metadata or data you explicitly grant. It never modifies or deletes data and adheres to Snowflake’s least-privilege access model.

4. ### Create and Configure a Monitoring User

This user is used by ADOC to authenticate and run observability jobs. The user only inherits the read-only permissions from the role you just created.

## Add Snowflake as a Data Source

### Step 1: Start Setup

1. Click **Register** from the left main menu.
2. Click **Add Data Source -&gt; Snowflake** from the list of data sources.
3. On the **Basic Details** page:
    1. Enter a name for this data source.
    2. (Optional) Add a description.
    3. Choose your Data Plane or click **Setup Data Plane** to create one.
    4. You must enable at least one or both of the following to continue:
        - Compute Observability
        - Data Reliability Monitoring

4. Click **Next**.

### Step 2: Add Connection Details

When adding a Snowflake connection, select the appropriate **Authorization Type** from the dropdown menu.

The following authentication methods are supported:

- Username and Password
- [Snowflake Integration Using OAuth](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/snowflake-integration-using-oauth)
- [Authenticating Using External OAuth (Microsoft Entra ID)](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/authenticating-using-external-oauth--microsoft-entra-id-)
- [Key Pair Authentication](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/snowflake-reliability#step-2-add-connection-details)

#### Key Pair Authentication

Key Pair authentication allows you to connect to Snowflake using an **RSA public/private key pair** instead of a password.

This method is recommended by Snowflake as a **secure alternative to username/password authentication**.

> - Key Pair authentication is supported with **data plane versions ADOC 26.3.0 and later**. Backward compatibility is **not supported** for this authentication method.> - External OAuth authentication can be used with **older data plane versions**.> - Existing **username/password connections continue to work** unless restricted by Snowflake configuration.> - Key Pair authentication supports **Spark**, **Pushdown**, **DPVP**, and **VTree** engines.

**Prerequisites**

- Generate an **RSA public and private key pair**.
- Register the **public key with the Snowflake user**.

- Keep the **private key securely**.
- Snowflake recommends using an **encrypted private key protected with a passphrase**.

**Configure Key Pair Authentication**

1. Select **Authorization Type → Key Pair**.
2. Enter the **Snowflake URL**.
3. Enter the **Username** **associated with the registered public key.**
4. Provide the private key using one of the following methods:

**Option 1: Upload Private Key File**

- Upload the private key file directly.
- If using an **encrypted private key**, enter the **passphrase** used to encrypt the key.

**Option 2: Use Secret Manager**

- Enable **Use Secret Manager**.
- Select the configured secret manager (e.g., **AWS Secret Manager**).
- Provide:

    - Secret Key Name for Private Key: Secret containing the Snowflake private key
    - Secret Key Name for Passphrase (if encrypted): Secret containing the key passphrase (if the key is encrypted)

**Storing the Private Key in Secret Manager**

When using a secret manager, the **private key must be stored as a Base64-encoded string** instead of uploading the `.p8` file directly. 

To convert the private key file to Base64 format:

```bash
base64 -i rsa_private_key.p8 > key_base64.txt
```



Display the encoded value:

```bash
cat key_base64.txt
```



Copy the output of the above command and store it as the **secret value** in the configured secret manager.

ADOC reads this Base64 value during authentication and reconstructs the private key to establish the Snowflake connection. 

After providing the private key:

5. Enter the Snowflake **Role**.
6. Select the **d ata plane Engine**.
7. Click **Test Connection**.

Note ADOC supports both:

- **Encrypted private keys** (recommended)
- **Unencrypted private keys**

If using an encrypted key, a **passphrase must be provided**. 

If using an unencrypted key, the passphrase field is **not required**.

**Key Rotation**

To rotate the key:

1. Generate a **new public/private key pair**.
2. Update the **public key in Snowflake**.
3. Edit the **data source in ADOC**.
4. Upload the **new private key** or update the **secret manager reference**.

---

#### External OAuth Authentication (Microsoft Entra ID)

ADOC supports connecting to Snowflake using **External OAuth with Microsoft Entra ID**. This authentication method uses the **OAuth 2.0 Authorization Code flow**, where Microsoft Entra ID acts as the authorization server and Snowflake validates the OAuth access token to establish a session.

Configuring this authentication method requires setup in **Microsoft Entra ID** and **Snowflake** before authentication can be completed in ADOC.

For detailed configuration instructions, see [Authenticating Using External OAuth (Microsoft Entra ID)](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/authenticating-using-external-oauth--microsoft-entra-id-).

In this configuration:

- **Microsoft Entra ID** acts as the Authorization Server
- **Snowflake** acts as the Resource Server
- **ADOC** acts as the OAuth Client using the Authorization Code Grant flow

#### Prerequisites

Before configuring authentication in ADOC, ensure that:

- Microsoft Entra ID is configured as the OAuth provider
- The required Microsoft Entra ID application registrations are created
- Snowflake is configured with an External OAuth security integration
- The Snowflake user has a default role configured

#### Configuring using External OAuth in ADOC

1. Select **Authorization Type → External OAuth (Microsoft Entra ID)**
2. Enter the following details:

| Field | Description | 
| ---- | ---- | 
| Snowflake URL | URL of your Snowflake account | 
| Authorization Endpoint | OAuth authorization endpoint | 
| Token Endpoint | OAuth token endpoint | 
| Client ID | Azure Application (client) ID | 
| Client Secret | Client secret generated in Azure | 
| Entra App ID | Azure application ID registered for Snowflake | 
| OAuth Login Name | Snowflake login name associated with the OAuth user | 
| Refresh Token Validity | Defines refresh token lifetime in seconds | 


3. Select the data plane engine.
4. Click **Authenticate**.

When you click **Authenticate**:

1. ADOC redirects the browser to Microsoft Entra ID.
2. You must log in using your Entra credentials.
3. Microsoft Entra ID returns an **authorization code**.
4. ADOC exchanges the code for:
    - Access Token
    - Refresh Token

The access token is used to establish a session with Snowflake.

When the access token expires, ADOC automatically uses the **refresh token** to obtain a new one.

After successful authentication, the remaining Snowflake setup steps (warehouse, database, crawling) remain unchanged.

> - Supported from **ADOC 26.3.0** and later.> - Backward compatible with existing OAuth-based configurations.> - Default Snowflake role is used during connection.> - Additional OAuth providers may be supported in future releases.

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


Once you have successfully created your Snowflake data source, proceed to crawl it. Crawling a Snowflake data source now includes materialized views. The crawl process now also captures materialized views. These appear as separate nodes in the lineage graph, enabling you to clearly visualize how data flows across base tables, standard views, and materialized views. This enhancement offers a more comprehensive and accurate view of data movement and transformations within your Snowflake environment.

## What’s Next

After you’ve connected Snowflake:

- Visit the Reliability tab to see data quality scores and crawler stats
- Schedule profiling jobs and schema checks
- Get real-time alerts for query spikes, delays, or data freshness issues
- Explore Pipelines to analyze data movement and transformation patterns