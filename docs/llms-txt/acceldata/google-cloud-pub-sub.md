# Source: https://docs.acceldata.io/documentation/google-cloud-pub-sub.md

# Google Cloud Pub/Sub

Integrate **Google Cloud Pub/Sub** with **Acceldata Data Observability Cloud (ADOC)** to monitor, profile, and ensure the reliability of your streaming data pipelines. Introduced in **ADOC v4.7.0**, this connector provides end-to-end observability for Pub/Sub topics through seamless data crawling, quality checks, and reconciliation.

**Google Cloud Pub/Sub** is a fully managed messaging service for building event-driven applications. By integrating it with ADOC, you can ensure visibility into your message data, validate data integrity, and maintain consistent reliability across your streaming systems.

ADOC connects to Pub/Sub as a **batch reader** using **ephemeral subscriptions**, ensuring each job run is isolated, consistent, and automatically cleaned up after completion.

Note The Pub/Sub connector supports the same observability capabilities as Kafka, including crawling, profiling, data quality checks, and reconciliation—providing consistent data reliability across streaming systems.

---

## Supported Authentication Methods

| Authentication Type | Description | 
| ---- | ---- | 
| **Google Workload Identity (Default)** | Uses GCP Workload Identity Federation for secure, identity-based authentication between ADOC Data Plane and GCP. | 
| **Service Account Key File (JSON)** | Authenticate using a GCP service account JSON key uploaded directly in ADOC. | 


---

## Supported Capabilities

- **Data Crawling:** Discover and catalog Pub/Sub topics and message schemas.
- **Data Profiling:** Analyze message payloads and structure for completeness, type distribution, and schema inference.
- **Data Quality Checks:** Apply validation rules and monitor message-level anomalies.
- **Reconciliation:** Compare Pub/Sub message data with other data sources (e.g., Kafka, BigQuery) to detect discrepancies and ensure consistency.
- **Schema Drift Monitoring:** Track structural changes in message payloads over time.

---

## Prerequisites and Permissions

Before adding Pub/Sub as a data source, ensure the following:

1. You have an existing or newly configured **Data Plane** in ADOC.
2. The Pub/Sub service account or workload identity used has these IAM permissions:

| Permission | Resource Scope | Purpose | 
| ---- | ---- | ---- | 
| `pubsub.subscriptions.create` | Subscription Project ID | Create ephemeral subscriptions for each job. | 
| `pubsub.topics.attachSubscription` | Source Project ID (each topic) | Link ephemeral subscriptions to topics. | 
| `pubsub.subscriptions.delete` | Subscription Project ID | Delete ephemeral subscriptions post-job. | 
| `pubsub.subscriptions.consume`, `pubsub.messages.pull`, `pubsub.messages.acknowledge` | Ephemeral Subscriptions | Read and acknowledge messages. | 
| `pubsub.topics.get` | Source Project ID | Retrieve topic metadata and retention settings. | 


> ⚠️ The Test Connection step validates these permissions, which are essential for ADOC job execution.

---

## Configuration Parameters

| Parameter | Description | Mandatory | Example | 
| ---- | ---- | ---- | ---- | 
| **Data Source Name** | Unique name for the Pub/Sub data source. | ✅ | `GCP-PubSub-Prod` | 
| **Description** | Optional notes about the data source. | ❌ | `Production Pub/Sub pipeline` | 
| **Data Plane** | ADOC Data Plane for processing. | ✅ | `dp-gcp-us` | 
| **Source Project ID** | GCP Project ID hosting Pub/Sub topics. | ✅ | `source-project-123` | 
| **Subscription Project ID** | GCP Project ID for creating ephemeral subscriptions. | ✅ | `subscription-project-xyz` | 
| **Region** | GCP region of the topics. | ✅ | `us-east1` | 
| **Authentication Method** | Choose _Workload Identity_ or _Service Account File_. | ✅ | `Workload Identity` | 
| **Service Account Key File** | JSON key file for Service Account authentication. | ⚙️ Required for key-file auth | `/path/to/service-account.json` | 
| **Topics of Interest** | List of Pub/Sub topics to monitor. | ✅ | `orders-topic, events-topic` | 


