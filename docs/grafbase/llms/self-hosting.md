# Source: https://grafbase.com/docs/platform/self-hosting.md

# Grafbase Enterprise Platform

Grafbase Enterprise Platform is a self-hosted version of the Grafbase platform, which is suitable for enterprises that are subject to regulatory compliance. It runs in your infrastructure and is governed by your own access and security controls.

<Image 
  src="/images/docs/ep/enterprise-platform-diagram.png" 
  alt="Grafbase Enterprise Platform Diagram"
  width={828}
  height={591}
/>

## Architecture

The Grafbase Enterprise Platform is composed of the following components:

- **Grafbase API**: The management API of the platform.
- **Grafbase Dashboard**: Web-based interface to manage graphs and access analytics.
- **Telemetry Sink**: Collects telemetry data from the Grafbase Gateway and writes it to Kafka.
- **Object Storage**: A small service that sits in front of an S3-compatible bucket to serve schemas and trusted documents with authentication and authorization.

In addition to these components, Grafbase Enterprise Platform requires the following services:

- **Postgres**: Database that contains core platform data.
- **ClickHouse**: Database that contains analytics data.
- **Zitadel**: Authentication management to manage users and permissions.
- **MinIO**: Storage provider to store published schemas and trusted documents. MinIO is optional, you can plug in any S3-compatible object storage.
- **Kafka**: Message broker to handle real-time telemetry data.
- **OpenTelemetry Collector**: Aggregates telemetry data from Kafka to ClickHouse.

## Helm Charts

The Grafbase Enterprise Platform is distributed via Helm charts that can be installed on any Kubernetes cluster. The Helm charts let you to decide which components you want from the Enterprise Platform.

To get access to the Helm charts please [contact us](/contact) and we will provide you with the necessary credentials.