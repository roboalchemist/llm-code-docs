# Source: https://docs.acceldata.io/documentation/kafka.md

# Apache Kafka

This guide walks you through connecting Kafka as a data source in ADOC, configuring observability, and enabling advanced features like concurrency control and freshness policies.

## Prerequisites

Ensure the following requirements are met before you connect Kafka as a data source:

- A running Kafka cluster with accessible topics that can publish messages in a supported format such as **JSON**, **Avro**, or **Confluent Avro**.
- An active ADOC Data Plane with access to Kafka brokers
- Depending on your Kafka setup, you may need the following security credentials:
- Username and password (for SASL or Basic Auth)
- Certificate Authority (CA) or Server Certificate (SSL) certificates (keystore and truststore)
- Kerberos principal and keytab

---

## Add Kafka as a Data Source

Follow these steps to set up HDFS in ADOC:

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source**.
3. Select **Kafka** from the list of data sources.
4. On the **Data Source Details** page:
    1. Enter a unique name for this data source.
    2. Optionally, add a brief description to clarify its purpose.
    3. Ensure the **Data Reliability** toggle is enabled and select your data plane from the drop-down list.

5. Select **Next** to proceed.

### Step 2: Add Connection Details

**Common Fields (Displayed for All Protocols)**

| Field | Description | 
| ---- | ---- | 
| **Bootstrap Servers** | Kafka broker address (e.g., `hostname:port`). Required. | 
| **Schema Registry Server** | URL of the Schema Registry, if applicable. Optional. | 
| **Schema Registry Authentication Type** | If you provide a Schema Registry URL, you must also configure its authentication details (if required by your Kafka setup).  **Authentication Type:** Select **Basic Auth** as the authentication type and provide the associated username and password. **Username and Password:** Enter the credentials used to access the schema registry. | 


**Protocol-Specific Fields**

To understand each protocol, refer to the [Apache Kafka security protocol](https://kafka.apache.org/25/javadoc/org/apache/kafka/common/security/auth/SecurityProtocol.html) documentation.

| Security Protocol | Field | Description | 
| ---- | ---- | ---- | 
| **Plain Text** | – | No additional fields required. | 
| **SSL** | Use data plane for connection files | Toggle ON to fetch SSL files from data plane; OFF to upload manually. If **Use data plane for connection files** is enabled, the Keystore/Truststore file location fields will not appear. These files are fetched automatically from the Data Plane configuration. | 
|  | SSL Keystore FileLocation | Upload the Keystore file containing the client certificate. | 
|  | SSL Keystore Password | Password to unlock the Keystore file. | 
|  | SSL Truststore FileLocation | Upload the Truststore file used to validate the server certificate. | 
|  | SSL Truststore Password | Password to unlock the Truststore file. | 
|  | Kafka Additional Properties | Optional key-value pairs for advanced connection configuration. | 
| **SASL Plain Text** | SASL Mechanism | Select the authentication mechanism (e.g., `PLAIN`, `SCRAM-SHA-256`). | 
|  | Kerberos Principal | Kerberos identity used to authenticate (e.g., `kafka/node1.example.com@EXAMPLE.COM`). | 
|  | Kerberos Service Name | Kafka service name used during Kerberos authentication (e.g., `kafka`). Must match server-side principal. | 
|  | Kerberos KeyTab File Location | Path to the KeyTab file containing credentials. Required for passwordless authentication. | 
|  | Kafka Additional Properties | Optional key-value pairs, including authentication details. | 
| **SASL_SSL** | SASL Mechanism | Select the SASL authentication mechanism. | 
|  | SSL Verification Required | Toggle ON to enforce SSL certificate validation. | 
|  | Use data plane for connection files | Toggle ON to fetch SSL files from data plane; OFF to upload manually. | 
|  | SSL Keystore FileLocation | Upload the Keystore file. | 
|  | SSL Keystore Password | Password for the Keystore file. | 
|  | SSL Truststore FileLocation | Upload the Truststore file. | 
|  | SSL Truststore Password | Password for the Truststore file. | 
|  | Kafka Additional Properties | Optional key-value configuration. | 


1. Select **Test Connection**. If successful, you’ll see “Connected.” **If the test fails**, ensure your bootstrap server is reachable, credentials are correct, and that the ADOC Data Plane service (`ad-analysis-standalone`) is running.
2. Select **Next** to proceed.

### Step 3: Setup Observability

Configure how ADOC will monitor your Kafka topic:

1. **Asset Name** – Descriptive name for this Kafka feed.
2. **Topic Name** – Single topic or topic pattern.
3. **Topic Format** – Choose `JSON`, `Avro`, or `Confluent Avro`.
4. **Schema Registry URL** – Required for Avro formats.
5. _(Optional)_ Enable **Job Concurrency Control** and set **Max Slots** to manage parallel profiling. For more information, see [Control Plane Concurrent Connections and Queueing Mechanism](https://docs.google.com/document/d/1W9E7ZGWzrtjXnNbVOHq-6x9F1FDbI0Fqa2gSPqUn5QI/edit?tab=t.0#heading=h.nnqa6y67lnw)
6. Click **Submit** to finalize setup.

---

## What’s Next

1. Crawl data from the configured Kafka topic.
2. Profile the data source to fetch metrics like message count, size, and freshness.
3. Apply ADOC’s data reliability rules and policies to validate the quality of your Kafka topic.