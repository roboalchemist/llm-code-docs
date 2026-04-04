# Source: https://docs.acceldata.io/documentation/good-bad-record-support-using-pushdown-engine.md

# Good/Bad Record Support Using Pushdown Engine

Starting from **ADOC v4.9.0**, Databricks data sources now support publishing _Good_ and _Bad_ records using the **Pushdown engine**. This enhancement aligns Databricks capabilities with Snowflake, allowing users to classify and export records based on Data Quality (DQ) policy outcomes to external storage locations such as **S3**, **DBFS**, or **ADLS**, in **Parquet** format.

## Prerequisites

Before configuring the Databricks data source in ADOC, ensure that:

1. **IAM Roles and External Storage Access**
    - The **Databricks workspace** must be configured with the appropriate **IAM roles** to access external storage (S3, ADLS, or DBFS).
    - These IAM roles must grant **read/write** permissions to the external bucket or container used for publishing Good/Bad records.
    - Refer to the detailed guide: [Configuring IAM Roles for Databricks Pushdown Integration](https://docs.google.com/document/u/0/d/1-8CxRq9B7ScL2MnRbbZeA17mnI6vljkJTPlY-eMV6ss/edit)

2. **External Storage Readiness**
    - The external storage location (e.g., S3 bucket or ADLS container) must exist and be reachable from the Databricks cluster.
    - Ensure network and firewall configurations allow outbound access from Databricks to the storage endpoint.

3. **Cluster and Engine Compatibility**
    - Pushdown engine must be enabled for the Databricks data source.
    - Use a compatible SQL Warehouse or All-Purpose Cluster for policy execution.

### Configuration Steps

Once IAM roles and storage access are in place, you can enable Good/Bad record publishing in the ADOC platform:

1. Navigate to Register &gt; Data Sources &gt; Add Data Source.
2. Select Databricks or Edit an existing Databricks data source in the Data Source page.
3. In the **Connection Details** page, select Pushdown as the Data Plane Engine and enable **Configure Global Storage with Databricks**.
4. Provide:
    1. **Base Path:** External storage path (e.g., `s3://my-good-bad-bucket/exports/warehouse/`).
    2. **File Format:** Currently supports only **Parquet**.

5. Click **Test Connection** to validate access.

During [Data Quality Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-quality-policy) creation:

- Enable **Good/Bad Records** in the **Advanced Execution Settings** section.
- When the policy runs, ADOC will automatically publish the Good and Bad record sets to the configured external storage.

### Supported External Storage

| Storage Type | Supported | Notes | 
| ---- | ---- | ---- | 
| **S3** | ✅ Fully tested | Recommended for AWS deployments | 
| **ADLS** | ⚙️ Supported (not fully validated) | Use for Azure Databricks | 
| **DBFS** | ✅ Supported | For internal or temporary storage | 


### Limitations

- Only **Parquet** format is supported in this release.
- **Good/Bad data** must remain available in the configured location; ADOC does not retain copies.
- Lifecycle management (e.g., TTL) must be handled by the customer.