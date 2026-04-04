# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-log-drain-create-papertrail.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible log_drain:create:papertrail

This command lets you create a [Log Drain](/core-concepts/observability/logs/log-drains/overview) to forward your container logs to Papertrail.

> 📘 Note

> Add a new Log Destination in Papertrail (make sure to accept TCP + TLS connections and logs from unrecognized senders), then copy the host and port from the Log Destination.

# Synopsis

```
Usage:
  aptible log_drain:create:papertrail HANDLE --host PAPERTRAIL_HOST --port PAPERTRAIL_PORT --environment ENVIRONMENT [--drain-apps true/false] [--drain_databases true/false] [--drain_ephemeral_sessions true/false] [--drain_proxies true/false]

Options:
  [--host=HOST]
  [--port=PORT]
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
