# Source: https://opentelemetry.io/docs/collector/registry/

Title: Registry

URL Source: https://opentelemetry.io/docs/collector/registry/

Markdown Content:
Docs
Ecosystem
Status
Community
Training
Blog
English 
Registry

Find libraries, plugins, integrations, and other useful tools for using and extending OpenTelemetry.

Note

The OpenTelemetry Registry allows you to search for instrumentation libraries, collector components, utilities, and other useful projects in the OpenTelemetry ecosystem. If you are a project maintainer, you can add your project to the OpenTelemetry Registry.

Search 916 entries
Submit
Reset
Collector
Type
Flags
Cloud Foundry
 native

by Cloud Foundry Authors

Adds an OpenTelemetry Collector to all Linux VMs to egress metrics and traces.
collector cloud foundry
Collector
Language
Application integration
Component
Apache-2.0
License
 Website Documentation
Heroku
 native

by Heroku Telemetry

Heroku Fir adds platform-native support for the collection and distribution of OpenTelemetry signals.
collector heroku
Collector
Language
Application integration
Component
Commercial
License
 Website Documentation
ThousandEyes for OpenTelemetry
 native

by Cisco ThousandEyes

It allows you to export ThousandEyes telemetry data in OTel format.
collector thousandeyes cisco
Collector
Language
Application integration
Component
Commercial
License
 Website Documentation
OpenTelemetry Collector Builder

by 🔭 OpenTelemetry Authors 🔭

A CLI tool that generates OpenTelemetry Collector binaries based on a manifest.
collector
v0.146.1
Version
Collector
Language
Core
Component
Apache 2.0
License
 Documentation Package Details (go) Repository
OpAMP Supervisor

by 🔭 OpenTelemetry Authors 🔭

Collector Supervisor for OpAMP
collector opamp
 Quick Install

When building a custom collector you can add this utilities to the manifest file like the following:

utilities:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/cmd/opampsupervisor v0.146.0


v0.146.0
Version
Collector
Language
Utilities
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Collector Environment Variable Provider

by 🔭 OpenTelemetry Authors 🔭

Environment variable provider for OpenTelemetry Collector configuration maps.
go confmap provider collector env
 Quick Install

When building a custom collector you can add this provider to the manifest file like the following:

providers:

    - gomod:

        go.opentelemetry.io/collector/confmap/provider/envprovider v1.52.0


v1.52.0
Version
Collector
Language
Provider
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Collector File Provider

by 🔭 OpenTelemetry Authors 🔭

File provider for OpenTelemetry Collector configuration maps.
go confmap provider collector file
 Quick Install

When building a custom collector you can add this provider to the manifest file like the following:

providers:

    - gomod:

        go.opentelemetry.io/collector/confmap/provider/fileprovider v1.52.0


v1.52.0
Version
Collector
Language
Provider
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Collector Google Secret Manager Provider

by 🔭 OpenTelemetry Authors 🔭

Google Secret Manager provider for OpenTelemetry Collector configuration maps.
go confmap provider collector googlesecretmanager
 Quick Install

When building a custom collector you can add this provider to the manifest file like the following:

providers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/confmap/provider/googlesecretmanagerprovider v0.146.0


v0.146.0
Version
Collector
Language
Provider
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Collector HTTP Provider

by 🔭 OpenTelemetry Authors 🔭

HTTP provider for OpenTelemetry Collector configuration maps.
go confmap provider collector http
 Quick Install

When building a custom collector you can add this provider to the manifest file like the following:

providers:

    - gomod:

        go.opentelemetry.io/collector/confmap/provider/httpprovider v1.52.0


v1.52.0
Version
Collector
Language
Provider
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Collector HTTPS Provider

by 🔭 OpenTelemetry Authors 🔭

HTTPS provider for OpenTelemetry Collector configuration maps.
go confmap provider collector https
 Quick Install

When building a custom collector you can add this provider to the manifest file like the following:

providers:

    - gomod:

        go.opentelemetry.io/collector/confmap/provider/httpsprovider v1.52.0


v1.52.0
Version
Collector
Language
Provider
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Collector YAML Provider

by 🔭 OpenTelemetry Authors 🔭

YAML provider for OpenTelemetry Collector configuration maps.
go confmap provider collector yaml
 Quick Install

When building a custom collector you can add this provider to the manifest file like the following:

providers:

    - gomod:

        go.opentelemetry.io/collector/confmap/provider/yamlprovider v1.52.0


v1.52.0
Version
Collector
Language
Provider
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Alertmanager Exporter

by 🔭 OpenTelemetry Authors 🔭

Exports OTel Events (SpanEvent in Tracing added by AddEvent API) as Alerts to Alertmanager backend to notify Errors or Change events.
alertmanager prometheus exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/alertmanagerexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Alibaba Cloud Log Service Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Alibaba Cloud Log Service Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/alibabacloudlogserviceexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
APIClarity HTTP Exporter

by Cisco

Exports traces and/or metrics via HTTP to an APIClarity endpoint for analysis.
go exporter collector apiclarity
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/openclarity/apiclarity/plugins/otel-collector/apiclarityexporter v0.0.0


v0.0.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS X-Ray Tracing Exporter

by 🔭 OpenTelemetry Authors 🔭

The AWS X-Ray Tracing Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsxrayexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS CloudWatch Logs Exporter

by 🔭 OpenTelemetry Authors 🔭

AWS CloudWatch Logs Exporter sends logs data to AWS CloudWatch Logs
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awscloudwatchlogsexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS CloudWatch EMF Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The AWS CloudWatch EMF Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsemfexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS S3 Exporter for OpenTelemetry Collector

by 🔭 OpenTelemetry Authors 🔭

