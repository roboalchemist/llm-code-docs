# Source: https://docs.acceldata.io/documentation/security-and-network-compliance.md

# Security and Network Compliance


The ADOC complies with the most demanding privacy and security requirements. For more information, see the [Trust Center](https://trust.acceldata.io/).

## Highlights

- Data never leaves your environment. Acceldata Data Observability Cloud(ADOC) service only contains metadata, query logs and aggregated statistics in its cloud service. ADOC, in particular, can support a configuration in which no individual records or personally identifiable information(PII) are ever removed from your environment.
- ADOC provides read-only access via APIs and/or dedicated service accounts, as well as granular rights to datasets of your choice.
- ADOC's hybrid design enables you to run its collector on your own cloud infrastructure, eliminating the need to expose any of your data warehouses, data lakes, and BI tools to Acceldata's cloud.


![ADOC Architecture](https://uploads.developerhub.io/prod/Yoq2/jh2iw8c2tey5q78tiiobbddbcmkdppudcxdvzou9laguwdd5g0j17zz2a51455c6.png)


## Compliance

- On request, Acceldata will provide an SOC 2 Type 2 report (Security, Availability and Confidentiality criteria). This is available from December, 2022.
- Acceldata will sign NDAs as necessary.
- Acceldata does not handle personally identifiable information(PII) or protected health information(PHI).

## Security and Privacy Practices

Acceldata follows industry best practices across the board to ensure the application's security and the client's data privacy. Some of the components of our security program and system architecture are as follows:

- Acceldata will solely gather metadata, query results, logs, and metrics to diagnose data reliability and compute issues.
- Your data will be used solely to build your own reports and will not be shared with any external parties.
- Raw consumer data is never saved in the Acceldata-hosted control plane.
- The processing is carried out on secure servers provided by the Amazon Web Services. All storage systems are encrypted, and all servers are strictly monitored and audited. At all times, data is encrypted in transit.
- In cases where debugging or maintenance work is required, a minimal number of engineers will be permitted to access the data necessary for this purpose. All engineers use encrypted laptops and are required to remove data from their devices when their debugging session is complete.  No customer data is copied to engineer laptops. Laptop security policies are enforced using MDM.
- Acceldata will access your environment via a set of published static IP addresses, allowing you to secure [network-level access](https://docs.acceldata.io/data-observability-cloud/documentation/network-connectivity) to your data resources.
- A yearly penetration test is performed to assess Acceldata's posture and find vulnerabilities. The final test was performed in December 2024, and the report is accessible upon request.
- Acceldata's service is built on highly accessible and redundant cloud services, primarily on Amazon Web Services in the **US** **East-2** region.
- Strong passwords and multi-factor authentication are used to protect access to all essential systems and production environments. SSO is used for centralized access control whenever possible. Access is reviewed prior to being granted and then periodically thereafter.

## Information ADOC Collects

ADOC collects some of your information for data processing and other operations. This section details out the data collected by various capabilities in ADOC. For more information, see the [Trust Center](https://trust.acceldata.io).

### Information Collected by Data Reliability

The following data is collected by Data Reliability capability in ADOC.


| **Information** | **Details** | **Purpose** | **Stored on** | 
| ---- | ---- | ---- | ---- | 
| Metadata | Names of tables, fields, field types, names and attributes of BI reports/dashboards and other such metadata. | Build a catalog of warehouse, lake and BI objects along with schema information. | Cloud service | 
| Metrics | Row counts, byte counts, last modification date, memory consumption, and other similar table-level metrics. | Track freshness, volume and other health metrics. | Cloud service | 
| Query Logs | History of queries, as well as metadata about them (timestamp, user performing the query, errors if any). | Track lineage, usage analytics and query history to help with troubleshooting and prevention use cases. | Cloud service | 
| Aggregated, anonymized statistics | Aggregated statistical measures of the data in selected tables, based on opt-in. Statistics may include null rates, distinct values, row counts, percentiles, and other similar metrics. | Track data health and corruption using ML-based anomaly detection as well as customer-provided rules. | Cloud service | 
| Troubleshooting data | A small sample of individual values or data records from the customer environment that are associated with a data reliability incident detected by Acceldata. | Help users quickly identify the nature of data issues and their root cause. | Data collector | 



### Information Collected by Compute

The following data is collected by Compute capability.


#### Snowflake


| **Information** | **Details** | **Purpose** | **Stored On** | 
| ---- | ---- | ---- | ---- | 
| Metadata | Warehouse names, tables names, databases names, Usage and contract metadata, login details, users details. | To provide overview of usage and contract. | Cloud service | 
| Metrics | Query execution details like execution time, warehouse, user etc. | To provide query, warehouse performance metrics. | Cloud service | 



ADOC collects the Snowflake metadata from Snowflake's [ACCOUNT_USAGE](https://docs.snowflake.com/en/sql-reference/account-usage.html) and [ORGANIZATION USAGE](https://docs.snowflake.com/en/sql-reference/organization-usage.html)  schemas. These schemas are part of the [Snowflake](https://docs.snowflake.com/en/sql-reference/snowflake-db.html) database. ADOC accesses the metadata tables under these schemas. ADOC provides you a script which you can modify to grant ADOC the access to these metadata tables. You can access the script from this [documentation](https://docs.acceldata.io/data-observability-cloud/documentation/snowflake#access-credentials-management-script).


#### Databricks


| **Information** | **Details** | **Purpose** | **Stored On** | 
| ---- | ---- | ---- | ---- | 
| Metadata | Databricks Cluster details, Job Details, Notebook details, SQL jobs details. Job metadata like execution time, number of drivers, executors. | Build Databricks workspace overview, Jobs overview and calculate vendor and Databricks cost usage. | Cloud service | 
| Metrics | Every Databricks job/cluster metrics like CPU, Memory, I/O, Network Usage. | Track the job execution and calculate usage statistics. | Cloud service | 
| Job Logs | Databricks job execution logs from executor and driver. | To provide detail log analysis for Databricks job | Cloud service | 


Reference
Click [here](https://pdfhost.io/edit?doc=97965d83-03fe-4a08-a575-9b3978e96702) to download





![](https://uploads.developerhub.io/prod/Yoq2/vnx44sk6fo19mq55hsy2j9l0u341h8uea3l6lkbjclfdy15bfaxfmhtqxivnyrzc.png)


