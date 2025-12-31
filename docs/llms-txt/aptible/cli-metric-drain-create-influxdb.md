# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-metric-drain-create-influxdb.md

# aptible metric_drain:create:influxdb

This command lets you create a [Metric Drain](/core-concepts/observability/metrics/metrics-drains/overview) to forward your container metrics to an [InfluxDB Database](/core-concepts/managed-databases/supported-databases/influxdb) hosted on Aptible.

> 📘 You must choose a destination InfluxDB Database that is within the same Environment as the Metric Drain you are creating.

# Synopsis

```
Usage:
  aptible metric_drain:create:influxdb HANDLE --db DATABASE_HANDLE --environment ENVIRONMENT

Options:
  [--db=DB]
  --env, [--environment=ENVIRONMENT]
```
