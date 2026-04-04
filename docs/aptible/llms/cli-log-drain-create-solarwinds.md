# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-log-drain-create-solarwinds.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible log_drain:create:solarwinds

This command lets you create a [Log Drain](/core-concepts/observability/logs/log-drains/overview) to forward your container logs to SolarWinds.

> 📘 Note

> Aptible supports sending logs to SolarWinds securely via Syslog+TLS. Add a new manual type destination in SolarWinds, and provide the syslog hostname and token when creating the log drain.

# Synopsis

```
Usage:
  aptible log_drain:create:solarwinds HANDLE --host SWO_HOSTNAME --token SWO_TOKEN --environment ENVIRONMENT [--drain-apps|--no-drain-apps] [--drain-databases|--no-drain-databases] [--drain-ephemeral-sessions|--no-drain-ephemeral-sessions] [--drain_proxies|--no-drain-proxies]

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

Create a SolarWinds Log Drain.  By default, App, Database, Ephemeral Session, and Proxy logs will be sent to your chosen destination.
```
