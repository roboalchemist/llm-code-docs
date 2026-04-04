# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-log-drain-create-https.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible log_drain:create:https

This command lets you create a [Log Drain](/core-concepts/observability/logs/log-drains/overview) to forward your container logs to an [HTTPS destination](/core-concepts/observability/logs/log-drains/https-log-drains) of your choice.

> 📘 There are specific CLI commands for creating Log Drains for some specific HTTPS destinations, such as [Datadog](/reference/aptible-cli/cli-commands/cli-log-drain-create-datadog), [LogDNA](/reference/aptible-cli/cli-commands/cli-log-drain-create-logdna), and [SumoLogic](/reference/aptible-cli/cli-commands/cli-log-drain-create-sumologic).

# Synopsis

```
Usage:
  aptible log_drain:create:https HANDLE --url URL --environment ENVIRONMENT [--drain-apps true/false] [--drain_databases true/false] [--drain_ephemeral_sessions true/false] [--drain_proxies true/false]

Options:
  [--url=URL]
  [--drain-apps], [--no-drain-apps]
                                                                 # Default: true
  [--drain-databases], [--no-drain-databases]
                                                                 # Default: true
  [--drain-ephemeral-sessions], [--no-drain-ephemeral-sessions]
                                                                 # Default: true
  [--drain-proxies], [--no-drain-proxies]
                                                                 # Default: true
  --env, [--environment=ENVIRONMENT]
```