This exporter targets to support proto/JSON and proto/binary format
aws s3 exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awss3exporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Azure Monitor Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Azure Monitor Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azuremonitorexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Apache Blob Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending traces, metrics, and logs data to [Azure Blob storage] (https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview).
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azureblobexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Azure Data Explorer Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter sends metrics, logs and trace data to Azure Data Explorer
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azuredataexplorerexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
BMC Helix Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending metrics to BMC Helix Operations Management through its metric ingestion REST API.
bmchelix exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/bmchelixexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Cassandra Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending OpenTelemetry logs and traces to Cassandra
cassandra exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/cassandraexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
ClickHouse Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending OpenTelemetry logs and spans to ClickHouse
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/clickhouseexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Coralogix Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Coralogix Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/coralogixexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Datadog Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Datadog Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datadogexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Dataset Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Dataset Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datasetexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Debug Exporter

by 🔭 OpenTelemetry Authors 🔭

Exports data to the console via zap.Logger.
debug exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        go.opentelemetry.io/collector/exporter/debugexporter v0.146.1


v0.146.1
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Apache Doris Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending traces, metrics, and logs data to Apache Doris (version >= 2.1).
doris exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/dorisexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
DuckLake Exporter

by hrl20

This exporter supports writing logs and traces to the DuckLake format.
exporter collector datalake duckdb
Collector
Language
Exporter
Component
Apache 2.0
License
 Repository
Elasticsearch Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending OpenTelemetry logs to Elasticsearch
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Faro Exporter

by 🔭 OpenTelemetry Authors 🔭

The OpenTelemetry Collector Exporter for Faro
go exporter faro collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/faroexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
File Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The File Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/fileexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Fluent Forward Exporter

by Romain Dauby

The OpenTelemetry Collector Exporter for the Fluent Forward protocol
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/r0mdau/fluentforwardexporter v0.4.2


v0.4.2
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Google Cloud Operations Collector Exporter

by Google

The Google Cloud Operations Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Google Cloud Pubsub Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter sends OTLP messages to a Google Cloud Pubsub topic.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudpubsubexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Google Managed Service for Prometheus Exporter

by Google

This exporter can be used to send metrics and traces to Google Cloud Managed Service for Prometheus.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlemanagedprometheusexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Honeycomb Marker Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter allows creating markers, via the Honeycomb Markers API, based on the look of incoming telemetry.
honeycombmarker exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/honeycombmarkerexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
InfluxDB Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending tracing, metrics, and logging data to InfluxDB
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/influxdbexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Kafka Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Kafka Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/kafkaexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Trace ID aware load-balancing Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Trace ID aware load-balancing for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/loadbalancingexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
LogicMonitor Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending logs and traces data to Logicmonitor
logicmonitor exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logicmonitorexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Logz.io Exporter

by 🔭 OpenTelemetry Authors 🔭

The OpenTelemetry Collector Exporter for Logz.io
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logzioexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Mezmo Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending OpenTelemetry log data to Mezmo.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/mezmoexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
No-op Exporter

by 🔭 OpenTelemetry Authors 🔭

Serves as a placeholder exporter in a pipeline. This can be useful if you want to e.g. start a Collector with only extensions enabled, or for testing Collector pipeline throughput without worrying about an exporter.
nop exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        go.opentelemetry.io/collector/exporter/nopexporter v0.146.1


v0.146.1
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OpenSearch Exporter

by 🔭 OpenTelemetry Authors 🔭

OpenSearch exporter supports sending OpenTelemetry signals as documents to OpenSearch.
opensearch exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/opensearchexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OpenTelemetry Protocol with Apache Arrow Exporter

by 🔭 OpenTelemetry Authors 🔭

Exports telemetry data using OpenTelemetry Protocol with Apache Arrow components with support for both OpenTelemetry Protocol with Apache Arrow and standard OpenTelemetry Protocol (OTLP) protocol via gRPC.
apache arrow exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/otelarrowexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OTLP gRPC Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The OTLP gRPC Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        go.opentelemetry.io/collector/exporter/otlpexporter v0.146.1


v0.146.1
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OTLP HTTP Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The OTLP HTTP Exporter for the OpenTelemetry Collector.
go exporter collector
Collector
Language
Exporter
Component
Apache 2.0
License
 Repository
Prometheus Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Prometheus Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/prometheusexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Prometheus Remote Write Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Prometheus Remote Write Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/prometheusremotewriteexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Pulsar Exporter

by 🔭 OpenTelemetry Authors 🔭

Pulsar exporter exports logs, metrics, and traces to Pulsar. This exporter uses a synchronous producer
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/pulsarexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
qryn exporter

by lorenzo@qxip.net, akvlad@qxip.net

This exporter supports sending OpenTelemetry logs, traces and metrics to ClickHouse using the qryn polyglot format.
go exporter qryn loki prometheus tempo
Collector
Language
Exporter
Component
Apache 2.0
License
 Repository
RabbitMQ Exporter

by 🔭 OpenTelemetry Authors 🔭

Exports metrics, traces, and logs to RabbitMQ using the AMQP 0.9.1 protocol
rabbitmq exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/rabbitmqexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
SAPM Exporter

by 🔭 OpenTelemetry Authors 🔭

The SAPM exporter builds on the Jaeger proto and adds additional batching on top. This allows
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sapmexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Sematext Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending metrics to Sematext Cloud in Influx line protocol format and logs using the Bulk Index API format.
sematext exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sematextexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Sentry Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Sentry Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sentryexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
SignalFx Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The SignalFx Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Splunk HTTP Event Collector (HEC) Exporter

by 🔭 OpenTelemetry Authors 🔭

The Splunk HTTP Event Collector (HEC) Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/splunkhecexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Splunk SAPM Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Splunk SAPM Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sapmexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
STEF Exporter

by 🔭 OpenTelemetry Authors 🔭

Exports data via gRPC using
stef exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/stefexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Sumo Logic Exporter

by 🔭 OpenTelemetry Authors 🔭

The OpenTelemetry Collector Exporter for Sumo Logic
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sumologicexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Syslog Exporter

by 🔭 OpenTelemetry Authors 🔭

