# Source: https://docs.datadoghq.com/error_tracking/backend/getting_started/dd_libraries.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/dd_libraries.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries.md

---
title: Add the Datadog Tracing Library
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > APM > Application Instrumentation > Add the Datadog Tracing Library
---

# Add the Datadog Tracing Library

## Overview{% #overview %}

To automatically instrument your application with Datadog libraries:

1. Install and configure the Agent.
1. Add the Datadog tracing library to your code.

## Install and configure the Agent{% #install-and-configure-the-agent %}

Install and configure the Datadog Agent to receive traces from your instrumented application. By default, the Datadog Agent is configured to receive traces in your `datadog.yaml` file under `apm_config` with `enabled: true` and listens for trace data at `http://localhost:8126`.

For containerized environments, follow the links below to enable trace collection within the Datadog Agent.

### Containers{% #containers %}

1. Set `apm_non_local_traffic: true` in the `apm_config` section of your main [`datadog.yaml` configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file).
1. See the specific setup instructions to ensure that the Agent is configured to receive traces in a containerized environment:

- [Docker](https://docs.datadoghq.com/agent/docker/apm/?tab=java)
- [Kubernetes](https://docs.datadoghq.com/agent/kubernetes/apm/?tab=helm)
- [Amazon ECS](https://docs.datadoghq.com/agent/amazon_ecs/apm/?tab=python)
- [ECS Fargate](https://docs.datadoghq.com/integrations/ecs_fargate/#trace-collection)

The trace client attempts to send traces to the Unix domain socket `/var/run/datadog/apm.socket` by default. If the socket does not exist, traces are sent to `http://localhost:8126`.

If a different socket, host, or port is required, use the `DD_TRACE_AGENT_URL` environment variable. For example:

```gdscript3
DD_TRACE_AGENT_URL=http://custom-hostname:1234
DD_TRACE_AGENT_URL=unix:///var/run/datadog/apm.socket
```

Similarly, the trace client attempts to send stats to the `/var/run/datadog/dsd.socket` Unix domain socket. If the socket does not exist, then stats are sent to `http://localhost:8125`.

{% callout %}
# Important note for users on the following Datadog sites: us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.ddog-gov.com, ap1.datadoghq.com, ap2.datadoghq.com


Set `DD_SITE` in the Datadog Agent to  to ensure the Agent sends data to the right Datadog location.

{% /callout %}

### AWS Lambda{% #aws-lambda %}

To set up Datadog APM in AWS Lambda, see the [Tracing Serverless Functions](https://docs.datadoghq.com/tracing/serverless_functions/) documentation.

### Other environments{% #other-environments %}

Tracing is available for several other environments, such as [Heroku](https://docs.datadoghq.com/agent/basic_agent_usage/heroku/#installation), [Cloud Foundry](https://docs.datadoghq.com/integrations/cloud_foundry/#trace-collection), [AWS Elastic Beanstalk](https://docs.datadoghq.com/integrations/amazon_elasticbeanstalk/), and [Azure App Service](https://docs.datadoghq.com/infrastructure/serverless/azure_app_services/#overview).

For other environments, see the [Integrations](https://docs.datadoghq.com/integrations/) documentation for that environment and [contact support](https://docs.datadoghq.com/help/) if you are encountering any setup issues.

## Instrument your application{% #instrument-your-application %}

Set up your application to send [traces](https://docs.datadoghq.com/tracing/glossary/#trace) using one of the following official Datadog tracing libraries:

- [Java](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java)
- [Python](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python)
- [Ruby](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby)
- [go](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go)
- [Node.js](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/nodejs)
- [PHP](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/php)
- [C++](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/cpp)
- [Rust](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/rust/)
- [.Net](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-core)
- [.Net](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-framework)
- [Android](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/android)
- [iOS](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ios)

To instrument an application written in a language that does not have official library support, see the list of [community tracing libraries](https://docs.datadoghq.com/developers/community/libraries/#apm-tracing-client-libraries).
