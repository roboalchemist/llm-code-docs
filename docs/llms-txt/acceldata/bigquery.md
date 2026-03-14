# Source: https://docs.acceldata.io/documentation/bigquery.md

# Google BigQuery

Google BigQuery is a fully managed, serverless data warehouse that enables fast SQL queries and large-scale data analysis. Integrating BigQuery with the Acceldata Data Observability Cloud (ADOC) gives you continuous visibility into the health, quality, and performance of your datasets.

Once connected, you can:

- Monitor data quality to ensure accuracy and reliability.
- Profile data on a schedule to track trends and anomalies.
- Measure data freshness to identify delays or gaps.
- Detect schema changes that may impact downstream processes.
- Analyze query performance to optimize cost and efficiency.

## Prerequisites

Before you connect BigQuery to ADOC, you need to make sure the right access is set up in Google Cloud. This setup involves three types of GCP projects — each used for a different purpose.

**Which projects do you actually need to create?**

At a minimum, you must have a **Data Source Project**, which contains your actual BigQuery datasets. It’s also **recommended** to create a separate **Service Project**, where ADOC will run its data crawling and job execution. While you can use the same project for both service and data source roles, separating them improves security and operational clarity.

Lastly, if you choose to process data using **Spark**, you’ll need a **Temporary Project** to store intermediate tables. If you’re using **Pushdown** processing, the temporary project is not required.

**What to Do in Each Project**

Grant the following IAM roles to the service account you're using to connect BigQuery to ADOC:

| Project | Purpose | IAM Roles to Assign | 
| ---- | ---- | ---- | 
| Service Project | Runs jobs and sessions initiated by ADOC | - BigQuery Read Session User - BigQuery Job User | 
| Data Source Project | Contains your production data in BigQuery | - BigQuery Data Viewer - Storage Object Viewer (if external tables are stored in GCS) | 
| Temporary Project | Used for temporary processing when using Spark | - BigQuery Data Editor | 


## Add BigQuery as a Data Source

### Step 1: Start Setup

1. Click **Register** from the left main menu.
2. Click **Add Data Source**.
3. Choose **BigQuery** from the list.
4. On the **Data Source Details** page:
    1. Enter a name for this data source.
    2. (Optional) Add a short description.
    3. Choose an existing data plane, or click **Setup Data Plane** to create one.

5. Click **Next** to proceed.

### Step 2: Add Connection Details

1. **Perform one of the following options:**
    1. **Option 1: Use Google Workload Identity**
        1. Turn on the Google Workload Identity toggle.
        2. Set up your data plane with the required Workload Identity configuration. In this case, you do not need to upload a credentials file.

    2. **Option 2: Use a Credentials File** 
        1. Keep the toggle off.Upload your **Google Cloud** credentials (JSON key file).

2. Enter the **Project Name**.
3. Select the **Data Plane Engine** (Spark or Pushdown).
4. Click **Test Connection**. Note _ __If the connection works, you’ll see a “Connected” message. If not, check your credentials and try again._
5. Click **Next**.

### Step 3: Set Up Observability

Before you begin this step, please note:

- If you choose to use **Spark as the data engine** for processing BigQuery data in ADOC, you must specify a **Temporary GCP Project** and a **Temporary Dataset.**
- This temporary project is required to store intermediate data and temporary tables during Spark job execution.
- It must be a valid, accessible project in GCP with BigQuery and GCS permissions enabled.
- The temporary dataset inside this project is used by Spark to stage query results and processed data.
- If you are **not using Spark** and instead opting for **Pushdown Processing** (where queries run directly in BigQuery), the original GCP project that holds your BigQuery dataset will be used.
- In this case, there is no need to create or specify a temporary project or dataset.

Make sure you choose the correct data engine based on your performance, scalability, and cost preferences. Spark requires additional setup (temporary project and dataset), but enables more control and flexibility in processing.

1. Enter the required project and dataset details: 
    1. **Temporary Project Name**: Enter the name of the GCP project used for temporary processing tasks.
    2. **Temporary Dataset Name**: Enter the name of the dataset used to store temporary tables.
    3. **Dataset Name**: Enter the name of the dataset that contains your BigQuery data. You can add multiple datasets if needed.

2. Turn on monitoring options as required:
    - **Enable Query Analysis**: Turn this on to monitor how queries are run on your data.
    - **Enable Data Freshness Monitoring**: Turn this on to track how often your data is updated.
    - **Enable Schema Drift Monitoring**: Turn this on to detect changes in the structure of your BigQuery tables.

3. (Optional) Set up crawler scheduling:
    1. **Enable Crawler Execution Schedule**: Turn this on to run regular scans on your data.
    2. Choose your preferred time and time zone for when the crawler should run.

4. (Optional) Enable failure alerts:
    1. **Notify on Crawler Failure**: Turn this on to get alerts if the crawler fails. **Note:** Schema changes will not be automatically detected unless the crawler is executed. Acceldata recommends scheduling the crawler.

5. Click **Submit**.

You have successfully added BigQuery as a data source. A new card for **BigQuery** will appear on the **Data Sources** page, displaying crawler status and basic connection details.

You can choose to run the crawler immediately or schedule it for later.

## What's Next

After you connect BigQuery, you can go to the following pages to view and manage your data:

- **Reliability** – View data quality scores, profiling status, and rule results for your BigQuery datasets.
- **Pipelines** – Monitor how data flows from BigQuery to downstream systems.
- **Alerts** – See notifications for quality issues or pipeline delays in real time.