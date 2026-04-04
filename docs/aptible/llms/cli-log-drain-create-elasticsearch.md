# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-log-drain-create-elasticsearch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible log_drain:create:elasticsearch

This command lets you create a [Log Drain](/core-concepts/observability/logs/log-drains/overview) to forward your container logs to an [Elasticsearch Database](/core-concepts/managed-databases/supported-databases/elasticsearch) hosted on Aptible.

> 📘 You must choose a destination Elasticsearch Database that is within the same Environment as the Log Drain you are creating.

# Synopsis

```
Usage:
  aptible log_drain:create:elasticsearch HANDLE --db DATABASE_HANDLE --environment ENVIRONMENT [--drain-apps true/false] [--drain_databases true/false] [--drain_ephemeral_sessions true/false] [--drain_proxies true/false]

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
  [--db=DB]
  [--pipeline=PIPELINE]
```
