# Source: https://docs.acceldata.io/documentation/azure-data-lake-gen2.md

# Microsoft Azure Data Lake Gen2

**Azure Data Lake Storage Gen2 (ADLS Gen2)** is Microsoft’s scalable, secure data lake platform for storing both structured and unstructured data. It supports big data analytics, machine learning, backups, and more.

Integrating ADLS Gen2 with the **Acceldata Observability Cloud (ADOC)** platform gives you full visibility into your lake’s data health, structure, and quality. This enables early detection of issues, ensures data reliability, and supports trusted analytics and business decisions.

## Prerequisites

Ensure the following requirements are met before you connect ADLS Gen2 as a data source:

- A valid Azure subscription with access to ADLS Gen2.
- Your **Storage Account Name** and **Access Key**, or use **Azure Managed Identity** credentials.
- An existing or new **Data Plane** configured in ADOC.
- Network access permissions allowing ADOC to reach your ADLS endpoint.

## Adding ADLS as a Data Source

### Step 1: Start Setup

1. Click **Register** from the left main menu.
2. Click **Add Data Source** -&gt; **Azure Data Lake** from the list of data sources.
3. Select a name for this data source (optional: add a description).
4. On the **Data Source Details** page:
    1. Enter a name for the data source.
    2. Add a short description (optional).

5. Ensure the **Data Reliability** toggle is enabled and select your **data plane** from the dropdown.
6. Select **Next**.

### Step 2: Add Connection Details

You can connect ADOC to your Azure Data Lake Storage Gen2 (ADLS Gen2) environment using one of three authentication methods:

1. **Storage Account Name + Access Key**
    1. Enter your **Azure Storage Account Name**.
    2. Enter the **Access Key** associated with that account.
    3. Click **Test Connection** to confirm access.

2. **Storage Account Name + Managed Identity**
    1. Enter your **Azure Storage Account Name**.
    2. Enable **Use Managed Identities**. For more information, see [Creating a Managed Identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/qs-configure-cli-windows-vm).
    3. Ensure the managed identity has the **Storage Blob Data Contributor** role for the account.
    4. Click **Test Connection** to verify.

3. **Storage Account Name + Service Principal**
    1. Enter your **Azure Storage Account Name**.
    2. Enable **Use Service Principal** and provide the following: **Service Principal Client ID, Service Principal Client Secret,** and **Azure Tenant ID**
    3. Click **Test Connection** to validate access.

> If the test fails, check that all credentials are correct and the identity has the necessary permissions in Azure.

### Step 3: Setup Observability

1. Enter values for the required fields:
    1. Asset Name:
        1. Path Expression: Define which paths to monitor in ADLS. Use Azure’s Azure Blob File Storage (ABFS) syntax. (e.g.`abfs://container-name@storageaccountname.dfs.core.windows.net/path/to/data` )
            1. Use `*` as a wildcard to include multiple folders or files.
            2. Use `abfss://` for secure (SSL) access.
            3. Example: `abfs://my-container@myaccount.dfs.core.windows.net/2024/*/*.parquet`
            4. Use abfss:// for secure (SSL) access.

        2. File Type (e.g., CSV, Parquet, JSON, ORC)

2. Select a file format, and depending on that file type, enter values for the following parameters:

| File Type | Parameter | Description | 
| ---- | ---- | ---- | 
| CSV | Delimiter | The character that separates fields in a CSV file. Common delimiters include commas (,), tabs (\t), or semicolons (;). | 
| ORC |  | No additional parameters are required for ORC files. | 
| PARQUET | File Processing Strategy | Options include: Evolving Schema (no additional parameters required), Random Files, or Date Partitioned. | 
|  | Base Path (Random Files) | The root directory or location in the storage system where the Parquet files are stored. This is used to locate the data for random file processing. | 
|  | Base Path (Date Partitioned) | The root directory or location where the date-partitioned Parquet files are stored. | 
|  | Pattern (Date Partitioned) | A file pattern that includes a date (e.g., "file-&lt;yyyy-MM-dd&gt;.parquet") to identify the specific files for processing. | 
|  | LookBack Days (Date Partitioned) | The number of days to look back when crawling and processing date-partitioned Parquet files. | 
|  | TimeZone (Date Partitioned) | The time zone in which the partitioned data is recorded. | 
| JSON | Flattening Level | Defines how deeply nested JSON structures will be flattened. Nested JSON fields will be expanded based on the level specified. | 
|  | MultiLine JSON | When enabled, this toggle allows for the processing of JSON data that spans multiple lines. | 
| AVRO | Schema Store Type | Specifies where the AVRO schema is stored. Options could include local files, a schema registry, or other storage systems. | 
| Delta |  | No additional parameters are required for Delta files. | 


3. To monitor multiple assets, click + and repeat.

#### Optional Settings

1. Enable Schema Drift Monitoring to track structural changes in your data lake.

_**Note: Schema drift detection requires scheduled crawler to be enabled.**_

2. Enable **Crawler Execution Schedule** to set up scheduled scans of your Hive tables:
    1. Choose how often the crawler runs (e.g., daily)
    2. Set execution time and time zone
    3. Add multiple execution times if needed

3. Set Notifications
    1. **Notify on Crawler Failure**: Choose one or more channels to receive failure alerts via configured channels.
    2. **Notify on Success**: Toggle this if you'd like to receive success notifications.

4. Click **Submit** to save your configuration to register and begin monitoring the Hive data source.

Once submitted, ADOC adds a **ADLS** data source card on the Data Sources page showing crawling status, time of last run, and observability metrics.

## What’s Next

Once ADLS Gen2 is integrated with ADOC, you can:

- Crawl the data source immediately or let the **Crawler Execution Schedule** run it automatically.
- In **Data Reliability**, view profiling results, schema structures, and rule validation outcomes for monitored ADLS assets.
- Enable **Schema Drift Monitoring** to detect and alert on structural changes in your files.
- Run **Data Reliability checks** on Delta Lake (Delta Parquet) datasets.
- (Optional) Create **SQL Views** for aggregation and validation checks directly on lake data.

## Glossary

**Delta Parquet** – A Parquet-based file format with ACID transaction support, used in Delta Lake for structured data processing.

**ABFS (Azure Blob File System)** – Protocol for accessing ADLS Gen2. Use `abfs://` for standard access and `abfss://` for secure, encrypted connections.

## Additional References

- [Creating a Managed Identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/qs-configure-cli-windows-vm)
- [Workload Identity with AKS](https://learn.microsoft.com/en-us/azure/aks/learn/tutorial-kubernetes-workload-identity)[Authorizing Requests to Azure Data Lake Storage using Azure AD](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/tutorial-windows-vm-access-datalake)
- [Using Kubernetes Service Account for Azure AD Workload Identity Federation](https://blog.identitydigest.com/azuread-federate-k8s/)