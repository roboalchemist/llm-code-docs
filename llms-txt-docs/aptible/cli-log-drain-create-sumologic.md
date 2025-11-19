# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-log-drain-create-sumologic.md

# aptible log_drain:create:sumologic

This command lets you create a [Log Drain](/core-concepts/observability/logs/log-drains/overview) to forward your container logs to Sumo Logic.

> 📘 Note

> Create a new Hosted Collector in Sumo Logic using a HTTP source, then use provided the HTTP Source Address for the `--url` option.

# Synopsis

```
Usage:
  aptible log_drain:create:sumologic HANDLE --url SUMOLOGIC_URL --environment ENVIRONMENT [--drain-apps true/false] [--drain_databases true/false] [--drain_ephemeral_sessions true/false] [--drain_proxies true/false]

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

Create a Sumo Logic Drain
```
