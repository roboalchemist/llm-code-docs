# Source: https://docs.startree.ai/thirdeye/troubleshooting/thirdeye-observability-and-monitoring.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ThirdEye Observability and Monitoring

To check the health of ThirdEye, set up the following metrics to monitor:

| Category           | Metrics to be monitored                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Environment        | Environment availability                                                                                                                         |
| Scheduler          | Task stats                                                                                                                                       |
| Anomalies & alerts | Total number of anomalies created, number of anomalies created - grouped by metrics/datasets, number of notifications sent, number active alerts |
| Data               | Persistent data and storage, queries per second (using Pinot broker) (executed from alerts), connectivity with Pinot                             |
| Availability       | TP95, API availability and latency, Swagger API is up and working, TE-Auth server connectivity check                                             |
| Usage              | DAU and MAU, API calls                                                                                                                           |

Built with [Mintlify](https://mintlify.com).
