# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-log-drain-create-logdna.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible log_drain:create:logdna

This command lets you create a [Log Drain](/core-concepts/observability/logs/log-drains/overview) to forward your container logs to LogDNA.

> 📘 The `--url` options must be given in the format of `https://logs.logdna.com/aptible/ingest/<INGESTION KEY>`. Refer to [https://docs.logdna.com/docs/aptible-logs](https://docs.logdna.com/docs/aptible-logs) for more options.

# Synopsis

```
Usage:
  aptible log_drain:create:logdna HANDLE --url LOGDNA_URL --environment ENVIRONMENT [--drain-apps true/false] [--drain_databases true/false] [--drain_ephemeral_sessions true/false] [--drain_proxies true/false]

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
