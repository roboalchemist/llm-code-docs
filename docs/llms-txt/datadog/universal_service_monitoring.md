# Source: https://docs.datadoghq.com/universal_service_monitoring.md

---
title: Universal Service Monitoring
description: >-
  Monitor service health metrics across your entire stack without code
  instrumentation using Universal Service Monitoring and the Datadog Agent.
breadcrumbs: Docs > Universal Service Monitoring
source_url: https://docs.datadoghq.com/index.html
---

# Universal Service Monitoring

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Universal Service Monitoring (USM) provides visibility into your service health metrics universally across your entire stack *without having to instrument your code*. It relies solely on the presence of a configured Datadog Agent and [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging), and brings performance data about your uninstrumented services into views such as the Software Catalog and Service Map. USM also works with [Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/), Monitors, Dashboards, and SLOs.

{% video
   url="https://datadog-docs.imgix.net/images/universal_service_monitoring/usm-demo.mp4" /%}

## Setup{% #setup %}

For information about supported platforms and protocols, and for instructions on getting started, read [Setting Up Universal Service Monitoring](https://docs.datadoghq.com/universal_service_monitoring/setup/).

{% alert level="info" %}
**Preview: Additional protocols and encryption methods**
USM are in Preview for discovering cloud services and for decoding additional protocols and traffic encryption methods. For more information and to request access, read [Cloud Service Discovery and Additional Protocols](https://docs.datadoghq.com/universal_service_monitoring/additional_protocols/).
{% /alert %}

## Automatic service tagging{% #automatic-service-tagging %}

Universal Service Monitoring automatically detects services running in your infrastructure. If it does not find [unified service tags](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging), it assigns them a name based on one of the tags: `app`, `short_image`, `kube_container_name`, `container_name`, `kube_deployment`, `kube_service`.

To update the service's name, set up [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging).

{% image
   source="https://datadog-docs.imgix.net/images/universal_service_monitoring/automatic-service-tagging.abb499edcbadd65afb7d22c7f173697d.png?auto=format"
   alt="When Datadog automatically detects your services, the tag used for this is shown on the top of the service page" /%}

## Exploring your services{% #exploring-your-services %}

After you configure the Agent, wait about five minutes for your service to appear in the Software Catalog. Click the service to see the service details page. An operation name of `universal.http.server` or `universal.http.client` in the upper left indicates that the service telemetry comes from Universal Service Monitoring.

The `universal.http.server` operation name captures health metrics for inbound traffic to your service. The corresponding `universal.http.client` operation name represents outbound traffic to other destinations.

{% image
   source="https://datadog-docs.imgix.net/images/universal_service_monitoring/select_service_operation_cropped.9244a3c187db2d29e4ae87c8294ff84c.png?auto=format"
   alt="The operation dropdown menu on the Services tab shows the available operation names" /%}

After enabling Universal Service Monitoring, you can:

- Navigate to **APM** > **Software Catalog** or **APM** > **Service Map** to [visualize your services and their dependencies](https://docs.datadoghq.com/tracing/software_catalog/).

- Click into specific Service pages to see golden signal metrics (requests, errors, and duration), and correlate these against recent code changes with [Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/).

- Create [monitors](https://docs.datadoghq.com/monitors/types/apm/?tab=apmmetrics), [dashboards](https://docs.datadoghq.com/dashboards/), and [SLOs](https://docs.datadoghq.com/service_level_objectives/metric/) using the `universal.http.*` metrics.

## Further Reading{% #further-reading %}

- [Setting Up Universal Service Monitoring](https://docs.datadoghq.com/universal_service_monitoring/setup/)
- [Golden signals in seconds with Universal Service Monitoring](https://www.datadoghq.com/blog/universal-service-monitoring-datadog/)
- [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/)
- [Discover and catalog the services reporting to Datadog](https://docs.datadoghq.com/tracing/software_catalog/)
- [Learn more about services in Datadog](https://docs.datadoghq.com/tracing/services/service_page/)
- [Read about the Service Map](https://docs.datadoghq.com/tracing/services/services_map/)
- [Best practices for monitoring and remediating connection churn](https://www.datadoghq.com/blog/monitor-connection-churn-datadog/)
- [Improve developer experience and collaboration with Software Catalog](https://www.datadoghq.com/blog/software-catalog/)
