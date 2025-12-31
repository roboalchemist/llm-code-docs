# Source: https://docs.vespa.ai/en/reference/api/prometheus-v1.html.md

# /prometheus/v1 API reference

 

The _prometheus node metrics API_ is available on each _node_ at the metrics proxy port, default _http://host:19092/prometheus/v1/values_.

This API has the same content as in _/metrics/v1/values_, in a [format](https://prometheus.io/docs/instrumenting/exposition_formats/) that can be scraped by [Prometheus](https://prometheus.io/docs/introduction/overview/).

Refer to [monitoring](/en/operations/self-managed/monitoring.html) for an overview of nodes, services and metrics APIs.

## HTTP requests

| HTTP request | prometheus/v1 operation | Description |
| --- | --- | --- |
| GET | 

 |
| | Node metrics | 

```
/prometheus/v1/values
```

See [monitoring](/en/operations/self-managed/monitoring.html#prometheus-v1-values) for examples.

 |

## Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| consumer | String | 

Specify response [consumer](../applications/services/admin.html#consumer), i.e. set of metrics. An unknown / empty value will return the `default` metric set. Built-in (note: case-sensitive):

- `default`
- `Vespa`

 |

## HTTP status codes

Non-exhaustive list of status codes:

| Code | Description |
| --- | --- |
| 200 | OK. |
 

## Response format

Responses are in Prometheus format, the values are the same as in [/metrics/v1/values](metrics-v1.html#metrics-v1-values)

 Copyright © 2025 - [Cookie Preferences](#)

