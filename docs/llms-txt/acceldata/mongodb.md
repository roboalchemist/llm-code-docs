# Source: https://docs.acceldata.io/documentation/mongodb.md

# MongoDB

Integrate **MongoDB** with **Acceldata Data Observability Cloud (ADOC)** to monitor and manage your MongoDB assets with comprehensive data reliability and observability capabilities.

**MongoDB** is a leading NoSQL database that stores data in flexible, JSON-like documents, allowing for scalable, schema-less storage. Integrating MongoDB with ADOC enables you to monitor collections, views, and virtual assets efficiently while maintaining visibility into data quality, reliability, and performance.

Starting from **ADOC v4.2.1**, support includes both **Collections** and **Views** within MongoDB data sources, allowing broader observability coverage.

---

## Supported Authentication Methods

| Authentication Type | Description | 
| ---- | ---- | 
| **Direct Connection (MongoDB URI)** | Connect using a MongoDB connection string URI containing host, port, and authentication details. | 
| **Secret Manager** | Securely fetch MongoDB credentials and connection details from an integrated secrets management service such as AWS Secrets Manager, Azure Key Vault, or GCP Secret Manager. | 


---

## Prerequisites and Permissions

Before integrating MongoDB with ADOC, ensure the following:

1. A running MongoDB instance (self-hosted or cloud-hosted).
2. Valid MongoDB credentials with read access to the target database(s).
3. ADOC installed with an operational **Data Plane**.
4. The following MongoDB roles or privileges for the configured user:
    - `readAnyDatabase` or `read` on the required databases.
    - Optional: `listDatabases` for discovery.
    - For aggregation-based profiling or SQL views, ensure access to execute the `aggregate` command.

---

## Configuration Parameters

| Parameter | Description | Mandatory | Example | 
| ---- | ---- | ---- | ---- | 
| **Data Source Name** | Unique name to identify the MongoDB data source. | ✅ | `MongoDB-Prod` | 
| **Description** | Optional notes about the MongoDB data source. | ❌ | `Production MongoDB for Retail Analytics` | 
| **Data Plane** | The ADOC Data Plane where MongoDB integration runs. | ✅ | `dp-us-west` | 
| **MongoDB URI** | MongoDB connection URI string. | ✅ | `mongodb://username:password@hostname:27017/admin` | 
| **MongoDatabase** | The database name to be monitored. | ✅ | `sales_db` | 
| **Use Secret Manager** | Option to fetch credentials from a configured secret manager. | Optional | `True` | 
| **Secret Manager Name** | Name of the configured secret manager (e.g., AWS Secrets Manager). | Optional | `aws_secret_mgr` | 
| **Secret Key/Name** | Identifier key to retrieve credentials. | Optional | `mongo_prod_uri` | 


---

## Adding MongoDB as a Data Source

Follow these steps to register MongoDB as a data source in ADOC:

1. Navigate to **Register** -&gt; **Data Sources** tab.
2. Click **Add Data Source**.
3. Select **MongoDB** from the list of supported connectors.
4. Choose one of the following connection methods:
    - **Using MongoDB URI:** Enter the connection string and database name.
    - **Using Secret Manager:** Toggle _Use Secret Manager_, select the service, and enter the secret key and MongoDB database.

5. Click **Test Connection** to validate credentials and network connectivity.
6. Once validated, click **Next** to proceed to the **Observability Set Up** page.

---

## Configuring Observability Setup

After a successful connection, configure the databases and crawler settings:

### Schema Flattening Level

MongoDB stores data in nested, hierarchical JSON-like structures. The **Schema Flattening Level** setting in ADOC determines how deeply ADOC should flatten these nested fields when interpreting and profiling MongoDB documents.

| Level | Description | Example | 
| ---- | ---- | ---- | 
| 1 | Flattens only the top-level fields. Nested objects remain unexpanded. | `{ "user": { "id": 1, "name": "John" } }` → `user` (object) | 
| 2 | Flattens one level deeper. Nested objects become separate fields with dot notation. | `{ "user": { "id": 1, "name": "John" } }` → `user.id`, `user.name` | 
| 3 and above | Recursively flattens nested fields up to the specified depth. | `{ "order": { "customer": { "name": "Alice" } } }` → `order.customer.name` | 


> - Use **Level 1** for compact schema representation when collections contain deeply nested documents.> - Use **Level 2 or higher** to capture detailed data attributes during profiling and quality checks.> - Higher levels increase schema size and processing time but provide richer data insights.

### Database Configuration

- **Database Name:** Provide one or more MongoDB databases to be monitored.
- Click **+** to add multiple databases if needed.

### Optional Settings

#### Enable Schema Drift Monitoring

Enable this to track structural changes (field additions, deletions, or type changes) within MongoDB collections or views over time.

Note Schema drift detection requires the crawler to be scheduled via the **Crawler Execution Schedule** setting.

#### Enable Crawler Execution Schedule

Set up automatic crawls to profile and update metadata regularly.
Options include:

- Frequency (e.g., Daily, Weekly, Hourly)
- Execution Time and Time Zone
- Multiple execution windows if required

#### Set Notifications

- **Notify on Crawler Failure:** Choose notification channels (e.g., Slack, Email) to receive alerts when a crawler job fails.
- **Notify on Success:** Toggle to receive notifications for successful crawler runs.

7. Click **Submit** to complete the setup and register MongoDB as a monitored data source.

---

## Creating SQL Views on MongoDB Data Sources

ADOC allows you to create **virtual assets** using MongoDB aggregation pipelines. These are treated as **SQL Views**, enabling advanced transformations without modifying source data. For more information about SQL Views, refer to the [Enrich Assets](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/enrich-assets#1-sql-view) documentation.

### Steps to Create an SQL View

1. Go to **Discover Assets** in ADOC.

<ol start="2">
  <li>
    Click &#8984; Actions&nbsp;&nbsp;and select <strong>Add SQL View</strong>.
  </li>
</ol>

3. Enter a name for the virtual asset.
4. Select your **MongoDB data source**, **Database**, and **Collection/View**.
5. Provide a description and define the **Aggregation Pipeline** logic.

#### Example Aggregation Pipeline

```json
[
  { "$match": { "department": "Engineering" } },
  { "$project": { "_id": 1, "name": 1, "salary": 1, "years_of_service": 1 } }
]
```



> This example filters employee data by department and selects specific fields for profiling.

6. Click **Save** to register the SQL View. It can now be used for profiling, quality checks, or reconciliation jobs within ADOC.

---

## Managing Data Source Performance and Job Concurrency

ADOC includes a **Control Plane Queueing Mechanism** to manage concurrent job executions.
You can configure concurrency limits per data source to prevent database overload.

### Key Features

- **Concurrency Control:** Limit the number of simultaneous profiling, quality, or reconciliation jobs.
- **Queueing Mechanism:** Jobs exceeding concurrency limits are queued until a slot becomes available.
- **Configurable Slots:** Define how many jobs can run concurrently per MongoDB data source.

For setup details, see [Control Plane Concurrent Connections and Queueing Mechanism](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/apache-hdfs#control-plane-concurrent-connections-and-queueing-mechanism).

---

## Next Steps

- View your MongoDB data source in **Register &gt; Data Sources**.
- Run a crawler to discover collections and views.
- Explore inferred schema, metadata, and reliability metrics in the MongoDB source dashboard.
- Use **SQL Views** to define and monitor virtual assets.
- Review crawler notifications to ensure continuous data monitoring.