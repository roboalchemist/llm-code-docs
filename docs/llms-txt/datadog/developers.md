# Source: https://docs.datadoghq.com/developers.md

---
title: Developers
description: Learn how to develop an integration on Datadog.
breadcrumbs: Docs > Developers
source_url: https://docs.datadoghq.com/index.html
---

# Developers

## Overview{% #overview %}

The Developers section contains reference materials for developing on Datadog. You may want to develop on Datadog if there is data you want to see in the product that you are not seeing. If this is the case, Datadog may already support the technology you need. See the table of commonly requested technologies to find the product or integration that may fulfill your needs.

## Commonly requested technologies{% #commonly-requested-technologies %}

If there is data you want to monitor with Datadog that you are not seeing, before building something custom, consider the following Datadog products and integrations:

| [](https://docs.datadoghq.com/integrations/openmetrics/)                  | **OpenMetrics**                     | The Agent includes the OpenMetrics check capable of scraping Prometheus endpoints. Metrics retrieved by this integration are considered [custom metrics](https://docs.datadoghq.com/metrics/custom_metrics/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [](https://docs.datadoghq.com/integrations/java)                          | **JMX Beans**                       | The JMX integration enables collection of metrics, logs, and traces from JVM-based applications. For example, the JMX integration is already used for official integrations like Solr, Tomcat, Cassandra, and more. Metrics generated through JMX-based integrations not natively supported by Datadog are considered [custom metrics](https://docs.datadoghq.com/metrics/custom_metrics/).                                                                                                                                                                                                                                                                                                                                  |
| [](https://docs.datadoghq.com/metrics/custom_metrics)                     | **Custom metrics and integrations** | Submit custom metrics for business stats using [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/) and the [API](https://docs.datadoghq.com/api/latest/metrics/). Datadog Agent integrations are Python files querying for metrics. All Agent code is open source, so it's possible to write your own [custom Agent check](https://docs.datadoghq.com/developers/custom_checks/) or [custom Agent integration](https://docs.datadoghq.com/developers/integrations/). The [integrations-extras GitHub repository](https://github.com/DataDog/integrations-extras) contains many community-developed custom integrations.                                                                                            |
| [](https://docs.datadoghq.com/logs)                                       | **Logs**                            | Use Log Management to view, monitor, and analyze the logs from your applications and infrastructure. The [Datadog Agent](https://docs.datadoghq.com/agent/logs/) provides advanced functionality for sending logs to your Datadog account, but you can also submit logs directly to the [Logs API](https://docs.datadoghq.com/api/latest/logs/).                                                                                                                                                                                                                                                                                                                                                                             |
| [](https://docs.datadoghq.com/tracing)                                    | **APM**                             | APM and Continuous Profiler provide out-of-the-box performance dashboards for web services, queues, and databases to monitor requests, errors, and latency. You can use the [Datadog Tracing Library](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/) for your environment and language, whether you are [tracing a proxy](https://docs.datadoghq.com/tracing/trace_collection/proxy_setup/) or tracing across [AWS Lambda functions](https://docs.datadoghq.com/serverless/distributed_tracing/) and hosts, using automatic instrumentation, dd-trace-api, or [OpenTelemetry](https://docs.datadoghq.com/tracing/trace_collection/open_standards/).                                                      |
| [](https://docs.datadoghq.com/infrastructure/process)                     | **Processes**                       | The [Processes integration](https://docs.datadoghq.com/integrations/process/) collects resource usage metrics for specific running processes on any host, such as CPU, memory, I/O, and others. Use [Live Process Monitoring](https://docs.datadoghq.com/infrastructure/process/) (which is like htop without having to SSH) to query across all your running processes.                                                                                                                                                                                                                                                                                                                                                     |
| [](https://docs.datadoghq.com/integrations/directory)                     | **Files and Directories**           | The Directory check measures the age of files, the number of files in a directory, or the size of a directory."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [](https://docs.datadoghq.com/synthetics)                                 | **Endpoint**                        | Use the Agent-based [HTTP check](https://docs.datadoghq.com/integrations/http_check/), or configure [Synthetic Monitoring](https://docs.datadoghq.com/synthetics/) from the Datadog application to validate if an endpoint or URL is running and accessible. Use either option to test both public and private endpoints. Combine with [Service Level Objectives, or SLOs](https://docs.datadoghq.com/service_management/service_level_objectives/) to define clear targets for performance.                                                                                                                                                                                                                                 |
| [](https://docs.datadoghq.com/network_monitoring)                         | **SNMP and Network Traffic**        | [Network Device Monitoring](https://docs.datadoghq.com/network_monitoring/devices/) enables you to collect [SNMP](https://docs.datadoghq.com/integrations/snmp/) (Simple Network Management Protocol) metrics emitted from network devices, such as routers, switches, and printers. [Network Performance Monitoring](https://docs.datadoghq.com/network_monitoring/performance/) tracks all network traffic in and out of a host, providing visibility into your network traffic between services, containers, availability zones, and any other tag in Datadog. Connection data at the IP, port, and PID levels is aggregated into application-layer dependencies between meaningful `source` and `destination` endpoints. |
| [](https://docs.datadoghq.com/integrations/#cat-cloud)                    | **Cloud Providers**                 | All the major Cloud providers ([AWS](https://docs.datadoghq.com/integrations/amazon_web_services/), [Azure](https://docs.datadoghq.com/integrations/azure/), [GCP](https://docs.datadoghq.com/integrations/google_cloud_platform/), [Alibaba](https://docs.datadoghq.com/integrations/alibaba_cloud/)) emit metrics through APIs. Use the [Datadog integration tiles](https://app.datadoghq.com/integrations) in your account to configure these integrations, which use Datadog servers to crawl for metrics.                                                                                                                                                                                                               |
| [](https://docs.datadoghq.com/integrations/windows_performance_counters/) | **Windows Performance Counters**    | Use the Windows performance counters integration to monitor performance and behavior in Windows environments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

If the solution you require is truly unavailable, you can contact [Datadog Support](https://docs.datadoghq.com/help/) to request a feature. You may also wish to create your own solution by using the reference materials in this section.

### Partners and the Datadog Marketplace{% #partners-and-the-datadog-marketplace %}

You may also be a partner who wants to build on Datadog and contribute to the [Datadog Marketplace](https://docs.datadoghq.com/developers/integrations/marketplace_offering) or to Datadog's community [integrations](https://docs.datadoghq.com/developers/integrations/).

- [Create an Agent-based Integration](https://docs.datadoghq.com/developers/integrations/agent_integration)
- [Create an API Integration](https://docs.datadoghq.com/developers/integrations/api_integration)
- [Create a Log Integration](https://docs.datadoghq.com/developers/integrations/log_integration)
- [Build a Marketplace Offering](https://docs.datadoghq.com/developers/integrations/marketplace_offering)

For more information about becoming a Datadog partner, navigate to the [Datadog Partner Network](https://www.datadoghq.com/partner/).

## Creating your own solution{% #creating-your-own-solution %}

Still not seeing the type of data that you need? Developers have several choices for sending unsupported data to Datadog.

- [**DogStatsD**](https://docs.datadoghq.com/developers/dogstatsd/) is a metrics aggregation service that accepts custom metrics, events, and service checks.

- [**Custom checks**](https://docs.datadoghq.com/developers/custom_checks/write_agent_check/) enable you to collect metrics from custom applications or systems. [Custom Agent checks](https://docs.datadoghq.com/developers/custom_checks/write_agent_check/) are suitable for many needs. For more advanced requirements like metrics preprocessing, you may choose to write an [OpenMetrics](https://docs.datadoghq.com/developers/custom_checks/prometheus/) check.

- [**Integrations**](https://docs.datadoghq.com/developers/integrations/) also enable you to collect metrics, events, and service checks from custom applications or systems. Integrations are reusable. You may keep your integration private, or write a public integration contributing to Datadog's [repository of community integrations](https://github.com/DataDog/integrations-extras) to be used by other developers.

### Custom check versus integration{% #custom-check-versus-integration %}

The primary difference between custom checks and integrations is that integrations are reusable components that can become part of the Datadog's ecosystem. They generally take more effort (time to develop) and are best suited for general use-cases such as application frameworks, open source projects, or commonly used software. For more unique scenarios, such as monitoring services that are not widely used outside your team or organization, writing a custom check may be the most efficient option.

However, you may choose to write an integration instead of a custom check if your particular use case requires you to publish and deploy your solution as a Python wheel (`.whl`). Metrics emitted through custom checks are considered custom metrics, which have a cost associated based on your subscription plan. However, once an integration gets accepted into the Datadog ecosystem, metrics that it emits are no longer considered custom metrics, and do not count against your custom metric count. For more information about how this might impact cost, see [Datadog Pricing](https://www.datadoghq.com/pricing/).

### How do I create an integration?{% #how-do-i-create-an-integration %}

Writing a public integration (that is, one that is part of Datadog's ecosystem, can be installed with the `datadog-agent integration` command, and is accepted into Datadog's [integrations-extras](https://github.com/DataDog/integrations-extras) or [integrations-core](https://github.com/DataDog/integrations-core) repositories) requires more work than a private integration. These integrations must pass all `ddev validate` steps, have usable tests, and undergo code review. You, as the code author, are the active maintainer of the integration and are responsible for ensuring its functionality.

The initial goal is to generate some code that collects the desired metrics in a reliable way, and to ensure that the general integration framework is in place. Start by writing the basic functionality as a custom Check, then fill in the framework details from [Create an Agent Integration](https://docs.datadoghq.com/developers/integrations/agent_integration).

Next, open a pull request against the [`integrations-extras` repository](https://github.com/DataDog/integrations-extras). This signals to Datadog that you're ready to start reviewing code together. Don't worry if you have questions about tests, Datadog internals, or other topicsâthe Datadog Ecosystems team is ready to help, and the pull request is a good place to go over those concerns.

Once the integration has been validated for functionality, framework compliance, and general code quality, it is merged into `integrations-extras` where it becomes part of the Datadog ecosystem.

When deciding how to send unsupported data to Datadog, the main considerations are effort (time to develop) and budget (cost of custom metrics). If you are trying to see data that Datadog doesn't support, start by deciding which method makes the most sense to start sending data:

| Type                | Effort | Custom Metrics | Language |
| ------------------- | ------ | -------------- | -------- |
| DogStatsD           | Lowest | Yes            | Any      |
| Custom check        | Low    | Yes            | Python   |
| Private integration | Medium | Yes            | Python   |
| Public integration  | High   | No             | Python   |

### Why create an integration?{% #why-create-an-integration %}

[Custom Checks](https://docs.datadoghq.com/help/) are great for occasional reporting, or in cases where the data source is either unique or very limited. For more general use cases - such as application frameworks, open source projects, or commonly-used software - it makes sense to write an integration.

Metrics reported from accepted integrations are not counted as custom metrics, and therefore don't impact your custom metric allocation. (Integrations that emit potentially unlimited metrics may still be considered custom.) Ensuring native support for Datadog reduces friction to adoption, and incentivizes people to use your product, service, or project. Also, being featured within the Datadog ecosystem is a great avenue for added visibility.

### What's the difference between a custom check and a service check?{% #whats-the-difference-between-a-custom-check-and-a-service-check %}

A [custom check](https://docs.datadoghq.com/developers/custom_checks/), also know as a custom Agent check, lets you send internal service data to Datadog. A [service check](https://docs.datadoghq.com/developers/service_checks/) is much simpler and lets you monitor the up or down status of the specific service. Even though these are both checks, they have different functionality and can be used separately and together based on your monitoring needs. For more information about each, see the [custom check](https://docs.datadoghq.com/developers/custom_checks/), and [service check](https://docs.datadoghq.com/developers/service_checks/) documentation sections.

### Sending metrics by integration types{% #sending-metrics-by-integration-types %}

- [DogStatsD: Overview of the features of DogStatsD, including setup, datagram format, and data submission.](https://docs.datadoghq.com/developers/dogstatsd)
- [Custom Agent Check: Learn how to report metrics, events, and service checks with your own custom check.](https://docs.datadoghq.com/developers/write_agent_check)
- [Custom OpenMetrics Check: Learn how to report your OpenMetrics check with a dedicated custom Agent Check.](https://docs.datadoghq.com/developers/prometheus)
- [Integrations: For more complex tasks, build a public or private Datadog integration. Public integrations can be shared with the community.](https://docs.datadoghq.com/developers/integrations/)

### Sending data by data types{% #sending-data-by-data-types %}

- [Custom Metrics: A deep-dive into custom metrics at Datadog. This section explains metrics types, what they represent, how to submit them, and how they are used throughout Datadog.](https://docs.datadoghq.com/metrics)
- [Events: Explore how to submit events to Datadog with custom Agent checks, DogStatsD, or the Datadog API.](https://docs.datadoghq.com/service_management/events/guides/)
- [Service Checks: Explore how to submit the up or down status of a specific service to Datadog.](https://docs.datadoghq.com/developers/service_checks)

## Engage with the developer community{% #engage-with-the-developer-community %}

- [Libraries: A list of official and community-contributed libraries for the Datadog API, DogStatsD client, APM & Continuous Profiler, and externally-supported community integrations for a wide variety of platforms.](https://docs.datadoghq.com/developers/libraries)
- [Guides: Read helpful articles covering technical details, code examples, and reference documentation.](https://docs.datadoghq.com/developers/guide/)

## Further Reading{% #further-reading %}

- [Learn about the Datadog API](https://docs.datadoghq.com/api/latest/)
- [Create great integration dashboards](https://datadoghq.dev/integrations-core/guidelines/dashboards/#best-practices)
- [DRUIDS, the design system that powers Datadog](https://www.datadoghq.com/blog/engineering/druids-the-design-system-that-powers-datadog/)
- [Introducing the Datadog Open Source Hub](https://www.datadoghq.com/blog/introducing-open-source-hub/)