The syslog exporter supports sending messages to a remote syslog server.
syslog exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/syslogexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
TencentCloud LogService Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter supports sending OpenTelemetry log data to LogService.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/tencentcloudlogserviceexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Tinybird Exporter

by 🔭 OpenTelemetry Authors 🔭

This exporter sends logs, metrics, and traces to Tinybird via the Events API.
tinybird exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/tinybirdexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Zipkin Collector Exporter

by 🔭 OpenTelemetry Authors 🔭

The Zipkin Exporter for the OpenTelemetry Collector.
go exporter collector
 Quick Install

When building a custom collector you can add this exporter to the manifest file like the following:

exporters:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/exporter/zipkinexporter v0.146.0


v0.146.0
Version
Collector
Language
Exporter
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Ack Extension

by 🔭 OpenTelemetry Authors 🔭

This extension allows acking of data upon successful processing. The upstream agent can choose to send event again if ack fails.
ack extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/ackextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
ASAP Client Authentication Extension

by 🔭 OpenTelemetry Authors 🔭

This extension provides Atlassian Service Authentication Protocol (ASAP) client credentials for HTTP or gRPC based exporters.
asap auth extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/asapauthextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Azure authenticator extension

by 🔭 OpenTelemetry Authors 🔭

This extension implements both extensionauth.HTTPClient and extensionauth.Server, so it can be used in both exporters and receivers.
azureauth extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/azureauthextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Basic Authenticator

by 🔭 OpenTelemetry Authors 🔭

This extension implements both configauth.ServerAuthenticator and configauth.ClientAuthenticator to authenticate clients and servers using Basic Authentication.
basicauth extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/basicauthextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Bearer token authenticator extension

by 🔭 OpenTelemetry Authors 🔭

The Bearer token authenticator extension allows gRPC and HTTP-based exporters to add authentication data to outgoing calls based on a static token.
go extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/bearertokenauthextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Cgroup Go runtime extension

by 🔭 OpenTelemetry Authors 🔭

The OpenTelemetry Cgroup Auto-Config Extension is designed to optimize Go runtime performance in containerized environments by automatically configuring GOMAXPROCS and GOMEMLIMIT based on the Linux cgroup filesystem. This extension leverages automaxprocs or gomaxecs for AWS ECS Tasks and automemlimit packages to dynamically adjust Go runtime variables, ensuring efficient resource usage aligned with container limits.
cgroupruntime extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/cgroupruntimeextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Datadog Collector Extension

by 🔭 OpenTelemetry Authors 🔭

The Datadog Extension for the OpenTelemetry Collector.
go extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Encoding extension

by 🔭 OpenTelemetry Authors 🔭

The encoding extension allows for other components to reference ingress/egress data formats
encoding extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Google Client Auth Extension

by 🔭 OpenTelemetry Authors 🔭

This extension provides Google OAuth2 Client Credentials and Metadata for gRPC and HTTP based exporters.
google client auth extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/googleclientauthextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Headers Setter extension

by 🔭 OpenTelemetry Authors 🔭

The headers_setter extension implements ClientAuthenticator and is used to set requests headers in gRPC / HTTP exporters with values provided via extension configurations or requests metadata (context).
headers setter extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/headerssetterextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Health Check Collector Extension

by 🔭 OpenTelemetry Authors 🔭

The Health Check Extension for the OpenTelemetry Collector enables an HTTP URL that can be probed to check the status of the OpenTelemetry Collector.
go extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Health Check Extension V2

by 🔭 OpenTelemetry Authors 🔭

This is an experimental extension that is intended to replace the existing health check extension.
healthcheckv2 extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckv2extension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
HTTP Forwarder Collector Extension

by 🔭 OpenTelemetry Authors 🔭

The HTTP Forwarder Extension for the OpenTelemetry Collector accepts HTTP requests, optionally adds headers to them and forwards them.
go extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/httpforwarderextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
ASAP Client Authentication Extension

by 🔭 OpenTelemetry Authors 🔭

This extension allows serving sampling strategies following the Jaeger’s remote sampling API.
jaeger sampling extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Memory Limiter Extension

by 🔭 OpenTelemetry Authors 🔭

The memory limiter extension is used to prevent out of memory situations on
memory limiter extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        go.opentelemetry.io/collector/extension/memorylimiterextension v0.146.1


v0.146.1
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OAuth2 Client Credentials authenticator extension

by 🔭 OpenTelemetry Authors 🔭

The OAuth2 Client Credentials authenticator extension allows gRPC and HTTP-based exporters to add authentication data to outgoing calls.
go extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/oauth2clientauthextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Host Observer Collector Extension

by 🔭 OpenTelemetry Authors 🔭

Observers are implemented as an extension to discover networked endpoints like a Kubernetes pod, Docker container, or local listening port. Currently available are observers for docker, ecs, ecs_task, host and K8s.
go extension collector
Collector
Language
Extension
Component
Apache 2.0
License
 Repository
OIDC authenticator extension

by 🔭 OpenTelemetry Authors 🔭

The OIDC authenticator extension allows gRPC and HTTP-based receivers to require authentication from remote clients.
go extension collector oidc
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/oidcauthextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OpAMP Agent Extension

by 🔭 OpenTelemetry Authors 🔭

Collector extension for OpAMP
opamp extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/opampextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Performance Profiler Collector Extension

by 🔭 OpenTelemetry Authors 🔭

The Performance Profiler Extension for the OpenTelemetry Collector can be used to collect performance profiles and investigate issues with the service.
go extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/pprofextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Remote Tap Extension

by 🔭 OpenTelemetry Authors 🔭

This extension runs as a Web server that loads the remote observers that are registered against it.
remote tap extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/remotetapextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Authenticator - SigV4

by 🔭 OpenTelemetry Authors 🔭

This extension provides SigV4 authentication for making requests to AWS services.
sigv4 auth extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/sigv4authextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Solarwinds APM Settings extension

by 🔭 OpenTelemetry Authors 🔭

