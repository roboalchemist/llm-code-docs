# Source: https://docs.datadoghq.com/agent/troubleshooting/debug_mode.md

---
title: Debug Mode
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Agent > Agent Troubleshooting > Debug Mode
source_url: https://docs.datadoghq.com/troubleshooting/debug_mode/index.html
---

# Debug Mode

## Overview{% #overview %}

The Agent, by default, logs in `INFO` level. You can set the log level to `DEBUG` to get more information from your logs.

**Note**: Debug mode is meant for debugging purposes only. Datadog recommends only enabling `DEBUG` for a certain window of time as it increases the number of indexed logs. Set the log level back to `INFO` when done.

To enable the Agent full debug mode:

1. Modify your local `datadog.yaml` file. See [Agent main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file) for OS specific details.

1. Replace `# log_level: INFO` with `log_level: DEBUG` (remove `#` to uncomment the line).

1. Restart the Datadog Agent. See [Agent Commands](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent) for OS specific details.

1. Wait a few minutes to generate some logs. See [Agent Log Files](https://docs.datadoghq.com/agent/configuration/agent-log-files/) for OS specific details.

## Containerized Agent{% #containerized-agent %}

To enable debug mode for the container Agent, use `DD_LOG_LEVEL=debug` when starting your Agent.

For Agent v6.19+ / v7.19+, set the Agent log level at runtime using:

```shell
agent config set log_level debug
```

You **cannot** change the log level for the trace-agent container at runtime like you can do for the agent container. A redeployment after setting `DD_LOG_LEVEL` variable to `debug` is still necessary for the dedicated trace-agent container.

If using [**Helm**](https://github.com/DataDog/helm-charts/blob/637472f105f42e8b444981ea2a38e955161c8e3a/charts/datadog/values.yaml#L125), replace `logLevel: INFO` with `logLevel: DEBUG` in your `datadog-values.yaml` file and re-deploy.

## Agent log level{% #agent-log-level %}

The following Agent log levels are available for `log_level` or `DD_LOG_LEVEL`:

| Option       | Critical logs | Error logs | Warn logs | Info logs | Debug logs | Trace logs |
| ------------ | ------------- | ---------- | --------- | --------- | ---------- | ---------- |
| `'OFF'`      |
| `'CRITICAL'` | yes           |
| `'ERROR'`    | yes           | yes        |
| `'WARN'`     | yes           | yes        | yes       |
| `'INFO'`     | yes           | yes        | yes       | yes       |
| `'DEBUG'`    | yes           | yes        | yes       | yes       | yes        |
| `'TRACE'`    | yes           | yes        | yes       | yes       | yes        | yes        |

**Note**: When setting the log level to `'OFF'` in the configuration file quotes are mandatory to prevent the value for being improperly parsed. Quotes are optional for other log levels.

## Further Reading{% #further-reading %}

- [Send an Agent Flare](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/)
- [Get the Status of an Agent Check](https://docs.datadoghq.com/agent/troubleshooting/agent_check_status/)
