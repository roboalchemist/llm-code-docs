# Source: https://docs.mage.ai/observability/external/prometheus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring with Prometheus

## Enable Prometheus

You will need to add `ENABLE_PROMETHEUS` environment variable as `true` in order to
enable Prometheus style metrics on the \<BASE\_PATH>/metrics route.

## Prometheus metrics

When enabled, Mage will publish Metrics for the HTTP Server (Tornado) as well as for
the Python Runtime. The /metrics route will be updated on-demand to respond to scrape requests.


Built with [Mintlify](https://mintlify.com).