The Solarwinds APM Settings extension gets Solarwinds APM specific settings from Solarwinds APM collector and /tmp/solarwinds-apm-settings.json & /tmp/solarwinds-apm-settings-raw periodically.
solarwinds apm settings extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/solarwindsapmsettingsextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Sumo Logic Extension

by 🔭 OpenTelemetry Authors 🔭

This extension is to be used in conjunction with the Sumo Logic Exporter in order to export telemetry data to Sumo Logic.
sumologic extension collector
 Quick Install

When building a custom collector you can add this extension to the manifest file like the following:

extensions:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/extension/sumologicextension v0.146.0


v0.146.0
Version
Collector
Language
Extension
Component
Apache 2.0
License
 Package Details (go-collector) Repository
zPages Collector Extension

by 🔭 OpenTelemetry Authors 🔭

The zPages Extension for the OpenTelemetry Collector serves zPages, an HTTP endpoint that provides live data for debugging different components that were properly instrumented for such.
go extension collector
Collector
Language
Extension
Component
Apache 2.0
License
 Repository
Attribute Collector Processor

by 🔭 OpenTelemetry Authors 🔭

The Attribute Processor for the OpenTelemetry Collector modifies attributes of a span.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/attributesprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Batch Collector Processor

by 🔭 OpenTelemetry Authors 🔭

The Batch Processor for the OpenTelemetry Collector accepts spans, metrics, or logs and places them into batches.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        go.opentelemetry.io/collector/processor/batchprocessor v0.146.1


v0.146.1
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Coralogix Processor

by 🔭 OpenTelemetry Authors 🔭

The Coralogix processor adds attributes to spans that enable features in Coralogix.
coralogix processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/coralogixprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Cumulative to Delta Processor

by 🔭 OpenTelemetry Authors 🔭

The cumulative to delta processor converts monotonic, cumulative sum and histogram metrics to monotonic, delta metrics. Non-monotonic sums and exponential histograms are excluded.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/cumulativetodeltaprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Datadog Semantics Processor

by 🔭 OpenTelemetry Authors 🔭

undefined
datadogsemantics processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/datadogsemanticsprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Delta to cumulative processor

by 🔭 OpenTelemetry Authors 🔭

The delta to cumulative processor (deltatocumulativeprocessor) converts metrics from delta temporality to cumulative, by accumulating samples in memory.
deltatocumulative processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Delta to Rate Processor

by 🔭 OpenTelemetry Authors 🔭

The delta to rate processor converts delta sum metrics to rate metrics. This rate is a gauge.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatorateprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
DNS Lookup Processor

by 🔭 OpenTelemetry Authors 🔭

The DNS Lookup Processor for the OpenTelemetry Collector is used to resolve DNS names to IP addresses.
dnslookup processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/dnslookupprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Filter Collector Processor

by 🔭 OpenTelemetry Authors 🔭

The Filter Processor for the OpenTelemetry Collector can be configured to include or exclude metrics.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/filterprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
GeoIP Processor

by 🔭 OpenTelemetry Authors 🔭

The geoIP processor geoipprocessor enhances resource attributes by appending information about the geographical location of an IP address. To add geographical information, the IP address must be included in the resource attributes using the source.address semantic conventions key attribute.
geoip processor collector
Collector
Language
Processor
Component
Apache 2.0
License
 Repository
Group by Trace Processor

by 🔭 OpenTelemetry Authors 🔭

The Group by Trace Processor for the OpenTelemetry Collector collects all the spans from the same trace, waiting a pre-determined amount of time before releasing the trace to the next processor.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbytraceprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Group by Attributes processor

by 🔭 OpenTelemetry Authors 🔭

This processor re-associates spans, log records and metric data points to a Resource that matches with the specified attributes. As a result, all spans, log records or metric data points with the same values for the specified attributes are “grouped” under the same Resource.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbyattrsprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Interval Processor

by 🔭 OpenTelemetry Authors 🔭

The interval processor (intervalprocessor) aggregates metrics and periodically forwards the latest values to the next component in the pipeline.
interval processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/intervalprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Isolation Forest Processor

by 🔭 OpenTelemetry Authors 🔭

The Isolation Forest processor adds inline, unsupervised anomaly detection to any OpenTelemetry Collector pipeline (traces, metrics, or logs). It embeds a lightweight implementation of the Isolation Forest algorithm that automatically learns normal behaviour from recent telemetry and tags, scores, or optionally drops anomalies in‑flight – no external ML service required.
isolationforest processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/isolationforestprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
K8s Attribute Processor

by 🔭 OpenTelemetry Authors 🔭

The K8s Attribute Processor for the OpenTelemetry Collector automatically discovers K8s resources (pods), extracts metadata from them and adds the extracted metadata to the relevant spans, metrics and logs.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/k8sattributesprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Log DeDuplication Processor

by 🔭 OpenTelemetry Authors 🔭

This processor is used to deduplicate logs by detecting identical logs over a range of time and emitting a single log with the count of logs that were deduplicated.
logdedup processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/logdedupprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Logs Transform Processor

by 🔭 OpenTelemetry Authors 🔭

The logs transform processor can be used to apply log operators to logs coming from any receiver. Please refer to config.go for the config spec.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/logstransformprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Memory Limiter Collector Processor

by 🔭 OpenTelemetry Authors 🔭

The Memory Limiter Processor for the OpenTelemetry Collector is used to prevent out of memory situations on the collector.
go processor collector
Collector
Language
Processor
Component
Apache 2.0
License
 Repository
Metrics Transform Processor

by 🔭 OpenTelemetry Authors 🔭

The Metrics Transform Processor for the OpenTelemetry Collector can be used to rename metrics, and add, rename or delete label keys and values. It can also be used to perform aggregations on metrics across labels or label values.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstransformprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Metrics Generation Processor

by 🔭 OpenTelemetry Authors 🔭

