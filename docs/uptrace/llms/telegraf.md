# Source: https://uptrace.dev/raw/ingest/telegraf.md

# Ingesting Telegraf metrics

> Output Telegraf metrics through the OpenTelemetry plugin, secure connections, and add resource attributes before sending to Uptrace.

If you're using [Telegraf](https://github.com/influxdata/telegraf) 1.20.0+ to collect metrics, you can ingest them to Uptrace using the [OpenTelemetry](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/opentelemetry/README.md) output plugin:

```toml
[[outputs.opentelemetry]]
  service_address = "api.uptrace.dev:4317"

  ## Optional TLS Config.
  ##
  ## Root certificates for verifying server certificates encoded in PEM format.
  # tls_ca = "/etc/telegraf/ca.pem"
  ## The public and private key pairs for the client encoded in PEM format.
  ## May contain intermediate certificates.
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS, but skip TLS chain and host verification.
  # insecure_skip_verify = false
  ## Send the specified TLS server name via SNI.
  # tls_server_name = "foo.example.com"

  [outputs.opentelemetry.headers]
  uptrace-dsn = "<FIXME>"

  ## Additional OpenTelemetry resource attributes
  # [outputs.opentelemetry.attributes]
  # "service.name" = "demo"
```
