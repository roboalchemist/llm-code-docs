# Source: https://docs.datadoghq.com/tracing.md

---
title: APM
description: Instrument your code to improve performance
breadcrumbs: Docs > APM
---

# APM

{% callout %}
##### Join an enablement webinar session

Join an introductory or intermediate enablement session to learn more about how Datadog Application Performance Monitoring (APM) provides AI-powered, code-level distributed tracing from browser and mobile applications to backend services and databases.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=APM)
{% /callout %}

## Overview{% #overview %}

Datadog Application Performance Monitoring (APM) provides deep visibility into your applications, enabling you to identify performance bottlenecks, troubleshoot issues, and optimize your services. With distributed tracing, out-of-the-box dashboards, and seamless correlation with other telemetry data, Datadog APM helps ensure the best possible performance and user experience for your applications.

For an introduction to terminology used in Datadog APM, see [APM Terms and Concepts](https://docs.datadoghq.com/tracing/glossary/).

## Getting started{% #getting-started %}

The simplest way to start with Datadog APM is with Single Step Instrumentation. This approach installs the Datadog Agent and instruments your application in one step, with no additional configuration steps required. To learn more, read [Single Step Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/).

For setups that require more customization, Datadog supports custom instrumentation with Datadog tracing libraries and [Dynamic Instrumentation](https://docs.datadoghq.com/tracing/dynamic_instrumentation/) in the Datadog UI. To learn more, read [Application Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/).

{% alert level="info" %}
If you're new to Datadog APM, read [Getting Started with APM](https://docs.datadoghq.com/getting_started/tracing/) to learn how to send your first trace to Datadog.
{% /alert %}

## Use cases{% #use-cases %}

Discover some ways Datadog APM can help support your use cases:

| You want toâ¦                                                    | How Datadog APM can help                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Understand how requests flow through your system.               | Use the [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/) to query and visualize end-to-end traces across distributed services.                                                                                                                                                                                       |
| Monitor service health and performance of individual services.  | Use the [service](https://docs.datadoghq.com/tracing/services/service_page/) and [resource pages](https://docs.datadoghq.com/tracing/services/resource_page/) to assess service health by analyzing performance metrics, tracking deployments, and identifying problematic resources.                                                    |
| Correlate traces with DBM, RUM, logs, synthetics, and profiles. | [Correlate APM Data with Other Telemetry](https://docs.datadoghq.com/tracing/other_telemetry/) to give context to your data for more comprehensive analysis.                                                                                                                                                                             |
| Control how data flows into Datadog.                            | Use [Ingestion Controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/) to adjust ingestion configuration and sampling rates by service and resource. Use [Retention filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#retention-filters) to choose which spans to retain for 15 days. |

### Trace Explorer{% #trace-explorer %}

The [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/) allows you search and analyze your traces in real-time. Identify performance bottlenecks, troubleshoot errors, and pivot to related logs and metrics to understand the full context around any issue.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/trace_explorer.5ff359dd1362128f456c58bc4c8f352d.png?auto=format"
   alt="Trace explorer view." /%}

### Service page{% #service-page %}

The [service page](https://docs.datadoghq.com/tracing/services/service_page/) helps you monitor service performance and [compare between versions during deployments](https://docs.datadoghq.com/tracing/services/deployment_tracking/).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/deployment_tracking/VersionComparison.22658393ea8fae2a616dfd2d80d01d87.png?auto=format"
   alt="Versions on the Service Page" /%}

### Correlating traces with other telemetry{% #correlating-traces-with-other-telemetry %}

Datadog APM integrates seamlessly with logs, real user monitoring (RUM), synthetic monitoring, and more:

- [View your application logs side-by-side with traces](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/) to find logs for specific requests, services, or versions.
- [Associate RUM sessions with backend traces](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm) to understand how backend performance affects user experience.
- [Associate synthetic tests with traces](https://docs.datadoghq.com/synthetics/apm/) to troubleshoot failures across frontend and backend requests.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/index/ConnectLogsWithTraces.2013232a879299ead4d876365845fa80.png?auto=format"
   alt="Connect Logs And Traces" /%}

### Ingestion controls and retention filters{% #ingestion-controls-and-retention-filters %}

Traces start in your instrumented applications and flow into Datadog.

Datadog APM provides tools to manage the volume and retention of your trace data. Use [Ingestion Controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/) to adjust sampling rates and [retention filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#retention-filters) to control which spans are stored.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/apm_lifecycle/apm_lifecycle_0.b4a77f319f38979ae947ee41e0c3ff3f.png?auto=format"
   alt="Flow of data through Datadog APM." /%}

## Troubleshooting{% #troubleshooting %}

For troubleshooting assistance, read the [APM Troubleshooting](https://docs.datadoghq.com/tracing/troubleshooting/) guide.

## Further reading{% #further-reading %}

- [Check out the latest Datadog APM releases! (App login required)](https://app.datadoghq.com/release-notes?category=APM)
- [How to monitor your Rust applications with OpenTelemetry](https://www.datadoghq.com/blog/monitor-rust-otel/)
- [Generate span-based metrics to track historical trends in application performance](https://www.datadoghq.com/blog/span-based-metrics/)
- [Gain visibility into risks, vulnerabilities, and attacks with APM Security View](https://www.datadoghq.com/blog/apm-security-view/)
- [Monitor your Linux web apps on Azure App Service with Datadog](https://www.datadoghq.com/blog/monitor-azure-app-service-linux/)
- [Manage API performance, security, and ownership with Datadog API Catalog](https://www.datadoghq.com/blog/monitor-apis-datadog-api-catalog/)
- [Improve developer experience and collaboration with Software Catalog](https://www.datadoghq.com/blog/software-catalog/)
- [Bring high-performance observability to secure Kubernetes environments with Datadog's CSI driver](https://www.datadoghq.com/blog/datadog-csi-driver/)
- [Join an interactive session to boost your APM understanding](https://dtdg.co/fe)
- [Troubleshoot faster with the GitLab Source Code integration in Datadog](https://www.datadoghq.com/blog/gitlab-source-code-integration)
