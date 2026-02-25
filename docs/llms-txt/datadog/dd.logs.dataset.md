# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.logs.dataset.md

---
title: Logs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Logs
---

# Logs

This dataset represents log events collected by Datadog Log Management. It provides access to application logs, infrastructure logs, and any other log data ingested into Datadog. Logs can be filtered by service, host, status, and any custom attributes, enabling troubleshooting, debugging, and operational analysis across your entire stack.

```
dd.logs
```
Log Management Public Documentation
{% icon name="icon-external-link" /%}
 Logs Standard Attributes Documentation
{% icon name="icon-external-link" /%}

## Query Parameters

This dataset uses a **polymorphic table function**. You must specify parameters when querying.

| Parameter        | Type            | Required | Description                                                                                                                                                   |
| ---------------- | --------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `columns`        | `array<string>` | Yes      | List of fields to return for each log event (e.g., 'timestamp', 'service', 'message', '@http.status_code'). Must follow with AS (â¦) to name and type outputs. |
| `filter`         | `string`        | No       | Optional search string. For example: filter => 'service:web-api AND status:error'.                                                                            |
| `indexes`        | `array<string>` | No       | Optional list of log indexes to search. If not specified, searches all indexes.                                                                               |
| `from_timestamp` | `string`        | No       | Lower time bound for the query; defaults to the query context if omitted.                                                                                     |
| `to_timestamp`   | `string`        | No       | Upper time bound for the query; defaults to the query context if omitted.                                                                                     |
| `storage`        | `string`        | No       | Optional storage tier to query. Defaults to 'hot'. Use 'flex_tier' for Flex Logs storage.                                                                     |

## Example Queries

```sql
-- Fetch recent error logs from a specific service
SELECT * FROM dd.logs(
  columns => ARRAY[
    'timestamp',
    'host',
    'service',
    'status',
    'message',
    '@http.status_code',
    '@error.message'
  ],
  filter => 'service:web-api AND status:error',
  from_timestamp => now() - interval '1 hour',
  to_timestamp => now()
) AS (
  ts         TIMESTAMP,
  host       VARCHAR,
  svc        VARCHAR,
  status     VARCHAR,
  msg        VARCHAR,
  http_code  BIGINT,
  err_msg    VARCHAR
);
```

## Fields

