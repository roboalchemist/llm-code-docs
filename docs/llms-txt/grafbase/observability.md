# Source: https://grafbase.com/docs/platform/self-hosting/observability.md

# Source: https://grafbase.com/docs/gateway/observability.md

# Source: https://grafbase.com/docs/platform/self-hosting/observability.md

# Source: https://grafbase.com/docs/gateway/observability.md

# Source: https://grafbase.com/docs/platform/self-hosting/observability.md

# Source: https://grafbase.com/docs/gateway/observability.md

# Source: https://grafbase.com/docs/platform/self-hosting/observability.md

# Source: https://grafbase.com/docs/gateway/observability.md

# Observability in the Grafbase Gateway

The Grafbase Gateway lets you monitor gateway operations and errors through logs, traces, and metrics. When you use the gateway with a Grafbase access token, the Grafbase dashboard receives gateway operation analytics automatically.

The gateway also supports sending monitoring data to endpoints that implement [OpenTelemetry](https://opentelemetry.io/) protocols. You can combine gateway traces with other services in your platform, and access more metrics beyond what the Grafbase dashboard currently shows.

## Logs

The Grafbase Gateway provides logs for monitoring gateway operations and errors. By default, it outputs logs to standard output. Additionally, the gateway can send monitoring data to an endpoint that implements the [OpenTelemetry](https://opentelemetry.io/) protocols.

### Level of Produced Information

You can define the level of information by setting the log level command line argument:

```bash
--log <LOG_LEVEL>
    Set the logging level, this applies to all spans, logs and trace events.

    Beware that *only* 'off', 'error', 'warn' and 'info' can be used safely in
    production. More verbose levels, such as 'debug', will include sensitive
    information like request variables, responses, etc.

    Possible values are: 'off', 'error', 'warn', 'info', 'debug', 'trace' or a
    custom string. In the last case, the string is passed on to
    [`tracing_subscriber::EnvFilter`] as is and is only meant for debugging
    purposes. No stability guarantee is made on the format.

    [env: GRAFBASE_LOG=]
    [default: info]
```

This setting affects both traces and logs. The default level is `info`. `debug` and `trace` will include sensitive details and should not be used in production.

The `error` or `off` levels affect all traces and spans at `info` level. If you want to silence all logs but still export them along with traces and metrics to an OpenTelemetry endpoint, direct standard output and standard error to `/dev/null`.

### System Logs

By default, the system outputs logs to standard output. Logs can appear in two different formats:

```bash
--log-style <LOG_STYLE>
    Set the style of log output

    [env: GRAFBASE_LOG_STYLE=]
    [default: pretty]

    Possible values:
    - pretty: Pretty printed logs, used as the default in the terminal
    - text:   Standard text, used as the default when piping stdout to a file
    - json: JSON objects
```

The default style is `pretty`, inside a terminal, which provides ANSI-colored text for terminal output and a human-friendly formatting. When piping to a file, `text` will be used instead.The `json` format delivers logs in JSON format, which can be useful if the logging platform supports structured data.

### Access Logs

The Grafbase Gateway can log access requests. Read more on the [access logs feature](https://grafbase.com/docs/gateway/security/access-logs.md) and configuring them in the [gateway configuration](https://grafbase.com/docs/gateway/configuration/gateway.md).

### Logging into an OpenTelemetry Endpoint

The Grafbase Gateway can send logs to an OpenTelemetry endpoint. To enable this feature, either define the global telemetry endpoint or an endpoint for the logs exporter. Read more about the [OpenTelemetry configuration](https://grafbase.com/docs/gateway/configuration/telemetry.md).

## Traces

Grafbase Gateway monitors the request lifecycle by providing traces. Add a valid access token in the `GRAFBASE_ACCESS_TOKEN` environment variable to automatically send traces to the Grafbase Dashboard or Grafbase Enterprise platform.

The dashboard displays only traces from the Grafbase Gateway. Configure a different OpenTelemetry endpoint in the configuration file to send traces elsewhere. A third-party telemetry platform lets you [propagate traces](https://grafbase.com/docs/gateway/configuration/telemetry.md) from the gateway with other services in your platform. Traces provide information on the request lifecycle and send data to the OpenTelemetry endpoint from the `info` level.

Read more about the [telemetry configuration](https://grafbase.com/docs/gateway/configuration/telemetry.md) and [tracing spans and attributes](https://grafbase.com/docs/gateway/telemetry/tracing-attributes.md).

## Metrics

The Grafbase Gateway delivers metrics for requests and operations to an OpenTelemetry endpoint. Metrics include counters, histograms, and gauges at various points in the system.

To automatically send metrics to the Grafbase Dashboard or Grafbase Enterprise platform, add a valid access token in the `GRAFBASE_ACCESS_TOKEN` environment variable. [Configure an additional OpenTelemetry exporter](https://grafbase.com/docs/gateway/configuration/telemetry.md) in the configuration file to send metrics to other destinations.

The [metrics reference](https://grafbase.com/docs/gateway/telemetry/metrics-attributes.md) lists all metrics and their attributes.