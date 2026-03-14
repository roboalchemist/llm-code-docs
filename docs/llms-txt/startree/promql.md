# Source: https://docs.startree.ai/corecapabilities/query_data/query_languages/promql.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PromQL

> Query metrics data using the Prometheus Query Language (PromQL).

PromQL support is built as a plugin on top of Apache Pinot's Time Series Engine, which is specifically designed to handle time series workloads efficiently. This integration allows you to:

* Use familiar Prometheus-style queries while leveraging Pinot's scalable analytics capabilities.
* Query high-cardinality time series data efficiently.
* Take advantage of StarTree Cloud optimized storage and indexing.

The [Time Series Engine](https://docs.pinot.apache.org/basics/releases/1.3.0#timeseries-engine-support-in-pinot-design-doc) in Pinot provides a pluggable framework that enables native support for various time-series query languages like PromQL. This engine is purpose-built for observability use cases and optimized for processing time series data in a more efficient way than traditional SQL queries.

<Note>
  The Time Series Engine and PromQL support in StarTree Cloud are currently in an alpha release.
</Note>

## Prerequisites

Before querying metrics with PromQL, ensure you have:

* A running Pinot cluster.
* Metrics data ingested into tables using the [Prometheus message decoder](/corecapabilities/ingestdata/adv-concepts/realtime/decoders/prometheus).

## Configuration

No additional configuration is required to enable TSE or PromQL. The Time Series Engine and PromQL support are enabled by default in StarTree Cloud.

The PromQL endpoint is available at `<Broker-endpoint>:8000/timeseries`. Supported PromQL queries can be executed on this endpoint - see [Supported PromQL Expressions](#supported-promql-expressions) for details.

## Data Ingestion Using Real-time Tables

<Warning>
  The Prometheus Message Decoder is only supported with REALTIME tables in StarTree Cloud. It cannot be used with OFFLINE tables.
</Warning>

To ingest Prometheus metrics data in real-time, you'll need to configure both the schema and table configuration properly. The Prometheus Message Decoder expects data in the following format:

```
<metric_name>{<label1>=<value1>,<label2>=<value2>,...} <metric_value> <timestamp>
```

### Required Schema Configuration

Your schema must include these specific fields with the exact names and data types:

| Field    | Type      | Description                                    |
| -------- | --------- | ---------------------------------------------- |
| `metric` | STRING    | Name of the Prometheus metric                  |
| `labels` | JSON      | Key-value pairs of Prometheus labels           |
| `value`  | DOUBLE    | The numeric value of the metric                |
| `ts`     | TIMESTAMP | Timestamp in milliseconds since the Unix epoch |

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/query_data/images/prometheus-schema.jpg?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=6443da136efaaab4c12ea6509f1d3235" alt="Table Schema" width="2972" height="1160" data-path="corecapabilities/query_data/images/prometheus-schema.jpg" />

### Table Configuration

For real-time ingestion, configure your table with the Prometheus Message Decoder:

1. Set the table type to `REALTIME`
2. Configure the stream settings to use `PrometheusMessageDecoder`
3. Set appropriate flush thresholds for your use case

   <img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/query_data/images/prometheus-table-config.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=915d78b2e9588bd525fc1d1001d408db" alt="Table Configuration" width="3036" height="1856" data-path="corecapabilities/query_data/images/prometheus-table-config.png" />

### Sample Data Format

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/query_data/images/prometheus-sample-data.jpg?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=f3898842c471bb08fad687c96973ab0a" alt="Sample Data" width="2994" height="1630" data-path="corecapabilities/query_data/images/prometheus-sample-data.jpg" />

### Important Considerations

1. The schema field names (`metric`, `labels`, `value`, `ts`) must match exactly as specified.
2. If you need different field names, use transform functions to alias them.
3. The timestamp must be in milliseconds since Unix epoch.
4. The labels field must be properly formatted JSON.

For more information, see [Prometheus Message Decoder](/corecapabilities/ingestdata/adv-concepts/realtime/decoders/prometheus).

## How to Query PromQL Data

There are two main ways to query PromQL data in Pinot:

### 1. Grafana Pinot Plugin

You can query PromQL data using the Grafana Pinot plugin:

1. Install the Grafana Pinot plugin.
2. Configure your Pinot data source in Grafana.

   <img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/query_data/images/configure-pinot-promql.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=bf1379bdb68d27b3333a22992c87a7b7" alt="Configure Pinot in Grafana" width="1998" height="1092" data-path="corecapabilities/query_data/images/configure-pinot-promql.png" />
3. Use the PromQL query editor in your Grafana dashboards.

   <img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/query_data/images/promql-query-grafana.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=6b436532e5fcc43de701dac57dda7f2e" alt="Grafana PromQL Query Editor" width="2426" height="1562" data-path="corecapabilities/query_data/images/promql-query-grafana.png" />

### 2. REST API Endpoints

You can query PromQL data using timeseries endpoint:

#### PromQL API endpoint

```bash  theme={null}
curl "http://localhost:8000/timeseries/api/v1/query_range" \
  -G \
  --data-urlencode "query=http_in_flight_requests" \
  --data-urlencode "start=1741011820" \
  --data-urlencode "end=1741021820" \
  --data-urlencode "step=30" \
  --data-urlencode "language=promql" \
  --data-urlencode "table=prometheusMsg_REALTIME"
```

Parameters explained:

* `query`: The PromQL expression to evaluate.
* `start`: Start timestamp in Unix epoch seconds.
* `end`: End timestamp in Unix epoch seconds.
* `step`: Query resolution in seconds (interval between data points).
* `language`: Query language type (promql).
* `table`: Pinot table name containing the metrics data.

## Supported PromQL Expressions

### Series Selectors

* Query Example: `http_requests_total`
* Description: Selects time series that match the given metric name.
* Usage: To retrieve multiple time series.

### Label Matching and Filtering

* Query Examples:

  ```promql  theme={null}
  http_requests_total{method="GET", status="200"}
  http_requests_total{method="GET", status="200"}[5m]
  ```

* Operators: `=`, `!=`, `=~` (regex match), `!~` (regex not match).
* Usage: To narrow down queries to specific metrics or labels.

### Offset

* Query Example: `http_requests_total offset 10m`
* Description: Shifts the time series back or forward in time.
* Usage: To compare current data with past data.

### Functions

* Supported Functions:
  * Rate: `rate(http_requests_total[5m])`
  * Increase: `increase(http_requests_total[5m])`
  * Delta: `delta(http_requests_total[5m])`
  * Instant Rate: `irate(http_requests_total[5m])`
* Usage: To compute rates, changes, and other complex calculations.

### Aggregation Operators

* Supported operators:
  * Sum: `sum(http_requests_total)`
  * AVG: `avg(http_requests_total)`
  * MAX: `max(http_requests_total)`
  * MIN: `min(http_requests_total)`
  * Count: `count(http_requests_total)`
  * Topk: `topk(1, http_requests_total)`
  * Bottom: `bottomk(2, http_requests_total)`
* Usage: To calculate sums, averages, and other metrics across multiple time series.

### By and Without Operators

* Examples:

  ```promql  theme={null}
  sum(http_requests_total) by (status)
  sum(http_requests_total) without(job)
  ```

* Description: Apply aggregation operator by or without labels.

### Binary Operators

* Supported operators: `+`, `-`, `*`, `/`
* Examples:

  ```promql  theme={null}
  http_requests_total / http_requests_failed
  http_requests_total - http_requests_failed
  ```

* Usage: To combine multiple series mathematically.

For detailed information about these operators and functions, please refer to the [Prometheus Query Language Documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/).

<Note>
  Only the operators and functions listed above are supported in Pinot, which is a subset of all Prometheus functions and operators.
</Note>

Built with [Mintlify](https://mintlify.com).