The metrics generation processor can be used to create new metrics using existing metrics following a given rule. Currently it supports following two approaches for creating a new metric.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricsgenerationprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Metric Start Time Processor

by 🔭 OpenTelemetry Authors 🔭

The metric start time processor (metricstarttime) is used to set the start
metricstarttime processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstarttimeprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Probabilistic Sampling Collector Processor

by 🔭 OpenTelemetry Authors 🔭

The Probabilistic Sampling Processor for the OpenTelemetry Collector provides probabilistic sampling of traces.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/probabilisticsamplerprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Redaction processor

by 🔭 OpenTelemetry Authors 🔭

This processor deletes span attributes that don’t match a list of allowed span
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/redactionprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Websocket Processor

by 🔭 OpenTelemetry Authors 🔭

The WebSocket processor, which can be positioned anywhere in a pipeline, allows
websocket remote tap processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/remotetapprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Resource Collector Processor

by 🔭 OpenTelemetry Authors 🔭

The Resource Processor for the OpenTelemetry Collector can be used to apply changes on resource attributes.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourceprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Resource Detection Processor

by 🔭 OpenTelemetry Authors 🔭

The Resource Detection Processor for the OpenTelemetry Collector can be used to detect resource information from the host, in a format that conforms to the OpenTelemetry resource semantic conventions, and append or override the resource value in telemetry data with this information.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Schema Transformer Processor

by 🔭 OpenTelemetry Authors 🔭

The Schema Processor is used to convert existing telemetry data or signals to a version of the semantic convention defined as part of the configuration.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Span Collector Processor

by 🔭 OpenTelemetry Authors 🔭

The Span Processor for the OpenTelemetry Collector modifies either the span name or attributes of a span based on the span name.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/spanprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Sumo Logic Processor

by 🔭 OpenTelemetry Authors 🔭

The Sumo Logic processor modifies the metadata on logs, metrics and traces sent to Sumo Logic so that the Sumo Logic apps can make full use of the ingested data.
sumologic processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/sumologicprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Tail Sampling Processor

by 🔭 OpenTelemetry Authors 🔭

The Tail Sampling Processor for the OpenTelemetry Collector samples traces based on a set of defined policies.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Transform Processor

by 🔭 OpenTelemetry Authors 🔭

The Transform Processor for the OpenTelemetry Collector can be used to transform any fields on traces, metrics, and logs within the collector. It utilizes a transformation language to define transformations and conditions and then applies those transformations to the specified telemetry.
go processor collector
 Quick Install

When building a custom collector you can add this processor to the manifest file like the following:

processors:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor v0.146.0


v0.146.0
Version
Collector
Language
Processor
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Active Directory Domain Services Receiver

by 🔭 OpenTelemetry Authors 🔭

The active_directory_ds receiver scrapes metric relating to an Active Directory domain controller using the Windows Performance Counters.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/activedirectorydsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Aerospike Receiver

by 🔭 OpenTelemetry Authors 🔭

The Aerospike receiver is designed to collect performance metrics from one or more Aerospike nodes.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/aerospikereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Apache Web Server Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver fetches stats from a Apache Web Server instance using the server-status?auto endpoint.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/apachereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Apache Spark Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver fetches metrics for an Apache Spark cluster through the Apache Spark REST API
apache spark receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/apachesparkreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS ECS Container Metrics Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The AWS ECS Container Metrics Receiver for the OpenTelemetry Collector reads task metadata and docker stats from Amazon ECS Task Metadata Endpoint, and generates resource usage metrics (such as CPU, memory, network, and disk) from them.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsecscontainermetricsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS X-Ray Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The AWS X-Ray Receiver for the OpenTelemetry Collector accepts segments (i.e. spans) in the X-Ray Segment format. This enables the collector to receive spans emitted by the existing X-Ray SDK.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsxrayreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Cloudwatch Receiver

by 🔭 OpenTelemetry Authors 🔭

Receives Cloudwatch events from AWS CloudWatch via the AWS SDK for Cloudwatch Logs
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscloudwatchreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS Container Insights Receiver

by 🔭 OpenTelemetry Authors 🔭

AWS Container Insights Receiver is an AWS specific receiver that supports CloudWatch Container Insights.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS Kinesis Data Firehose Receiver

by 🔭 OpenTelemetry Authors 🔭

Receiver for ingesting AWS Kinesis Data Firehose delivery stream messages and parsing the records received based on the configured record type.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsfirehosereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
AWS S3 Receiver

by 🔭 OpenTelemetry Authors 🔭

Receiver for retrieving trace previously stored in S3 by the AWS S3 Exporter.
aws s3 receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awss3receiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Azure Blob Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver reads logs and trace data from Azure Blob Storage
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azureblobreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Azure Event Hub Receiver

by 🔭 OpenTelemetry Authors 🔭

The Azure Event Hub receiver listens to logs emitted by Azure Event hubs.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azureeventhubreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Azure Monitor Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver scrapes Azure Monitor API for resources metrics.
azure monitor receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azuremonitorreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Carbon Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Carbon Receiver for the OpenTelemetry Collector supports Carbon’s plaintext protocol.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/carbonreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Chrony Receiver

by 🔭 OpenTelemetry Authors 🔭

The chrony receiver is a pure go implementation of the command chronyc tracking
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/chronyreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Cloudflare Receiver

by 🔭 OpenTelemetry Authors 🔭

This Cloudflare receiver allows Cloudflare’s LogPush Jobs to send logs from the Cloudflare logs aggregation system
cloudflare receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/cloudflarereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Cloud Foundry Receiver

by 🔭 OpenTelemetry Authors 🔭

The Cloud Foundry receiver connects to the RLP (Reverse Log Proxy) Gateway of the Cloud Foundry installation
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/cloudfoundryreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
CollectD Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The CollectD Receiver for the OpenTelemetry Collector can receive data exported by the CollectD’s write_http plugin.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/collectdreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
CouchDB Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver fetches stats from a CouchDB server.
go receiver collector couchdb
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/couchdbreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Datadog APM Receiver