---

## Adding Google Cloud Pub/Sub as a Data Source

Follow these steps to register Pub/Sub in ADOC:

1. Navigate to **Register** -&gt; **Data Sources**.
2. Click **Add Data Source**.
3. Select **Google Cloud Pub/Sub**.
4. Enter a **Data Source Name** and optional **Description**.
5. Enable the **Data Reliability** toggle.
6. Choose a **Data Plane**.
7. Click **Next** and provide the following:
    - Source Project ID
    - Subscription Project ID
    - Region
    - Authentication Method (Workload Identity or Service Account)
    - Topics of Interest

8. Click **Test Connection** to validate permissions and access.
9. Once validation succeeds, click **Next**.
10. Proceed to **Set Up Observability** to configure topic details and optional settings.

---

## Configuring Topic Details

After connecting successfully, configure topic-level settings to enable profiling and observability.

### Topic Configuration Fields

| Field | Description | Example | 
| ---- | ---- | ---- | 
| **Asset Name** | Logical name for the topic in ADOC. | `orders_topic_asset` | 
| **Topic Name** | Pub/Sub topic name. | `orders-topic` | 
| **Message Format** | Supported formats: JSON, Avro, Confluent Avro. | `JSON` | 
| **Schema ID** | Schema Registry ID (Avro/Confluent Avro). | `order-schema-v3` | 
| **Schema Naming Strategy** | Defines schema lookup rule (`TOPIC_NAME`, `RECORD_NAME`, or `TOPIC_RECORD_NAME`). | `TOPIC_RECORD_NAME` | 
| **Schema File Path** | Path to Avro or Confluent schema file (if manually provided). | `/schemas/order.avsc` | 


> For Avro or Confluent Avro topics, ensure the Schema Registry endpoint is accessible to ADOC.

---

## Optional Settings

### Schema Flattening Level

Determines how deeply ADOC flattens nested JSON structures in message payloads.

| Level | Description | Example | 
| ---- | ---- | ---- | 
| **1** | Flattens only top-level fields. | `user` (object) | 
| **2** | Flattens one level deeper. | `user.id`, `user.name` | 
| **3+** | Fully flattens nested objects using dot notation. | `order.customer.name` | 


### Enable Schema Drift Monitoring

Track structural changes in message schemas across time.

> Requires Enable Crawler Execution Schedule to be turned on.

### Enable Crawler Execution Schedule

Schedule automatic crawls to update schema and profile metadata.

- Set frequency (Daily, Weekly, Hourly)
- Configure time and timezone
- Add multiple runs if needed

### Notifications

- **Notify on Crawler Failure:** Get alerts via Slack or Email.
- **Notify on Success:** Toggle to receive success notifications.

---

## Data Reading Strategies

ADOC supports two reading modes for Pub/Sub:

### Full Read Mode

Reads all messages available in the topic’s retention period.

> Ensure topic or subscription retention is configured appropriately.

### Incremental Read Mode

Reads messages published after the last processed job (timestamp-based) or within a specified lookback window.

> Changing strategies resets the internal watermark and may reprocess older messages.

---

## Cross-System Reconciliation with Kafka

Once both **Google Cloud Pub/Sub** and **Kafka** are added as data sources in ADOC,
you can create **Reconciliation Policies** between them to ensure consistency across your streaming data systems.

**How It Works**

- ADOC reads data from Pub/Sub and Kafka topics using their connectors.
- The reconciliation engine compares message data for differences in record count, schema, or payload.
- Runs in **batch mode** to provide a consistent snapshot for each job execution.

**Use Cases**

- Verify message consistency between Kafka → Pub/Sub ingestion pipelines.
- Detect data loss or duplication across systems.
- Maintain end-to-end data reliability across multi-cloud architectures.

> Reconciliation validates data integrity—it does not stream or replicate data in real time.

---

## Next Steps

- View Pub/Sub data sources under **Data Reliability -&gt; Data Sources**.
- Schedule crawlers and enable drift monitoring.
- Create reconciliation policies between Pub/Sub and Kafka.
- Monitor data quality and profiling metrics via dashboards.