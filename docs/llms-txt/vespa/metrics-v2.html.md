# Source: https://docs.vespa.ai/en/reference/api/metrics-v2.html.md

# /metrics/v2 API reference

 

The _application metrics API_ is available on each _node_ at the metrics proxy port, default _http://host:19092/metrics/v2/values_. A container service on the same node as the metrics proxy might forward _/metrics/v2/values_ on its own port, normally 8080.

_/metrics/v2/values_ is an aggregation of the application instance nodes _/metrics/v1/values_. Refer to [monitoring](/en/operations/self-managed/monitoring.html) for an overview of nodes, services and metrics APIs.

## HTTP requests

| HTTP request | metrics/v2 operation | Description |
| --- | --- | --- |
| GET | 

 |
| | Application metrics | 

```
/metrics/v2/values
```

See [monitoring](/en/operations/self-managed/monitoring.html#metrics-v2-values) for examples.

 |

## Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| consumer | String | 

Specify response [consumer](../applications/services/admin.html#consumer), i.e. set of metrics. See [metrics/v1](metrics-v1.html#consumer) for details.

 |

## HTTP status codes

Non-exhaustive list of status codes:

| Code | Description |
| --- | --- |
| 200 | OK. |
 

## Response format

Responses are in JSON format, with the following fields:

| Element | Parent | Type | Description |
| --- | --- | --- | --- |
| 

nodes

 | | Array | Root element for /metrics/v2/values. Returns an array of node objects with metrics |
| 

hostname

 | nodes | String | Node hostname. |
| 

role

 | nodes | String | Node role. |
| 

services

 | nodes | Array | Array of service objects, the are services running on the node. The `service` object is defined in [/metrics/v1/values](metrics-v1.html#metrics-v1-values). |

 Copyright © 2026 - [Cookie Preferences](#)

