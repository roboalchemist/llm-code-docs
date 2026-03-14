# Source: https://docs.acceldata.io/documentation/troubleshooting-data-source-connection---crawling.md

# Troubleshooting Data Source Connection & Crawling

When onboarding a new data source in Acceldata, you may encounter connection or crawler issues.
 This guide explains common failure scenarios, how to validate your setup, and what steps you can take before contacting Acceldata Support.

It is intended for data engineers and administrators responsible for configuring and monitoring data source integrations.

Every time you add a new data source in ADOC, two key operations occur:

1. **Connection Validation:** Acceldata tests your credentials and attempts to reach the data source.
2. **Metadata Crawling:** Acceldata retrieves metadata such as schemas, tables, columns, lineage, and other catalog details.

If either step fails, the UI displays an error message. Some messages are specific, while others may be generic depending on the connector.

This guide helps you interpret these errors and identify corrective actions.

## Troubleshooting Connection Failures

Connection failures typically fall into four categories.

### A. Invalid Credentials

You may see errors such as:

- **Authentication failed**
- **Invalid username or password**
- **Access denied**

**What to Check**

- Verify the username and password.
- Ensure your credentials have metadata-level read permissions (system tables, information schema, catalog metadata).
- If using OAuth or tokens, ensure they are active and not expired.
- If using IAM roles (Snowflake, BigQuery, AWS, etc.), confirm the correct role is assigned.

### B. Incorrect Connection Parameters

These errors occur when the details in the configuration screen are incorrect, such as:

- Wrong hostname or IP
- Incorrect port
- Incorrect JDBC/connection URL
- Wrong project/database/catalog/warehouse name

**What to Check**

- Verify host, port, and region.
- Confirm the connection string format matches provider requirements (Snowflake, Databricks, BigQuery, etc.).
- Test the same endpoint using a SQL client (DBeaver, SnowSQL, BigQuery CLI, etc.).
- Confirm the region and endpoint are correct.

### C. Network Reachability Issues

The ADOC Data Plane must be able to reach your data source. Failures may occur due to:

- Firewall restrictions
- Missing IP allowlisting
- Blocked outbound (egress) traffic
- VPC/subnet routing misconfigurations
- Private endpoints without proper routing
- DNS failures
- Proxy requirements not configured

**What to Check**

- Ensure the Data Plane outbound IP is added to your database allowlist.
- Confirm the required port is open for inbound database connections.
- If using PrivateLink, or, VPC peering ensure routing is correctly configured.
- Verify DNS resolution for the database hostname.
- If your organization uses proxies, ensure proxy settings are configured properly.

### D. Platform Services Are Temporarily Unhealthy

If backend services are temporarily unavailable, you may see:

- **HTTP 403** or **HTTP 500** errors
- Errors like _Unable to process request_

**What to Check**

- Retry after a few minutes.
- Ensure your Data Plane is running and healthy.
- If the issue persists, provide the error details to Acceldata Support.

## Troubleshooting Crawling Failures

Once a connection is successful, Acceldata runs a metadata crawler to fetch catalog and lineage information.

Crawling may fail due to permission issues, resource limits, or upstream system errors.

### A. Crawler Does Not Start

Symptoms:

- Crawl does not begin
- The UI shows a generic error
- No metadata is populated

**Possible Causes**

- Invalid or insufficient metadata permissions
- Connectivity interruptions
- Temporary Data Plane issues

**What to Check**

- Retry the crawl.
- Ensure the database user has permissions to list databases, schemas, tables, and columns.
- Ensure routing and firewall paths remain open.
- Confirm the target data source is online.

### B. Crawler Started but Encountered Errors

Symptoms:

- Crawling stops midway
- Some schemas or tables are missing
- Partial metadata appears

**Possible Causes**

- Metadata permissions missing for certain schemas
- Large systems requiring higher compute
- Cloud warehouse inactive or paused
- Query timeouts
- API rate limits (BigQuery, Snowflake, Databricks, etc.)

**What to Check**

- Confirm permissions:
    - **List Databases**
    - **List Schemas**
    - **Select / Describe Tables**
    - **Access System Metadata Tables**

- Ensure the target warehouse or SQL endpoint is active (Snowflake warehouse, Databricks SQL Warehouse, etc.).
- If crawling a very large environment, consider increasing Data Plane CPU/Memory.
- Retry after temporary cloud throttling subsides.

### C. Crawler Does Not Launch (Job/Pod Not Created)

Symptoms:

- No visible crawler progress
- The UI shows repeated crawl failures
- Metadata is never collected

**Possible Causes**

- Data Plane resource exhaustion
- Database unavailability
- Compute endpoint paused or offline
- Incorrect permissions during crawl phase

**What to Check**

- Ensure the Data Plane node has available CPU/memory.
- Verify the database is reachable and responsive.
- Validate credentials again (expired tokens can pass initial checks but fail later).
- Retry after cloud resource reallocation (Databricks/Snowflake compute warm-up).

If the issue continues, capture the failure timestamp and open a support ticket.