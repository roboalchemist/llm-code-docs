# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-metric-drain-create-datadog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible metric_drain:create:datadog

This command lets you create a [Metric Drain](/core-concepts/observability/metrics/metrics-drains/overview) to forward your container metrics to [Datadog](/core-concepts/integrations/datadog).

You need to use the `--site` option to specify the [Datadog Site](https://docs.datadoghq.com/getting_started/site/) associated with your Datadog account. Valid options are `US1`, `US3`, `US5`, `EU1`, or `US1-FED`

# Synopsis

```
Usage:
  aptible metric_drain:create:datadog HANDLE --api_key DATADOG_API_KEY --site DATADOG_SITE --environment ENVIRONMENT

Options:
  [--api-key=API_KEY]
  [--site=SITE]
  --env, [--environment=ENVIRONMENT]
```
