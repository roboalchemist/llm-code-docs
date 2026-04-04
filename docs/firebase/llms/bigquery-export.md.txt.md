# Source: https://firebase.google.com/docs/perf-mon/bigquery-export.md.txt

> [!NOTE]
> **Note:** Exporting Performance Monitoring data into BigQuery is currently only available for **Apple and Android apps**.

You can export Performance Monitoring data from Apple and Android apps into
[BigQuery](https://bigquery.cloud.google.com) for further
analysis. BigQuery allows you to analyze the data using
BigQuery SQL, export it to another cloud provider, and even use the
data for your custom ML models.

## Enable BigQuery export

> [!NOTE]
> **Note:** Make sure that you have the [required level of access](https://firebase.google.com/docs/projects/bigquery-export#permissions-and-roles) to view or manage settings for data export to BigQuery.

1. Go to the
   [*Integrations*](https://console.firebase.google.com/project/_/settings/integrations)
   page in the Firebase console, then click **Link** in the **BigQuery**
   card.

2. Follow the on-screen instructions to enable BigQuery.

   When you enable BigQuery export for Performance Monitoring, the following
   occurs:
   - Firebase [exports a copy of your existing data](https://firebase.google.com/docs/perf-mon/bigquery-export#what-data-exported) to
     BigQuery. The initial propagation of data for export may take up to
     48 hours to complete.

     - You can [manually schedule data backfills](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer) up to the past 30 days or for the most recent date when you enabled BigQuery export (whichever is most recent).
   - After the dataset is created, the location
     can't be changed, but you can copy the dataset to a different location
     or manually move (recreate) the dataset in a different location. To learn
     more, see [Change dataset location](https://firebase.google.com/docs/projects/bigquery-export?product=perfmon#change-dataset-location).

   - Firebase sets up regular syncs of your data from your Firebase project to
     BigQuery. These daily export operations usually finish in 24 hours
     after they are scheduled.

   - By default, all apps in your project are linked to BigQuery. Any
     apps that you later add to the project are automatically linked to
     BigQuery. You can
     [manage which apps send data](https://support.google.com/firebase/answer/6318765#manage).

To deactivate BigQuery export,
[unlink your project](https://support.google.com/firebase/answer/6318765#unlink)
in the Firebase console.

## What data is exported to BigQuery?

For each app in the project, the export creates a table that includes all the
captured performance events. Each row in the table is a single performance event
that can be one of the following:

- **Duration trace** --- traces that collect, by default, the metric of
  "duration", which include app start, app-in-foreground, and app-in-background,
  as well as any developer-instrumented custom code traces

  - `event_type` is `DURATION_TRACE`
  - `event_name` is the same as the trace name
- **Trace metric** --- custom metrics that are associated with
  developer-instrumented custom code traces

  - `event_type` is `TRACE_METRIC`
  - `event_name` is the name of the metric
  - `parent_trace_name` is the trace name that contains this metric
- **Screen trace** --- traces spanning the lifetime of a screen (screen rendering
  traces)

  - `event_type` is `SCREEN_TRACE`
  - `event_name` is prefix `_st_` plus the actual screen name
- **Network request** --- traces spanning the lifetime of a network request
  (HTTP network request traces)

  - `event_type` is `NETWORK_REQUEST`
  - `event_name` is the categorized pattern of the network request URL

Each performance event contains attributes of the event (such as country and
carrier of the client device), as well as event-specific information:

- Duration traces, trace metrics, and screen traces contain `trace_info`
- Trace metrics contain `trace_info.metric_info`
- Screen traces contain `trace_info.screen_info`
- Network traces contain `network_info`

### Detailed data schema

| **Field Name** | **Type** | **Description** |
|---|---|---|
| event_timestamp | timestamp | Timestamp since Epoch when event started on client device (trace start, network start, etc.) |
| app_display_version | string | Display version of the application (for example, "4.1.7") - For Android --- `VersionName` - For iOS --- `CFBundleShortVersionString` |
| app_build_version | string | Build version of the application (for example, "1523456") - For Android --- `VersionCode` - For iOS --- `CFBundleVersion` |
| os_version | string | OS version of the client device - For Android --- Android API level (for example "26") - For iOS --- iOS version (for example "11.4") |
| device_name | string | Name of the client device (for example, "Google Pixel") |
| country | string | Two-letter country code of the country from which the event took place (for example, "US", or "ZZ" for unknown country) |
| carrier | string | Carrier of the client device |
| radio_type | string | Active radio type when the event took place (for example, "WIFI") |
| custom_attributes | ARRAY\<RECORD\> | All custom attributes attached to this event |
| custom_attributes.key | string | Key of the custom attribute |
| custom_attributes.value | string | Value of the custom attribute |
| event_type | string | Type of the event; possible values: - `DURATION_TRACE` --- traces that collect, by default, the metric of "duration", which include app start, app-in-foreground, and app-in-background, as well as any developer-instrumented custom code traces - `SCREEN_TRACE` --- traces spanning the lifetime of a screen (screen rendering traces) - `TRACE_METRIC` --- custom metrics that are associated with developer-instrumented custom code traces - `NETWORK_REQUEST` --- traces spanning the lifetime of a network request (HTTP network request traces) |
| event_name | string | Name of the event - For `DURATION_TRACE` --- trace name - For `TRACE_METRIC` --- custom metric name - For `SCREEN_TRACE` --- `_st_` followed by the trace name - For `NETWORK_REQUEST` --- network request URL pattern |
| parent_trace_name | string | Name of the parent trace that carries the trace metric Only present for `TRACE_METRIC` |
| trace_info | RECORD | Only present for `DURATION_TRACE`, `SCREEN_TRACE`, and `TRACE_METRIC` |
| trace_info.duration_us | int64 | - For `DURATION_TRACE` and `SCREEN_TRACE` --- Length of time ("duration") from the beginning to the end of the trace - For `TRACE_METRIC` --- length of time ("duration") from the beginning to the end of the parent trace Unit: microsecond |
| trace_info.screen_info | RECORD | Only present for `SCREEN_TRACE` |
| trace_info.screen_info.slow_frame_ratio | float64 | Ratio of slow frames for this screen trace, between 0 and 1 (for example, a value of 0.05 means 5% of the frames for this screen instance took more than 16ms to render) |
| trace_info.screen_info.frozen_frame_ratio | float64 | Ratio of frozen frames for this screen trace, between 0 and 1 (for example, a value of 0.05 means 5% of the frames for this screen instance took more than 700ms to render) |
| trace_info.metric_info | RECORD | Only present for `TRACE_METRIC` |
| trace_info.metric_info.metric_value | int64 | Value of the trace metric |
| network_info | RECORD | Only present for `NETWORK_REQUEST` |
| network_info.response_code | int64 | HTTP response code for the network response (for example, 200, 404) |
| network_info.response_mime_type | string | MIME type of the network response (for example, "text/html") |
| network_info.request_http_method | string | HTTP method of the network request (for example, "GET" or "POST") |
| network_info.request_payload_bytes | int64 | Size of the network request payload Unit: byte |
| network_info.response_payload_bytes | int64 | Size of the network response payload Unit: byte |
| network_info.request_completed_time_us | int64 | Microseconds after `event_timestamp` when network request sending is complete Unit: microsecond |
| network_info.response_initiated_time_us | int64 | Microseconds after `event_timestamp` when network response is initiated Unit: microsecond |
| network_info.response_completed_time_us | int64 | Microseconds after `event_timestamp` when network response is completed Unit: microsecond |

## What can you do with the exported data?

The following sections offer examples of queries that you can run in
BigQuery against your exported Performance Monitoring data.

### Match the data seen on the console

The Firebase dashboard aggregates daily data in `America/Los_Angeles` timezone.
To match what was seen on the console, date functions should explicitly set
`America/Los_Angeles` as the timezone otherwise the date function will
[default to using UTC](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions#date).

```
SELECT
  DATE(event_timestamp, 'America/Los_Angeles') AS daily_date,
  APPROX_QUANTILES(trace_info.duration_us, 100)[OFFSET(90)] / 1000000 AS p90_seconds,
FROM `TABLE_NAME`
WHERE
  DATE(event_timestamp, 'America/Los_Angeles')
    >= DATE_SUB( PARSE_DATE('%Y%m%d', 'YYYY-MM-DD'), INTERVAL 7 DAY)
  AND DATE(event_timestamp, 'America/Los_Angeles')
    <= PARSE_DATE('%Y%m%d', 'YYYY-MM-DD')
  AND event_name = '_app_start'
GROUP BY 1
ORDER BY 1 DESC;
```

### View average app start latency break-down by country

```
SELECT AVG(trace_info.duration_us), country
FROM `TABLE_NAME`
WHERE _PARTITIONTIME > TIMESTAMP("YYYY-MM-DD")
AND event_type = "DURATION_TRACE"
AND event_name = "_app_start"
GROUP BY 2;
```

### Check the ratio of frozen frames against various conditions

For example, you can check the ratio of frozen frames alongside the amount of
time users spend on each screen of your app when on different radio types (WiFi,
4G, etc.).

```
SELECT
  AVG(trace_info.duration_us / 1000000) AS seconds_on_screen,
  AVG(trace_info.screen_info.frozen_frame_ratio) AS frozen_frame_ratio,
  event_name,
  radio_type
FROM `TABLE_NAME`
WHERE _PARTITIONTIME > TIMESTAMP("YYYY-MM-DD")
AND event_type = "SCREEN_TRACE"
GROUP BY event_name, radio_type
ORDER BY event_name, radio_type;
```

### Compute cache hit rate for loading certain types of files from disk

This analysis assumes that you instrumented a custom code trace for loading from
disk with a custom attribute named `file-extension` and a custom metric (a
`TRACE_METRIC`) named `cache-hit` that is set to `1` if cache hit and `0` if
cache miss.

For example, you can compute the cache hit rate for loading PNG files
from disk:

```
SELECT AVG(trace_info.metric_info.metric_value) AS cache_hit_rate
FROM `TABLE_NAME`
WHERE _PARTITIONTIME > TIMESTAMP("YYYY-MM-DD")
AND event_type = "TRACE_METRIC"
AND event_name = "cache-hit"
AND parent_trace_name = "loadFromDisk"
AND STRUCT("file-extension", "png") IN UNNEST(custom_attributes);
```

### Check for the time of day that users issue network requests

For example, you can check at what hour of the day users from the United States
issue network requests from your app:

```
SELECT
  count(1) AS hourly_count,
  EXTRACT(HOUR FROM event_timestamp) AS hour_of_day
FROM `TABLE_NAME`
WHERE _PARTITIONTIME > TIMESTAMP("YYYY-MM-DD")
AND event_type = "NETWORK_REQUEST"
AND country = "US"
GROUP BY 2 ORDER BY 2;
```

### Take your Performance Monitoring data anywhere

Sometimes you want to access your Performance Monitoring data server-side or push it to
another third-party solution. There is currently no charge for exporting data.

You can export your data by:

- Using the BigQuery web UI

- Running the CLI command
  [`bq extract`](https://cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_extract)

- Submitting an
  [extract job](https://cloud.google.com/bigquery/docs/reference/v2/jobs#configuration.extract)
  via the API or client libraries.

## Pricing

There is no charge for exporting data from Performance Monitoring, and BigQuery
provides generous no-cost usage limits. For detailed information, refer to
[BigQuery pricing](https://cloud.google.com/bigquery/pricing)
or the [BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox).