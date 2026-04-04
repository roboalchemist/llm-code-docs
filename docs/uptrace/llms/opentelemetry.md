# Source: https://uptrace.dev/raw/opentelemetry.md

# Source: https://uptrace.dev/raw/ingest/opentelemetry.md

# Ingesting telemetry using OpenTelemetry Distros for Uptrace

> Configure OpenTelemetry SDKs in any language with an Uptrace DSN over OTLP gRPC or HTTP.

Uptrace uses OpenTelemetry protocol (OTLP) to receive telemetry data such as [traces](/opentelemetry/distributed-tracing#spans), [metrics](/opentelemetry/metrics), and [logs](/opentelemetry/logs). Uptrace supports both OTLP/gRPC and OTLP/HTTP.

To start sending data to Uptrace, you need to configure OpenTelemetry SDK for your programming language using an Uptrace DSN.

Uptrace DSN (Data Source Name) is a connection string that is used to connect and send data to an Uptrace backend. It contains a backend address (host:port) and a secret token that grants access to a project.

You can find your project DSN on the Project Settings page:

![Uptrace DSN](/get/dsn.png)

Once you have a DSN, follow instructions for your programming language:

<home-distro-list>



</home-distro-list>
