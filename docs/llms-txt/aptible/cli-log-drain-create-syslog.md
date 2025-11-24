# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-log-drain-create-syslog.md

# aptible log_drain:create:syslog

This command lets you create a [Log Drain](/core-concepts/observability/logs/log-drains/overview) to forward your container logs to an [Syslog TCP+TLS destination](/core-concepts/observability/logs/log-drains/syslog-log-drains) of your choice.

> 📘 Note

> There are specific CLI commands for creating Log Drains for some specific Syslog destinations, such as [Papertrail](/reference/aptible-cli/cli-commands/cli-log-drain-create-papertrail).

# Synopsis

```
Usage:
  aptible log_drain:create:syslog HANDLE --host SYSLOG_HOST --port SYSLOG_PORT [--token TOKEN] --environment ENVIRONMENT [--drain-apps true/false] [--drain_databases true/false] [--drain_ephemeral_sessions true/false] [--drain_proxies true/false]

Options:
  [--host=HOST]
  [--port=PORT]
  [--token=TOKEN]
  [--drain-apps], [--no-drain-apps]
                                                                 # Default: true
  [--drain-databases], [--no-drain-databases]
                                                                 # Default: true
  [--drain-ephemeral-sessions], [--no-drain-ephemeral-sessions]
                                                                 # Default: true
  [--drain-proxies], [--no-drain-proxies]
                                                                 # Default: true
  --env, [--environment=ENVIRONMENT]

Create a Papertrail Log Drain
```
