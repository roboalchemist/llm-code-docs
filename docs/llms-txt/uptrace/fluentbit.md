# Source: https://uptrace.dev/raw/ingest/logs/fluentbit.md

# Sending FluentBit logs to Uptrace

> Use Fluent Bit with the OpenTelemetry output to stream syslog data to Uptrace and tag records with custom labels.

[FluentBit](https://fluentbit.io/) is an open-source and multi-platform log processor and forwarder that allows you to collect data/logs from different sources, unify and filter them, and send them to multiple destinations.

## Configuration

To configure FluentBit to send logs to Uptrace, use the OpenTelemetry output and pass your project DSN via HTTP headers.

For example, to collect syslog messages, you can create the following FluentBit config:

```shell
[SERVICE]
    Flush         3
    Log_level     info
    Parsers_File  /etc/fluent-bit/parsers.conf

[INPUT]
    Name         Tail
    Path         /var/log/syslog
    Path_Key     log_file
    DB           /run/fluent-bit-messages.state
    Parser       syslog-rfc3164

[OUTPUT]
    Name                 opentelemetry
    Match                *
    Host                 api.uptrace.dev
    Port                 443
    Header               uptrace-dsn <FIXME>
    Compress             gzip
    Metrics_uri          /v1/metrics
    Logs_uri             /v1/logs
    Traces_uri           /v1/traces
    Log_response_payload True
    Tls                  On
    Tls.verify           Off
    # add user-defined labels
    add_label            service.name myservice
    add_label            log.source fluent-bit
```

Copy the config above to `fluent-bit.conf` and then start FluentBit:

```shell
fluent-bit -c fluent-bit.conf
```

## See also

- [Vector Logs](/ingest/logs/vector)
- [Monitoring Logs](/get/logs)
- [Structured Logging](/glossary/structured-logging)
- [OpenTelemetry Logs](/opentelemetry/logs)
