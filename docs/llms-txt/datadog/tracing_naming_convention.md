# Source: https://docs.datadoghq.com/tracing/trace_collection/tracing_naming_convention.md

---
title: Span Tag Semantics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > APM > Application Instrumentation > Span Tag Semantics
---

# Span Tag Semantics

## Overview{% #overview %}

[Datadog tracing libraries](https://docs.datadoghq.com/tracing/setup_overview/) provide out-of-the-box support for instrumenting a variety of libraries. These instrumentations generate spans to represent logical units of work in distributed systems. Each span consists of [span tags](https://docs.datadoghq.com/glossary/#span-tag) to provide additional information on the unit of work happening in the system. Naming conventions describe the name and content that can be used in span events.

{% alert level="info" %}
To find a comprehensive list of all span tags, reserved attributes, and naming conventions, see [Default Standard Attributes.](https://docs.datadoghq.com/standard-attributes/?product=apm)
{% /alert %}

## Span tag naming conventions{% #span-tag-naming-conventions %}

There are a variety of span tags to describe work happening in the system. For example, there are span tags to describe the following domains:

- **Reserved**: Attributes that are always present on all spans.
- **Core**: Instrumentation used and the kind of operation.
- **Network communications**: Work units corresponding to network communications.
- **HTTP requests**: HTTP client and server spans.
- **Database**: Database spans.
- **Message queue**: Messaging system spans.
- **Remote procedure calls**: Spans corresponding to remote procedure calls such as RMI or gRPC.
- **Errors**: Errors associated with spans.

For more information, see [Default Standard Attributes](https://docs.datadoghq.com/standard-attributes/?product=apm).

## Span tags and span attributes{% #span-tags-and-span-attributes %}

Span tags and span attributes are similar but distinct concepts:

- Span tags provides context related to the span. For instance, host or container tags on the infrastructure the service is running on.
- Span attributes are the content of the span, collected with automatic or manual instrumentation in the application.

### Span tags{% #span-tags %}

Span tags provide context related to the span. For instance, host or container tags on the infrastructure the service is running on. More examples include:

- **Host tags**: `hostname`, `availability-zone`, `cluster-name`
- **Container tags**: `container_name`, `kube_deployment`, `pod_name`

The list of added tags can be found for [Kubernetes](https://docs.datadoghq.com/containers/kubernetes/tag/), [Docker](https://docs.datadoghq.com/containers/docker/tag/) and [Amazon ECS](https://docs.datadoghq.com/containers/amazon_ecs/tags/).

Tags are usually enriched from other data sources like tags sourced from host, container, or Software Catalog. These tags are added to the span to describe the context. For example, tags might describe the properties of the host and the container the span is coming from, or the properties of the services the span is emitted from.

To find span tags in Datadog, go to the **Infrastructure** tab in the Trace side panel:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/attributes/span-tags.9f0573adbc35b36044a8d9b63fcdb1d8.png?auto=format"
   alt="Span tags on Infrastructure tab." /%}

### Span attributes{% #span-attributes %}

Span attributes are the content of the span, collected with automatic or manual instrumentation in the application. Some examples include:

- `http.url`
- `http.status_code`
- `error.message`

To query span attributes, use the `@` character followed by the attribute name in the search box. For example, `@http.url`.

To find span attributes in Datadog, go to the **Info** tab in the Trace side panel:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/attributes/span-attributes.41bf445be0955359b4f2eb569a60dffb.png?auto=format"
   alt="Span attributes on Info tab." /%}

## Further reading{% #further-reading %}

- [Learn more about standard attributes for Log Management](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention)
- [Data collected for RUM Browser](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/data_collected)
- [Learn how to explore your traces](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/)
