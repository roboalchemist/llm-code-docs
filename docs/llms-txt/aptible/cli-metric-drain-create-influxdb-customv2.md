# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-metric-drain-create-influxdb-customv2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible metric_drain:create:influxdb:customv2

This command lets you create a [Metric Drain](/core-concepts/observability/metrics/metrics-drains/overview) to forward your container metrics to an InfluxDB v2 database hosted outside Aptible.

> 📘 This command is for InfluxDB v2 destinations, which use organizations, buckets, and tokens for authentication. For InfluxDB v1 (which uses databases, usernames, and passwords), use [metric\_drain:create:influxdb:custom](/reference/aptible-cli/cli-commands/cli-metric-drain-create-influxdb-custom).

# Synopsis

```
Usage:
  aptible metric_drain:create:influxdb:customv2 HANDLE --org ORGANIZATION --token INFLUX_TOKEN --url URL_INCLUDING_PORT --bucket INFLUX_BUCKET_NAME --environment ENVIRONMENT

Options:
  [--bucket=BUCKET]
  [--org=ORG]
  [--token=TOKEN]
  [--url=URL]
  --env, [--environment=ENVIRONMENT]
```

# Examples

```bash  theme={null}
aptible metric_drain:create:influxdb:customv2 my-influxdb-v2-drain \
  --org my-org \
  --token my-influxdb-auth-token \
  --url https://influxdb.example.com:8086 \
  --bucket production-metrics \
  --environment production
```

# Related Commands

* [aptible metric\_drain:list](/reference/aptible-cli/cli-commands/cli-metric-drain-list) - List all metric drains
* [aptible metric\_drain:create:influxdb](/reference/aptible-cli/cli-commands/cli-metric-drain-create-influxdb) - Create a metric drain for InfluxDB hosted on Aptible
* [aptible metric\_drain:create:influxdb:custom](/reference/aptible-cli/cli-commands/cli-metric-drain-create-influxdb-custom) - Create a metric drain for external InfluxDB v1
* [aptible metric\_drain:deprovision](/reference/aptible-cli/cli-commands/cli-metric-drain-deprovision) - Remove a metric drain