by 🔭 OpenTelemetry Authors 🔭

The Datadog APM Receiver accepts traces in the Datadog APM format
datadog receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/datadogreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Docker Stats Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Docker Stats Receiver queries the local Docker daemon’s container stats API for all desired running containers on a configured interval.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/dockerstatsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Elasticsearch Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver queries the Elasticsearch node stats and index statsendpoints in order to scrape metrics from a running elasticsearch cluster.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/elasticsearchreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Envoy ALS(access log service) receiver

by 🔭 OpenTelemetry Authors 🔭

This is a receiver for the Envoy gRPC ALS sink.
envoyals receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/envoyalsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Expvar Receiver

by 🔭 OpenTelemetry Authors 🔭

An Expvar Receiver scrapes metrics from expvar
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/expvarreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Faro Receiver

by 🔭 OpenTelemetry Authors 🔭

The OpenTelemetry Collector Receiver for Faro
go receiver faro collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/faroreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Filelog Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Filelog Receiver tails and parses logs from files using the opentelemetry-log-collection library.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filelogreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
File Stats Receiver

by 🔭 OpenTelemetry Authors 🔭

The File Stats receiver collects metrics from files specified with a glob pattern.
filestats receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filestatsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
FlinkMetrics Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver uses Flink’s REST API to collect Jobmanager, Taskmanager, Job, Task and Operator metrics.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/flinkmetricsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Fluent Forward Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Fluent Forward Receiver for the OpenTelemetry Collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/fluentforwardreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Trace2 Receiver

by Jeff Hostetler

A receiver for git Trace2 telemetry from local git commands, translates it into an OpenTelemetry format, and forwards it to other OpenTelemetry components.
go receiver collector trace2 git
Collector
Language
Receiver
Component
MIT
License
 Repository
GitHub Receiver

by 🔭 OpenTelemetry Authors 🔭

The GitHub receiver receives data from GitHub. As a starting point it scrapes metrics from repositories but will be extended to include traces and logs.
github receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/githubreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
GitLab Receiver

by 🔭 OpenTelemetry Authors 🔭

Workflow tracing support is actively being added to the GitLab receiver.
gitlab receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/gitlabreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Google Cloud Monitoring Receiver

by 🔭 OpenTelemetry Authors 🔭

The primary objective of the Google Cloud Monitoring Receiver is to gather time series metrics data from all Google services and convert this data into a pipeline format that facilitates further use.
googlecloudmonitoring receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudmonitoringreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Google Pubsub Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver gets OTLP messages from a Google Cloud Pubsub subscription.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudpubsubreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Google Cloud Spanner Receiver

by 🔭 OpenTelemetry Authors 🔭

Google Cloud Spanner enable you to investigate issues with your database
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudspannerreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
HAProxy Receiver

by 🔭 OpenTelemetry Authors 🔭

The HAProxy receiver generates metrics by polling periodically the HAProxy process through a dedicated socket or HTTP URL.
haproxy receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/haproxyreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Host Metrics Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Host Metrics Receiver for the OpenTelemetry Collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
HTTP Check Receiver

by 🔭 OpenTelemetry Authors 🔭

The HTTP Check Receiver can be used for synthetic checks against HTTP endpoints. This receiver will make a request to the specified endpoint using the
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/httpcheckreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Huawei Cloud CES Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver contains the implementation of the Huawei Cloud Cloud Eye Service (CES) receiver for the OpenTelemetry Collector. The receiver collects metrics from Huawei Cloud’s CES service and sends them to the OpenTelemetry Collector for processing and exporting.
huaweicloudces receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/huaweicloudcesreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Microsoft IIS Receiver

by 🔭 OpenTelemetry Authors 🔭

The iis receiver grabs metrics about an IIS instance using the Windows Performance Counters.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/iisreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
InfluxDB Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver accepts metrics data as InfluxDB Line Protocol.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/influxdbreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Jaeger Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Jaeger Receiver for the OpenTelemetry Collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jaegerreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
JMX Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The JMX Receiver will work in conjunction with the OpenTelemetry JMX Metric Gatherer to report metrics from a target MBean server using a built-in or your custom OpenTelemetry helper-utilizing Groovy script.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jmxreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Journald Receiver

by 🔭 OpenTelemetry Authors 🔭

Parses Journald events from systemd journal.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/journaldreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Kubernetes Cluster Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Kubernetes Cluster Receiver for the OpenTelemetry Collector collects cluster-level metrics from the Kubernetes API server. It uses the K8s API to listen for updates. A single instance of this receiver can be used to monitor a cluster.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Kubernetes Events Receiver

by 🔭 OpenTelemetry Authors 🔭

The Kubernetes Events receiver collects events from the Kubernetes
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8seventsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
K8slog Receiver

by 🔭 OpenTelemetry Authors 🔭

Tails and parses logs in K8s environment.
k8slog receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8slogreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Kubernetes Objects Receiver

by 🔭 OpenTelemetry Authors 🔭

The Kubernetes Objects receiver collects(pull/watch) objects from the Kubernetes API server.
k8sobjects receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sobjectsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Kafka Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Kafka Receiver for the OpenTelemetry Collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kafkareceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Kafka Metrics Receiver

by 🔭 OpenTelemetry Authors 🔭

Kafka metrics receiver collects Kafka metrics (brokers, topics, partitions, consumer groups) from Kafka server,
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kafkametricsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Kubelet Stats Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Kubelet Stats Receiver for the OpenTelemetry Collector pulls pod metrics from the API server on a kubelet and sends it down the metric pipeline for further processing.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kubeletstatsreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Libhoney Receiver

by 🔭 OpenTelemetry Authors 🔭

The Libhoney receiver will accept data for either Trace or Logs signals that are emitted from applications that were
libhoney receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/libhoneyreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OpenTelemetry Collector Lightstep Receiver

