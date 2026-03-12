# Source: https://docs.acceldata.io/documentation/google-cloud-storage.md

# Google Cloud Storage

Integrate Google Cloud Storage (GCS) with ADOC to continuously monitor data stored in your GCS buckets. Once configured, ADOC’s Data Reliability features enable you to crawl assets, detect schema drift, track file activity, and ensure end-to-end observability for your cloud storage.

## Prerequisites

Ensure the following requirements are met before you connect GCS as a data source:

- You have a service account with permissions to your GCP project.
- The following roles are granted to that service account:
- Access to the relevant GCS buckets (e.g. Storage Object Viewer / Admin).
- If using Pub/Sub channel monitoring: permission to publish/subscribe.
- A Data Plane in GCP is available (existing or new). The Data Plane is required for crawling and observability and must meet ADOC compatibility requirements (i.e. Kubernetes version ≥ 1.25)

---

## Add GCS as a Data Source

Follow these steps to set up GCS in ADOC:

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source**.
3. Select **GCS** from the list of data sources.
4. On the **Data Source Details** page:
    1. Enter a name for this data source that is unique within your tenant. 
    2. Optionally, add a brief description to clarify its purpose.
    3. Ensure the Data Reliability toggle is enabled and select your data plane from the drop-down list.

5. Select **Next** to proceed.

### Step 2: Add Connection Details

1. Choose an authentication method based on your infrastructure setup:
    - **Google Workload Identity**: 
Enable this toggle if your Data Plane is running on GKE (Google Kubernetes Engine) and has been configured to use Workload Identity. This method allows ADOC to securely authenticate with GCS without needing to upload service account credentials.
    - **Credentials File**: If you're not using GKE with Workload Identity, upload a service account credentials JSON file. After uploading:

2. You can optionally enable **Use Secret Manager** to store the credentials securely.
    1. If enabled, select your **Secret Manager provider** and enter the **Secret Name or Key**.
    2. Provide:
        1. Project Name: Specify the name of your GCP project that contains the GCS bucket.
        2. Bucket Name: Enter the name of the specific GCS bucket you want to connect to within your GCP project.

3. Select a **File** **Monitoring Channel Type**: Select **Pub/Sub** if you want to enable real-time file change detection in the GCS bucket using Google Pub/Sub.
    1. None: No real-time monitoring. Crawler will scan data on schedule.
    2. Pubsub: Triggers ingestion based on object creation or update events in GCS.

4. Select **Test Connection.** On success, you’ll see “Connected”. On failure, re‑check your service account JSON and client email settings.
5. Click **Next** to proceed.

### Step 3: Setup Observability

1. Enter values for the required fields:
2. Project Name
3. For each asset:
4. Asset Name
5. Path Expression (e.g. gs://bucket-name/observability.csv)
6. File Type (e.g., CSV, Parquet, JSON, ORC)
7. Depending on the file type, enter values for the following parameters:

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


3. Use a wildcard path (e.g. gs://bucket-name) to include all files in the bucket.
4. To monitor multiple assets, click + and repeat.

**Optional Settings**

5. Enable Schema Drift Monitoring to track structural changes in your Hive tables. Note _**Schema drift detection requires scheduled crawler to be enabled.**_
6. Enable **Crawler Execution Schedule** to set up scheduled scans of your Hive tables:
    1. Choose how often the crawler runs (e.g., daily)
    2. Set execution time and time zone
    3. Add multiple execution times if needed

7. Set Notifications
    1. **Notify on Crawler Failure**: Choose one or more channels to receive failure alerts via configured channels.
    2. **Notify on Success**: Toggle this if you'd like to receive success notifications.

8. Click **Submit** to save your configuration to register and begin monitoring the GCS data source.

Once submitted, ADOC adds a **GCS data source card** on the Data Sources page showing crawling status, time of last run, and observability metrics.

---

## What’s Next

1. Run your first crawler immediately or wait for the scheduled crawl.
2. Access the Data Reliability section to review asset inventory, file-level trends, schema drift alerts, and data quality insights.
3. Configure custom monitoring policies or alerts for schema changes, late files, or ingestion failures.
4. To add more assets or file types later, edit the GCS data source configuration.

---

## Glossary

| Term | Definition | 
| ---- | ---- | 
| **Channel Monitoring** | A mechanism to detect file changes (uploads or modifications) in real time. In GCS by using Google Pub/Sub, this enables ADOC to start ingestion or profiling immediately when changes occur, rather than waiting for a scheduled crawler run. | 
| **Schema Drift Monitoring** | Detects changes in file schema over time for assets being crawled. | 
| **Google Workload Identity** | A Google Cloud feature that securely binds Kubernetes service accounts to Google Cloud service accounts, allowing applications to access Google Cloud resources without managing service account keys. | 


---

## Additional Reference

- If your service accounts or buckets are in a separate GCP project, refer to the [Cross Implementation](https://docs.acceldata.io/documentation/cross-account-access-implementation#gcs) guide.