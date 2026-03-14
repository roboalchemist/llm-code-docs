# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/custom-connection.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Any Data Source

> Connect to any data source using the custom connector. Configure the connector to use a batch or streaming source.

## Step 1: Select the Data Source Category

To begin the connection setup, select the **appropriate data source category** that best represents the type of system you are connecting to. This helps in identifying the **ingestion mode** and ensures the correct configurations are applied.

### **Batch Sources**

* Select this option for **file-based systems**, such as:
  * **AWS S3**
  * **Google Cloud Storage (GCS)**
  * **Azure Blob Storage**
  * **HDFS**
  * **Local file systems**
* These sources typically provide **static data** that can be **ingested periodically**.

### **Streaming Sources**

* Choose this category for **real-time streaming data sources**, such as:
  * **Apache Kafka**
  * **Amazon Kinesis**
  * **Apache Pulsar**
* These sources **continuously generate data**, requiring Pinot to process events in **real time**.

### **SQL-Based Sources**

* Use this option when connecting to **traditional relational databases**, such as:
  * **Snowflake**
  * **Google BigQuery**
* This setup allows Pinot to **fetch data using SQL queries**.

***

## Step 2: Configure the Data Source Connection

Once you have selected the appropriate **data source category**, enter the required **connection configuration details**.   These settings will depend on the type of source you are connecting to and should align with **Apache Pinot’s ingestion configuration**. After entering the configuration details correctly, proceed with **validating the connection**.

***

## Step 3: Preview the Data

Click **Show Sample Data** to preview the source data before finalizing the configuration.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

Built with [Mintlify](https://mintlify.com).
