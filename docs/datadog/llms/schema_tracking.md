# Source: https://docs.datadoghq.com/data_streams/schema_tracking.md

---
title: Schema Tracking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Data Streams Monitoring > Schema Tracking
---

# Schema Tracking

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Data Streams Monitoring is not available for the  site.
{% /alert %}


{% /callout %}

Data Streams Monitoring provides visibility into schemas used by producers and consumers, and how schema issues impact downstream services. You can track new schemas added, schemas with errors, and schema evolutions to manage schema migrations and identify issues.

Changing a schema produced by a service without updating the consumer can lead to the consumer struggling to process payloads, blocking further data flow downstream. Understanding schema changes ensures data compatibility between producers and consumers, and ultimately prevents issues.

## Prerequisites{% #prerequisites %}

You must have [Data Streams Monitoring installed](https://docs.datadoghq.com/data_streams/java/) on the producer and consumer services.

## Supported languages{% #supported-languages %}

| Avro    | Protobuf | Minimal tracer version |
| ------- | -------- | ---------------------- |
| Java    | yes      | yes                    | v1.36+           |
| Node.js | yes      | yes                    | v5.24+ or v4.48+ |
| Python  | yes      | yes                    | v2.14+           |
| .NET    | yes      | v3.15+                 |
| Golang  |

## View schemas{% #view-schemas %}

### Schema list{% #schema-list %}

In the [schema list](https://app.datadoghq.com/data-streams/schemas), you can view all schemas used across your pipelines.

{% image
   source="https://datadog-docs.imgix.net/images/data_streams/schema_list.709d05babe1c3f0c8a6d996f11b53e69.png?auto=format"
   alt="List view of three schemas" /%}

For each schema, the table shows the following:

- Type
- Name
- First and last seen
- Produce rate, consume rate, and error rate in the selected time frame
- All producers and consumers of the schema
- Consumer lag: the max Kafka lag for all consumers of a specific schema

Selecting a schema from the list displays the throughput of the schema by service, errors by service, and the full schema.

{% image
   source="https://datadog-docs.imgix.net/images/data_streams/schema_panel.cc6a677b2d15bf8043af4cd92f9dd02d.png?auto=format"
   alt="Schema list view with an open side panel showing detailed information about one schema" /%}

Use the following steps to view detailed information about a schema:

1. Navigate to [Data Streams Monitoring](https://app.datadoghq.com/data-streams/).
1. Click the **Schemas** tab.
1. Select the time frame.
1. Use the quick filters to filter for new schemas (first seen within the last 3 hours), schemas with high error rates, or active schemas.
1. Select a schema. A side panel opens with detailed information for that schema.

### At the service level{% #at-the-service-level %}

For each service you track in Data Streams Monitoring, you can see information about the schemas that it uses.

To view schema information at the service level:

1. Navigate to [Data Streams Monitoring](https://app.datadoghq.com/data-streams/).
1. Ensure the **Explore** tab is selected.
1. Click on a service. The service detail side panel appears.
1. Select the **Schemas** tab.

On the schemas tab, you can:

- View input throughput by schema.
- View a list of all schemas detected within the selected time frame, along with when it was first and last seen, its type (input or output schema), error rate, and throughput.
- Expand a schema to view all of its fields.
