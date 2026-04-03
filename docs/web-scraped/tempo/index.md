# Grafana Tempo Documentation

Grafana Tempo is an open source, easy-to-use, and high-scale distributed tracing backend.

Source: https://github.com/grafana/tempo
Official Docs: https://grafana.com/docs/tempo/latest/

## Overview

Tempo is a distributed tracing backend that requires only object storage to operate. It's deeply integrated with Grafana, Prometheus, and Loki.

## Key Features

- **Simple Operation**: Uses only object storage for backend operations
- **Multi-tenancy**: Built for multi-tenancy from the ground up
- **High Scale**: Ingests up to 2 million spans/second
- **Cost Effective**: Reduce costs with trace sampling and aggregation
- **Deep Grafana Integration**: Query traces directly from metrics and logs
- **Protocol Agnostic**: Works with any trace protocol (Jaeger, Zipkin, OpenTelemetry, Kafka compatible)

## What is Distributed Tracing?

Distributed tracing helps teams quickly pinpoint performance issues and understand the flow of requests across services. The Traces Drilldown UI simplifies this process by offering a user-friendly interface to view and analyze trace data.

## Getting Started

See the [official Getting Started guide](https://grafana.com/docs/tempo/latest/getting-started/) for setup instructions.

## Main Sections

- **Architecture**: Understand Tempo's design and components
- **Configuration**: Configure Tempo for your environment
- **Setup & Deployment**: Deploy Tempo in various environments
- **Operations**: Operate and maintain Tempo
- **TraceQL**: Query language for traces
- **API**: REST API reference
- **CLI**: Command-line interface

## TraceQL

Tempo implements TraceQL, a traces-first query language inspired by LogQL and PromQL, which enables targeted queries or rich UI-driven analyses.

## Integrations

Tempo is compatible with:

- Jaeger
- Zipkin
- Kafka
- OpenTelemetry
- Prometheus
- Grafana Loki

## Storage Options

Tempo supports multiple storage backends:

- Azure Blob Storage
- Google Cloud Storage (GCS)
- Amazon S3
- Local disk

## Community

- [GitHub Repository](https://github.com/grafana/tempo)
- [Slack Channel](https://grafana.slack.com/archives/C01D981PEE5)
- [Community Forum](https://community.grafana.com/c/grafana-tempo/40)
- License: AGPL-3.0
