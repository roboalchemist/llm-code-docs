# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-metric-drain-create-influxdb-custom.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible metric_drain:create:influxdb:custom

This command lets you create a [Metric Drain](/core-concepts/observability/metrics/metrics-drains/overview) to forward your container metrics to an InfluxDB database hosted outside Aptible.

> 📘 Only InfluxDB v1 destinations are supported.

# Synopsis

```
Usage:
  aptible metric_drain:create:influxdb:custom HANDLE --username USERNAME --password PASSWORD --url URL_INCLUDING_PORT --db INFLUX_DATABASE_NAME --environment ENVIRONMENT

Options:
  [--db=DB]
  [--username=USERNAME]
  [--password=PASSWORD]
  [--url=URL]
  --env, [--environment=ENVIRONMENT]
```