| Title               | ID                                     | Type            | Data Type | Description                                                                                                                                |
| ------------------- | -------------------------------------- | --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Timestamp           | timestamp                              | core            | timestamp | Time the log event was recorded (e.g., 2025-10-02T09:36:04Z). Applies to: all.                                                             |
| Host                | host                                   | core            | string    | The name of the originating host as defined in metrics (e.g., i-0123456789abcdef0). Applies to: all.                                       |
| Source              | source                                 | core            | string    | Integration name, the technology from which data originated (e.g., nginx, postgresql). Applies to: all.                                    |
| Service             | service                                | core            | string    | The unified service name for the application or service generating data (e.g., web-api). Applies to: all.                                  |
| Status              | status                                 | core            | string    | Level or severity of the log (e.g., info, warn, error). Applies to: all.                                                                   |
| Message             | message                                | core            | string    | Body of the log entry; indexed for full-text search by default. Applies to: all.                                                           |
| Trace ID            | trace_id                               | core            | string    | Used for traces and correlate with other data, including APM traces. Applies to: all.                                                      |
| Client IP           | @network.client.ip                     | event_attribute | string    | IP address of the client that initiated the connection (e.g., 192.168.1.100). Applies to: network logs.                                    |
| Client Port         | @network.client.port                   | event_attribute | int64     | Port used by the client connection (e.g., 51402). Applies to: network logs.                                                                |
| Destination IP      | @network.destination.ip                | event_attribute | string    | IP address of the destination (e.g., 10.0.0.1). Applies to: network logs.                                                                  |
| Destination Port    | @network.destination.port              | event_attribute | int64     | Port of the destination (e.g., 443). Applies to: network logs.                                                                             |
| Client Country      | @network.client.geoip.country.name     | event_attribute | string    | Country name derived from client IP geolocation (e.g., United States). Applies to: network logs.                                           |
| Client Country Code | @network.client.geoip.country.iso_code | event_attribute | string    | ISO country code derived from client IP (e.g., US). Applies to: network logs.                                                              |
| Client City         | @network.client.geoip.city.name        | event_attribute | string    | City name derived from client IP geolocation (e.g., San Francisco). Applies to: network logs.                                              |
| HTTP Method         | @http.method                           | event_attribute | string    | HTTP method used in the request (e.g., GET, POST, PUT). Applies to: HTTP logs.                                                             |
| HTTP Status Code    | @http.status_code                      | event_attribute | int64     | HTTP response status code (e.g., 200, 404, 500). Applies to: HTTP logs.                                                                    |
| HTTP URL            | @http.url                              | event_attribute | string    | Full URL of the HTTP request (e.g., https://example.com/api/v1/users). Applies to: HTTP logs.                                              |
| HTTP User Agent     | @http.useragent                        | event_attribute | string    | User agent string from the HTTP request (e.g., Mozilla/5.0...). Applies to: HTTP logs.                                                     |
| URL Host            | @http.url_details.host                 | event_attribute | string    | Parsed host from the URL (e.g., example.com). Applies to: HTTP logs.                                                                       |
| URL Path            | @http.url_details.path                 | event_attribute | string    | Parsed path from the URL (e.g., /api/v1/users). Applies to: HTTP logs.                                                                     |
| Error Kind          | @error.kind                            | event_attribute | string    | The type or class of the error (e.g., RuntimeError, NullPointerException). Applies to: error logs.                                         |
| Error Message       | @error.message                         | event_attribute | string    | Concise, human-readable description of the error (e.g., Connection refused). Applies to: error logs.                                       |
| Error Stack Trace   | @error.stack                           | event_attribute | string    | Stack trace or traceback for the error. Applies to: error logs.                                                                            |
| Logger Name         | @logger.name                           | event_attribute | string    | Name of the logger (e.g., com.example.MyClass). Applies to: all.                                                                           |
| Thread Name         | @logger.thread_name                    | event_attribute | string    | Name of the current thread when logging (e.g., main, worker-1). Applies to: all.                                                           |
| Method Name         | @logger.method_name                    | event_attribute | string    | Name of the method where the log was generated. Applies to: all.                                                                           |
| Database Instance   | @db.instance                           | event_attribute | string    | Database instance identifier (e.g., orders-db). Applies to: database logs.                                                                 |
| Database Operation  | @db.operation                          | event_attribute | string    | Type of database operation performed (e.g., SELECT, INSERT). Applies to: database logs.                                                    |
| Database User       | @db.user                               | event_attribute | string    | Database user executing the operation. Applies to: database logs.                                                                          |
| User ID             | @usr.id                                | event_attribute | string    | Unique identifier of the user (e.g., 12345). Applies to: all.                                                                              |
| User Email          | @usr.email                             | event_attribute | string    | Email address of the user (e.g., user@example.com). Applies to: all.                                                                       |
| User Name           | @usr.name                              | event_attribute | string    | Full name or display name of the user. Applies to: all.                                                                                    |
| Duration            | @duration                              | event_attribute | int64     | Duration of the operation in nanoseconds (e.g., 1500000). Applies to: all.                                                                 |
| Syslog Hostname     | @syslog.hostname                       | event_attribute | string    | Hostname from syslog message. Applies to: syslog.                                                                                          |
| Syslog Severity     | @syslog.severity                       | event_attribute | int64     | Syslog severity level (0-7). Applies to: syslog.                                                                                           |
| Syslog Facility     | @syslog.facility                       | event_attribute | int64     | Syslog facility code. Applies to: syslog.                                                                                                  |
| Event ID            | id                                     | core            | string    | A unique identifier for the event.                                                                                                         |
| Discovery Timestamp | discovery_timestamp                    | core            | int64     | The time when Datadog first received the event (milliseconds since Unix epoch). May differ from timestamp if there was an ingestion delay. |
| Tiebreaker          | tiebreaker                             | core            | int64     | A value used to establish deterministic ordering among events that share the same timestamp.                                               |
| Ingest Size         | ingest_size_in_bytes                   | core            | int64     | The size of the event payload in bytes at the time of ingestion, before any processing.                                                    |
| Random Draw         | random_draw                            | core            | float64   | A random value between 0.0 and 1.0 assigned at ingestion, useful for consistent sampling across queries.                                   |
