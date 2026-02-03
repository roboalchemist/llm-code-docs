# Source: https://docs.datadoghq.com/tracing/guide/service_overrides.md

---
title: Overrides in APM
description: >-
  Understand service overrides, integration overrides, and how to adapt your
  configuration when using inferred services to improve service dependency
  representation.
breadcrumbs: Docs > APM > Tracing Guides > Overrides in APM
---

# Overrides in APM

## Overview{% #overview %}

Both integration overrides and service overrides change the service name of spans. The initial service name is referred to as the **base service**.

This page explains **integration overrides** and **service overrides** in APM.

### Integration overrides{% #integration-overrides %}

Datadog tracing libraries automatically set different service names on client spans to represent databases, queues, or third-party dependencies in integrations. These types of overrides are referred to as **integration overrides**. With inferred entities, integration overrides are not necessary to represent dependencies, and may pollute service lists and maps. For instructions on how to remove integration overrides, see [Integration Override Removal](https://docs.datadoghq.com/tracing/services/service_override_removal).

### Service overrides{% #service-overrides %}

You can manually set the service name on spans. This gives you visibility into specific components of the service, such as shared libraries and middleware layers. These types of overrides are referred to as **service overrides**.

## How overrides are represented{% #how-overrides-are-represented %}

Integration overrides and service overrides are represented similarly in APM.

#### In service and resource pages{% #in-service-and-resource-pages %}

Services that are overrides are flagged in the service page header. Hover over the flag to see the list of base services where the service name is overridden.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/service_overrides_service_page.a20588039bef602c9f54f1223fbab7d1.png?auto=format"
   alt="Service page overrides" /%}

#### In service maps{% #in-service-maps %}

In service maps, overrides are represented as part of the edge going from the base service and the inferred service.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/service_overrides_service_map.536f2aeb0a6efd39f7e23bfee2b6e685.png?auto=format"
   alt="Service map overrides" /%}

#### In traces{% #in-traces %}

In the trace side panel, the client span header represents the call going from the base service to the inferred service. The top of the overview section also shows information about the base service name, the overridden service name, and the inferred entity name.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/service_overrides_traces.b5d6224e24094788ace5c2bbc4cbd141.png?auto=format"
   alt="Trace side panel service overrides" /%}

## Removing integration overrides{% #removing-integration-overrides %}

You can remove integration overrides directly in the Datadog UI or with a configuration change. For more details, see [Integration Override Removal](https://docs.datadoghq.com/tracing/services/service_override_removal).

## Glossary{% #glossary %}

##### Integration override{% #integration-override %}

A service name set for a span which differs from the default `DD_SERVICE` name, set automatically by some Datadog integrations.

##### Service override{% #service-override %}

A service name set for a span which differs from the default `DD_SERVICE` name, set manually by users.

##### Base service{% #base-service %}

The default `DD_SERVICE` name.

## Further reading{% #further-reading %}

- [Remove Service Overrides](https://docs.datadoghq.com/tracing/services/service_override_removal)
- [Inferred services](https://docs.datadoghq.com/tracing/services/inferred_services)
