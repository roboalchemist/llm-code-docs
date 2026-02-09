# Source: https://docs.datadoghq.com/containers/monitoring.md

# Source: https://docs.datadoghq.com/cloudprem/operate/monitoring.md

---
title: Monitor CloudPrem
description: Learn how to monitor specific metrics for your CloudPrem deployment
breadcrumbs: Docs > CloudPrem > Operate CloudPrem > Monitor CloudPrem
---

# Monitor CloudPrem

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Dashboards{% #dashboards %}

CloudPrem provides an out-of-the-box dashboard that monitors CloudPrem's key metrics.

### Setup{% #setup %}

These metrics are exported by [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/?tab=hostagent). You can either:

- Run DogStatsD as a standalone service, or
- Run the Datadog Agent (which includes DogStatsD by default)

Configure either option with your organization's API key to export these metrics. As soon as your CloudPrem cluster is connected to Datadog, the OOTB dashboard is automatically created, and you can access it from your [Dashboards list](https://app.datadoghq.com/dashboard/lists?q=cloudprem&p=1).

{% alert level="info" %}
To display distribution metrics on your dashboard, you must [enable advanced query functionality](https://docs.datadoghq.com/metrics/distributions/#enabling-advanced-query-functionality).
{% /alert %}

### Data Collected{% #data-collected %}

| Metric                                                   | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- |
| **indexed\_events.count**(Counter)                       | Number of indexed events                                 |
| **indexed\_events\_bytes.count**(Counter)                | Number of indexed bytes                                  |
| **ingest\_requests.count**(Counter)                      | Number of ingest requests                                |
| **ingest\_requests.duration\_seconds**(Histogram)        | Ingest request latency                                   |
| **object\_storage\_delete\_requests.count**(Counter)     | Number of delete requests on object storage              |
| **object\_storage\_get\_requests.count**(Counter)        | Number of get requests on object storage                 |
| **object\_storage\_get\_requests\_bytes.count**(Counter) | Total bytes read from object storage using GET requests  |
| **object\_storage\_put\_requests.count**(Counter)        | Number of PUT requests on object storage                 |
| **object\_storage\_put\_requests\_bytes.count**(Counter) | Total bytes written to object storage using PUT requests |
| **pending\_merge\_ops.gauge**(Gauge)                     | Number of pending merge operations                       |
| **search\_requests.count**(Counter)                      | Number of search requests                                |
| **search\_requests.duration\_seconds**(Histogram)        | Search request latency                                   |
| **metastore\_requests.count**(Counter)                   | Number of metastore requests                             |
| **metastore\_requests.duration\_seconds**(Histogram)     | Metastore request latency                                |
| **cpu.usage.gauge**(Gauge)                               | CPU usage percentage                                     |
| **uptime.gauge**(Gauge)                                  | Service uptime in seconds                                |
| **memory.allocated\_bytes.gauge**(Gauge)                 | Allocated memory in bytes                                |
| **disk.bytes\_read.counter**(Counter)                    | Total bytes read from disk                               |
| **disk.bytes\_written.counter**(Counter)                 | Total bytes written to disk                              |
| **disk.available\_space.gauge**(Gauge)                   | Available disk space in bytes                            |
| **disk.total\_space.gauge**(Gauge)                       | Total disk capacity in bytes                             |
| **network.bytes\_recv.counter**(Counter)                 | Total bytes received over network                        |
| **network.bytes\_sent.counter**(Counter)                 | Total bytes sent over network                            |
