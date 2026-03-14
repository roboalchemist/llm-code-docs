# Source: https://docs.acceldata.io/documentation/trino-integration-with-openlineage.md

# Trino Integration with OpenLineage

ADOC integrates with Trino using **OpenLineage** to capture query execution metadata and automatically build pipeline observability. When configured, Trino emits OpenLineage events for every query execution. ADOC ingests these events and uses them to construct pipelines and pipeline runs, enabling visibility into how data is processed and moved across Trino workloads.

**How Trino integration with OpenLineage works in ADOC:**

- Trino emits **OpenLineage events** for each query execution.
- ADOC ingests these events.
- Each **unique query pattern** is modeled as a **Pipeline**.
- Each **execution of that query** is modeled as a **Pipeline Run**.

**Example**

Consider the following queries executed on a Trino table (T1) :

```none
INSERT INTO T1 VALUES (1);

INSERT INTO T1 VALUES (2);
```



In ADOC, this results in:

- 1 Pipeline → INSERT INTO T1
- 2 Pipeline Runs → one per execution

This keeps pipelines stable while capturing execution-level observability.

---

## Pipeline Stitching at Query Level

Unlike traditional job-based pipelines, Trino pipelines in ADOC are stitched at the query level.

- The **query signature** defines the pipeline.
- Each **runtime execution** of that query becomes a pipeline run.

- **Inputs and outputs** are automatically derived from OpenLineage metadata.

This approach allows ADOC to model highly dynamic, ad-hoc Trino workloads without requiring predefined pipeline definitions.

---

## Enhanced Lineage & Related Pipelines

With this integration, ADOC can:

- Identify pipelines reading from a table
- Identify pipelines writing to a table

- Show upstream and downstream dependencies

**Use cases**:

- Impact analysis
- Data quality investigations

- Change management

---

## Configuration on Trino

### 1. Configure OpenLineage EvenListener

File: 

```none
/etc/trino/event-listener.properties
```



Add:

```none
event-listener.name=openlineage
openlineage-event-listener.transport.type=http
openlineage-event-listener.transport.url=https://<ADOC_HOST>/torch-pipeline/api/v1/lineage
openlineage-event-listener.transport.headers=accessKey:<ADOC_ACCESS_KEY>,secretKey:<ADOC_SECRET_KEY>
openlineage-event-listener.trino.uri=http://<TRINO_HOST>:8080
openlineage-event-listener.trino.include-query-types=CREATE_TABLE,CREATE_VIEW
```



### 2. Configure TLS TrustStore

1. Download certificate from ADOC UI as: `acceldata-cert.pem`
2. Add the above file to a folder, example “**certs**”.
3. In the created folder, generate a **truststore.jks** file using:

```none
keytool -import -trustcacerts -noprompt \
  -alias acceldata \
  -file ./acceldata-cert.pem \
  -keystore ./truststore.jks \
  -storepass changeit
```



4. Mount the files in the Trino instance at this location: `/etc/trino/certs`

After configuration, Trino queries automatically emit OpenLineage events to ADOC.