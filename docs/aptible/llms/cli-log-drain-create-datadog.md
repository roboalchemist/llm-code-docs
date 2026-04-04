# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-log-drain-create-datadog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible log_drain:create:datadog

This command lets you create a [Log Drain](/core-concepts/observability/logs/log-drains/overview) to forward your Container logs to Datadog.

> 📘 The `--url` option must be in the format of `https://http-intake.logs.datadoghq.com/v1/input/<DD_API_KEY>`. Refer to [https://docs.datadoghq.com/logs/log\_collection](https://docs.datadoghq.com/logs/log_collection) for more options.

> Please note, Datadog's documentation defaults to v2. Please use v1 Datadog documentation with Aptible.

# Synopsis

```
Usage:
  aptible log_drain:create:datadog HANDLE --url DATADOG_URL --environment ENVIRONMENT [--drain-apps true/false] [--drain_databases true/false] [--drain_ephemeral_sessions true/false] [--drain_proxies true/false]

Options:
  [--drain-apps], [--no-drain-apps]
                                                                 # Default: true
  [--drain-databases], [--no-drain-databases]
                                                                 # Default: true
  [--drain-ephemeral-sessions], [--no-drain-ephemeral-sessions]
                                                                 # Default: true
  [--drain-proxies], [--no-drain-proxies]
                                                                 # Default: true
  --env, [--environment=ENVIRONMENT]
  [--url=URL]
```
