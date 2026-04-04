# Source: https://console.groq.com/docs/prometheus-metrics

---
description: Explore the Prometheus metrics available to your Groq Organization.
title: Prometheus Metrics - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Prometheus Metrics

[Prometheus](https://prometheus.io/) is an open-source monitoring system that collects and stores metrics as time series data. Its [stable API](https://prometheus.io/docs/prometheus/latest/querying/api/) is compatible with a range of systems and tools like [Grafana](https://grafana.com/oss/grafana).

## [Enterprise Feature](#enterprise-feature)

This feature is only available to our Enterprise tier customers. To get started, please reach out to [our Enterprise team](https://groq.com/enterprise-access).

## [APIs](#apis)

Groq exposes Prometheus metrics about your organization's usage through [VictoriaMetrics](https://victoriametrics.com/). It [supports](https://docs.victoriametrics.com/victoriametrics/#prometheus-querying-api-usage) most Prometheus querying API paths:

* `/api/v1/query`
* `/api/v1/query_range`
* `/api/v1/series`
* `/api/v1/labels`
* `/api/v1/label/<label_name>/values`
* `/api/v1/status/tsdb`

## [MetricsQL](#metricsql)

Prometheus queries against Groq endpoints use [MetricsQL](https://docs.victoriametrics.com/MetricsQL.html), a query language that extends Prometheus's native [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) query language.

## [Querying](#querying)

Queries can be sent to the following endpoint:

`https://api.groq.com/v1/metrics/prometheus` 

To Authenticate, you will need to provide your Groq API key as a header in the `Authorization: Bearer <your-api-key>` format.

## [Grafana](#grafana)

If you run Grafana, you can add Groq metrics as a Prometheus datasource:

1. Add a new Prometheus datasource in Grafana by navigating to Settings -> Data Sources -> Add data source -> Prometheus.
2. Enter the following URL under HTTP -> URL: `https://api.groq.com/v1/metrics/prometheus`
3. Set the `Authorization` header to your Groq API key:
* Go to Custom HTTP Headers -> Add Header  
   * Header: `Authorization`  
   * Value: `Bearer <your-api-key>`
1. Save & Test.

## [Available Metrics](#available-metrics)

All metrics are broken out by model and project id. Some metrics are broken out by status code and le (for use with histogram\_quantile). Metric names are prefixed with their labels and provided as rate5m (rate over a 5 minute window).

In addition to using the APIs directly, you can see a handful of curated charts directly in our console at [Metrics](https://console.groq.com/metrics/prometheus)

Groq provides the following metrics:

### [Request Metrics](#request-metrics)

* `model_project_id_status_code:requests:rate5m`

### [Token Metrics](#token-metrics)

* `le_model_project_id:tokens_in_bucket:rate5m`
* `le_model_project_id:tokens_out_bucket:rate5m`
* `model_project_id:tokens_in:rate5m`
* `model_project_id:tokens_out:rate5m `

### [Latency Metrics](#latency-metrics)

* `le_model_project_id:queue_latency_seconds_bucket:rate5m`  
   * Time from when a request is received until it begins processing. In addition to any time waiting, this is inclusive of time spent doing authorization, tokenization, etc., and internal network time between services so you should never expect this to be 0\. It is computed as first\_input\_token\_at - request\_start\_at
* `le_model_project_id:ttft_latency_seconds_bucket:rate5m`  
   * Time from when a request is received until the first token of output is generated.
* `le_model_project_id:e2e_latency_seconds_bucket:rate5m`  
   * Total time from when a request is received until the last token is streamed. If not streaming, TTFT and End-to-End latency are the same

### [Prompt Cache Metrics](#prompt-cache-metrics)

* `le_model_project_id:prompt_cache_hits_bucket:rate5m`
* `model_project_id:prompt_cache_hits:rate5m`
* `model_project_id:prompt_cache_misses:rate5m`

## [Examples](#examples)

Total requests across all models and projects:

`sum(model_project_id_status_code:requests:rate5m)` 

P99 E2E latency across all projects, for a specific model:

`histogram_quantile(0.99, sum by(le) (model_project_id:e2e_latency_seconds_bucket:rate5m{model="llama-3.1-8b-instant"}))`