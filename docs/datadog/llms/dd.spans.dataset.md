# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.spans.dataset.md

---
title: APM Spans
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > APM Spans
---

# APM Spans

This dataset represents APM span data collected by Datadog Application Performance Monitoring. Spans represent individual units of work within distributed traces, capturing timing, resource usage, and error information. This enables analysis of service dependencies, latency issues, error rates, and overall application performance across your distributed systems.

```
dd.spans
```
APM Public Documentation
{% icon name="icon-external-link" /%}
 Trace Explorer Documentation
{% icon name="icon-external-link" /%}
 Span Tags and Attributes Documentation
{% icon name="icon-external-link" /%}

## Query Parameters

This dataset uses a **polymorphic table function**. You must specify parameters when querying.

| Parameter        | Type            | Required | Description                                                                                                                                           |
| ---------------- | --------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `columns`        | `array<string>` | Yes      | List of fields to return for each span (e.g., 'trace_id', 'service', 'resource_name', '@duration'). Must follow with AS (â¦) to name and type outputs. |
| `filter`         | `string`        | No       | Optional search string. For example: filter => 'service:web-api AND status:error'.                                                                    |
| `from_timestamp` | `string`        | No       | Lower time bound for the query; defaults to the query context if omitted.                                                                             |
| `to_timestamp`   | `string`        | No       | Upper time bound for the query; defaults to the query context if omitted.                                                                             |

## Example Queries

```sql
-- Fetch error spans from a specific service
SELECT * FROM dd.spans(
  columns => ARRAY[
    'timestamp',
    'trace_id',
    'service',
    'resource_name',
    'operation_name',
    '@duration',
    '@error.message',
    '@http.status_code'
  ],
  filter => 'service:web-api AND status:error',
  from_timestamp => now() - interval '1 hour',
  to_timestamp => now()
) AS (
  ts            TIMESTAMP,
  trace_id      VARCHAR,
  svc           VARCHAR,
  resource      VARCHAR,
  operation     VARCHAR,
  duration_ns   BIGINT,
  error_msg     VARCHAR,
  http_status   BIGINT
);
```

## Fields