by Zalando SE

The lightstepreceiver receives OpenTracing traces from Lightstep tracers in various supported formats converting them into OpenTelemetry’a ptrace.Traces propagating it further in pipelines
lightstep receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/zalando/otelcol-lightstep-receiver v0.0.16


v0.0.16
Version
Collector
Language
Receiver
Component
MIT
License
 Package Details (go-collector) Repository
Loki Receiver

by 🔭 OpenTelemetry Authors 🔭

The Loki receiver implements the Loki Push API
loki receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/lokireceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Memcached Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Memcached Receiver for the OpenTelemetry Collector can fetch stats from a Memcached instance using the stats command.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/memcachedreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
MongoDB Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver fetches stats from a MongoDB instance using the [golang
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mongodbreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
MongoDB Atlas Receiver

by 🔭 OpenTelemetry Authors 🔭

Receives metrics from MongoDB Atlas
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mongodbatlasreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
MySQL Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver queries MySQL’s global status and InnoDB tables.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mysqlreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Named Pipe Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver supports opening a Unix Named Pipe (aka FIFO), and reading logs from it.
namedpipe receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/namedpipereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Netflow receiver

by 🔭 OpenTelemetry Authors 🔭

The netflow receiver can listen for netflow, sflow, and ipfix data and convert it to OpenTelemetry logs. The receiver is based on the goflow2 project.
netflow receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/netflowreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
NGINX Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The NGINX Receiver for the OpenTelemetry Collector can fetch stats from a NGINX instance using a mod_status endpoint.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/nginxreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
No-op Receiver

by 🔭 OpenTelemetry Authors 🔭

Serves as a placeholder receiver in a pipeline. This can be useful if you want to e.g. start a Collector with only extensions enabled.
nop receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        go.opentelemetry.io/collector/receiver/nopreceiver v0.146.1


v0.146.1
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
NSX-T Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver fetches metrics important to run virtual networking using NSX-T. The receiver ingests metrics via the NSX Rest API
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/nsxtreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
NTP Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver periodically retrieves the clock offset from a NTP server.
ntp receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ntpreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OPC UA Log Receiver
 new

by Thomas Brüggemann

The OPC UA Log Receiver collects log records from OPC UA servers implementing the LogObject specification (OPC UA Part 26) and converts them to OpenTelemetry log format for industrial automation system observability.
go receiver collector opc-ua logs industrial
Collector
Language
Receiver
Component
Apache 2.0
License
 Repository
Oracle DB receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver collects metrics from an Oracle Database.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/oracledbreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
osquery Receiver

by 🔭 OpenTelemetry Authors 🔭

The osquery receiver runs queries run on an osquery’s daemon on a schedule and converts the output to logs.
osquery receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/osqueryreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OpenTelemetry Protocol with Apache Arrow Receiver

by 🔭 OpenTelemetry Authors 🔭

Receives telemetry data using OpenTelemetry Protocol with Apache Arrow and standard OTLP protocol via gRPC.
arrow receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OTLP Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The OTLP Receiver for the OpenTelemetry Collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        go.opentelemetry.io/collector/receiver/otlpreceiver v0.146.1


v0.146.1
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
OTLP JSON File Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver will read pipeline data from JSON files. The data is written in
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otlpjsonfilereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Podman Stats Receiver

by 🔭 OpenTelemetry Authors 🔭

The Podman Stats receiver queries the Podman service API to fetch stats for all running containers
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/podmanreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
PostgreSQL Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver queries the PostgreSQL statistics collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/postgresqlreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Pprof Receiver

by 🔭 OpenTelemetry Authors 🔭

TODO
pprof receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/pprofreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Prometheus Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Prometheus Receiver for the OpenTelemetry Collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Prometheus Remote Write Receiver

by 🔭 OpenTelemetry Authors 🔭

prometheusremotewrite receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusremotewritereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Pulsar Receiver

by 🔭 OpenTelemetry Authors 🔭

Pulsar receiver receives logs, metrics, and traces from Pulsar.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/pulsarreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Pure Storage FlashArray Receiver

by 🔭 OpenTelemetry Authors 🔭

The Pure Storage FlashArray receiver, receives metrics from Pure Storage internal services hosts.
purefa receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/purefareceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Pure Storage FlashBlade Receiver

by 🔭 OpenTelemetry Authors 🔭

The Pure Storage FlashBlade receiver, receives metrics from Pure Storage FlashBlade via the Pure Storage FlashBlade OpenMetrics Exporter.
purefb storage receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/purefbreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
RabbitMQ Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver fetches stats from a RabbitMQ node using the RabbitMQ Management Plugin.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/rabbitmqreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Receiver Creator Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Receiver Creator Receiver for the OpenTelemetry Collector can instantiate other receivers at runtime based on whether observed endpoints match a configured rule.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/receivercreator v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Redis Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Redis Receiver for the OpenTelemetry Collector is designed to retrieve Redis INFO data from a single Redis instance, build metrics from that data, and send them to the next consumer at a configurable interval.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/redisreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Riak Receiver

by 🔭 OpenTelemetry Authors 🔭

Riak metrics will be collected from the /stats endpoint.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/riakreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
SAP HANA Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver can fetch stats from a SAP HANA instance. It leverages the driver written by SAP for connecting to SAP HANA with the golang SQL module to execute several monitoring queries.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/saphanareceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
SignalFx Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The SignalFx Receiver for the OpenTelemetry Collector accepts metrics in the SignalFx proto format and events (Logs) in the SignalFx proto format.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/signalfxreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Simple Prometheus Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Simple Prometheus Receiver for the OpenTelemetry Collector provides a simple configuration interface to configure the prometheus receiver to scrape metrics from a single target.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/simpleprometheusreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Skywalking Receiver

by 🔭 OpenTelemetry Authors 🔭

Receives trace data in Skywalking format.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/skywalkingreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
SNMP Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver fetches stats from an SNMP-enabled host using the Go SNMP client. Metrics are collected based on configuration settings.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/snmpreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Snowflake Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver collects metrics from a Snowflake account by connecting to an account and running queries at set intervals.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/snowflakereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Solace Receiver

by 🔭 OpenTelemetry Authors 🔭

The Solace receiver receives trace data from a Solace PubSub+ Event Broker
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/solacereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Splunk HEC Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Splunk HEC Receiver for the OpenTelemetry Collector accepts metrics, traces, and logs in the Splunk HEC format.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/splunkhecreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
splunkenterprise

by 🔭 OpenTelemetry Authors 🔭

The Splunk Enterprise Receiver is a pull based tool which enables the ingestion of performance metrics describing the operational status of a user’s Splunk Enterprise deployment to an appropriate observability tool.
splunkenterprise receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/splunkenterprisereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
SQL Query Receiver (Alpha)

by 🔭 OpenTelemetry Authors 🔭

The SQL Query Receiver uses custom SQL queries to generate metrics from a database connection.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sqlqueryreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Microsoft SQL Server Receiver

by 🔭 OpenTelemetry Authors 🔭

The sqlserver receiver grabs metrics about a Microsoft SQL Server instance using the Windows Performance Counters.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sqlserverreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
SSH Check Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver creates stats by connecting to an SSH server which may be an SFTP server.
ssh sftp receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sshcheckreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
StatsD Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The StatsD Receiver for the OpenTelemetry Collector ingests StatsD messages.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/statsdreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
STEF Receiver

by 🔭 OpenTelemetry Authors 🔭

Receives data via gRPC in Otel/STEF format. Otel/STEF is a compact and
stef receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/stefreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Syslog Receiver

by 🔭 OpenTelemetry Authors 🔭

Parses Syslogs received over TCP or UDP.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/syslogreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Systemd Receiver

by 🔭 OpenTelemetry Authors 🔭

systemd receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/systemdreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
TCP Check Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver creates stats by connecting to an TCP server.
tcpcheck receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tcpcheckreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
TCP Receiver

by 🔭 OpenTelemetry Authors 🔭

Receives logs over TCP.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tcplogreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
TLS Check Receiver

by 🔭 OpenTelemetry Authors 🔭

Emit metrics about x.509 certificates.
tlscheck receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tlscheckreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Trace Simulation Receiver

by Takuya Kajiwara

A receiver that generates synthetic traces based on a declarative blueprint for testing and demonstration purposes.
go receiver synthetic trace simulation
Collector
Language
Receiver
Component
Apache 2.0
License
 Repository
UDP Receiver

by 🔭 OpenTelemetry Authors 🔭

Receives logs over UDP.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/udplogreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
vCenter Receiver

by 🔭 OpenTelemetry Authors 🔭

This receiver fetches metrics from a vCenter or ESXi host running VMware vSphere APIs.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/vcenterreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Wavefront Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Wavefront Receiver for the OpenTelemetry Collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/wavefrontreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Webhook Event Receiver

by 🔭 OpenTelemetry Authors 🔭

The Webhook Event receiver is meant to act as a generally available push based receiver for any webhook style data source.
webhookevent receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/webhookeventreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Windows Performance Counters Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Windows Performance Counters Receiver for the OpenTelemetry Collector captures the configured system, application, or custom performance counter data from the Windows registry using the PDH interface.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowsperfcountersreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Windows Log Event Receiver

by 🔭 OpenTelemetry Authors 🔭

Tails and parses logs from windows event log API using the opentelemetry-log-collection library.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowseventlogreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Windows Service Receiver

by 🔭 OpenTelemetry Authors 🔭

The Windows Service Receiver is a receiver for scraping information about the state of services running on a Windows machine.
windowsservice receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowsservicereceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Zipkin Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Zipkin Receiver for the OpenTelemetry Collector.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/zipkinreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Zookeeper Collector Receiver

by 🔭 OpenTelemetry Authors 🔭

The Zookeeper Receiver for the OpenTelemetry Collector collects metrics from a Zookeeper instance, using the ‘mntr’ command.
go receiver collector
 Quick Install

When building a custom collector you can add this receiver to the manifest file like the following:

receivers:

    - gomod:

        github.com/open-telemetry/opentelemetry-collector-contrib/receiver/zookeeperreceiver v0.146.0


v0.146.0
Version
Collector
Language
Receiver
Component
Apache 2.0
License
 Package Details (go-collector) Repository
Collector

by 🔭 OpenTelemetry Authors 🔭

The OpenTelemetry Collector (Agent/Service)
collector agent
Collector
Language
Core
Component
Apache 2.0
License
 Repository
Kubernetes Operator

by 🔭 OpenTelemetry Authors 🔭

A Kubernetes Operator for the OpenTelemetry Collector.
kubernetes
Collector
Language
Core
Component
Apache 2.0
License
 Repository
OddDotNet: Test Harness for OpenTelemetry

by Tyler Kenna

OddDotNet is a Test Harness for OpenTelemetry that works for any language, built in .NET. It is a container image that accepts OpenTelemetry signals over gRPC, and it includes a query language for verifying and validating those signals. OddDotNet enables automated Observability Driven Development, hence where it gets its name.
proto protobuf testing odd observability collector test-harness odddotnet
Collector
Language
Utilities
Component
Apache 2.0
License
 Documentation Repository
OTelBin

by Dash0

SaaS editor for OpenTelemetry Collector configurations with visualization, validation and sharing support
collector configuration-validation dash0 validation visualization
Collector
Language
Utilities
Component
Apache 2.0
License
 Repository
OTTL Playground

by OTTL Playground Authors

Powerful and user-friendly tool designed to allow users to experiment with OTTL effortlessly.
otel collector ottl ottl-validation validation
Collector
Language
Utilities
Component
Apache 2.0
License
 Website Repository
© 2019–present OpenTelemetry Authors | Docs CC BY 4.0