| Title                        | ID                            | Type            | Data Type | Description                                                                                                                                |
| ---------------------------- | ----------------------------- | --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Timestamp                    | timestamp                     | core            | timestamp | Time the span started. Applies to: all.                                                                                                    |
| Trace ID                     | trace_id                      | core            | string    | Unique identifier for the distributed trace. Applies to: all.                                                                              |
| Environment                  | env                           | core            | string    | Environment identifier (e.g., production, staging). Applies to: all.                                                                       |
| Service                      | service                       | core            | string    | Name of the service generating the span. Applies to: all.                                                                                  |
| Operation Name               | operation_name                | core            | string    | Name of the operation being traced (e.g., http.request, db.query). Applies to: all.                                                        |
| Resource Name                | resource_name                 | core            | string    | Specific resource being accessed (e.g., GET /api/users, SELECT users). Applies to: all.                                                    |
| Status                       | status                        | core            | string    | Span completion status (ok, error). Applies to: all.                                                                                       |
| Ingestion Reason             | ingestion_reason              | core            | string    | Why the span was ingested (e.g., auto, manual, sampling). Applies to: all.                                                                 |
| Span ID                      | span_id                       | core            | string    | Unique identifier for this span. Applies to: all.                                                                                          |
| Parent Span ID               | parent_id                     | core            | string    | ID of the parent span (empty for root spans). Applies to: all.                                                                             |
| Duration                     | @duration                     | event_attribute | int64     | Duration of the span in nanoseconds. Applies to: all.                                                                                      |
| Span Kind                    | @span.kind                    | event_attribute | string    | Type of span (server, client, producer, consumer, internal). Applies to: all.                                                              |
| Version                      | @version                      | event_attribute | string    | Version of the service generating the span. Applies to: all.                                                                               |
| Language                     | @language                     | event_attribute | string    | Programming language of the client SDK (go, java, python, etc.). Applies to: all.                                                          |
| Component                    | @component                    | event_attribute | string    | Component or library generating the span. Applies to: all.                                                                                 |
| Error                        | @error                        | event_attribute | int64     | Whether an error occurred (0 or 1). Applies to: all.                                                                                       |
| Error Message                | @error.message                | event_attribute | string    | Error message text. Applies to: error spans.                                                                                               |
| Error Type                   | @error.type                   | event_attribute | string    | Type or class of the error. Applies to: error spans.                                                                                       |
| Error Stack                  | @error.stack                  | event_attribute | string    | Stack trace for the error. Applies to: error spans.                                                                                        |
| HTTP Method                  | @http.method                  | event_attribute | string    | HTTP method (GET, POST, PUT, etc.). Applies to: HTTP spans.                                                                                |
| HTTP Status Code             | @http.status_code             | event_attribute | int64     | HTTP response status code. Applies to: HTTP spans.                                                                                         |
| HTTP URL                     | @http.url                     | event_attribute | string    | Full URL of the HTTP request. Applies to: HTTP spans.                                                                                      |
| HTTP Route                   | @http.route                   | event_attribute | string    | Parameterized route pattern (e.g., /users/:id). Applies to: HTTP spans.                                                                    |
| HTTP User Agent              | @http.useragent               | event_attribute | string    | User agent string from the request. Applies to: HTTP spans.                                                                                |
| HTTP Request Content Length  | @http.request.content_length  | event_attribute | int64     | Size of the HTTP request body in bytes. Applies to: HTTP spans.                                                                            |
| HTTP Response Content Length | @http.response.content_length | event_attribute | int64     | Size of the HTTP response body in bytes. Applies to: HTTP spans.                                                                           |
| Database System              | @db.system                    | event_attribute | string    | Database system type (postgresql, mysql, mongodb, redis, etc.). Applies to: database spans.                                                |
| Database Operation           | @db.operation                 | event_attribute | string    | Database operation performed (SELECT, INSERT, UPDATE, DELETE). Applies to: database spans.                                                 |
| Database Table               | @db.sql.table                 | event_attribute | string    | Name of the database table being accessed. Applies to: database spans.                                                                     |
| Database Statement           | @db.statement                 | event_attribute | string    | Database statement or query text. Applies to: database spans.                                                                              |
| Database User                | @db.user                      | event_attribute | string    | Database user performing the operation. Applies to: database spans.                                                                        |
| Row Count                    | @db.row_count                 | event_attribute | int64     | Number of rows affected or returned. Applies to: database spans.                                                                           |
| Peer Service                 | @peer.service                 | event_attribute | string    | Name of the remote service being called. Applies to: client spans.                                                                         |
| Peer Hostname                | @peer.hostname                | event_attribute | string    | Hostname of the remote peer. Applies to: client spans.                                                                                     |
| Peer Port                    | @peer.port                    | event_attribute | int64     | Port of the remote peer. Applies to: client spans.                                                                                         |
| Client IP                    | @network.client.ip            | event_attribute | string    | IP address of the client. Applies to: server spans.                                                                                        |
| Messaging System             | @messaging.system             | event_attribute | string    | Messaging system type (kafka, rabbitmq, sqs, etc.). Applies to: messaging spans.                                                           |
| Messaging Destination        | @messaging.destination        | event_attribute | string    | Topic or queue name. Applies to: messaging spans.                                                                                          |
| Messaging Operation          | @messaging.operation          | event_attribute | string    | Messaging operation (publish, receive, process). Applies to: messaging spans.                                                              |
| Host                         | @host                         | event_attribute | string    | Hostname where the span was generated. Applies to: all.                                                                                    |
| Container ID                 | @container_id                 | event_attribute | string    | Container ID where the span was generated. Applies to: containerized services.                                                             |
| Container Name               | @container_name               | event_attribute | string    | Container name where the span was generated. Applies to: containerized services.                                                           |
| Pod Name                     | @pod_name                     | event_attribute | string    | Kubernetes pod name. Applies to: Kubernetes services.                                                                                      |
| User ID                      | @usr.id                       | event_attribute | string    | Unique identifier for the user. Applies to: all.                                                                                           |
| User Email                   | @usr.email                    | event_attribute | string    | Email address of the user. Applies to: all.                                                                                                |
| RPC System                   | @rpc.system                   | event_attribute | string    | RPC system type (grpc). Applies to: gRPC spans.                                                                                            |
| RPC Service                  | @rpc.service                  | event_attribute | string    | Name of the RPC service being called. Applies to: gRPC spans.                                                                              |
| RPC Method                   | @rpc.method                   | event_attribute | string    | Name of the RPC method being called. Applies to: gRPC spans.                                                                               |
| gRPC Status Code             | @rpc.grpc.status_code         | event_attribute | int64     | gRPC status code. Applies to: gRPC spans.                                                                                                  |
| Event ID                     | id                            | core            | string    | A unique identifier for the event.                                                                                                         |
| Discovery Timestamp          | discovery_timestamp           | core            | int64     | The time when Datadog first received the event (milliseconds since Unix epoch). May differ from timestamp if there was an ingestion delay. |
| Tiebreaker                   | tiebreaker                    | core            | int64     | A value used to establish deterministic ordering among events that share the same timestamp.                                               |
| Ingest Size                  | ingest_size_in_bytes          | core            | int64     | The size of the event payload in bytes at the time of ingestion, before any processing.                                                    |
| Random Draw                  | random_draw                   | core            | float64   | A random value between 0.0 and 1.0 assigned at ingestion, useful for consistent sampling across queries.                                   |
