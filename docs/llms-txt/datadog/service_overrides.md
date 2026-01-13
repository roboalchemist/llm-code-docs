# Source: https://docs.datadoghq.com/tracing/guide/service_overrides.md

---
title: Service Overrides
description: >-
  Understand service overrides and how to adapt your configuration when using
  inferred services to improve service dependency representation.
breadcrumbs: Docs > APM > Tracing Guides > Service Overrides
source_url: https://docs.datadoghq.com/guide/service_overrides/index.html
---

# Service Overrides

## Overview{% #overview %}

[Inferred services](https://docs.datadoghq.com/tracing/services/inferred_services) improve how Datadog represents service dependencies. This document explains the changes and how to adapt your configuration.

### Before inferred services{% #before-inferred-services %}

Datadog used to change service names of client spans (`span.kind:client`) to represent databases, queues, and third-party dependencies. For example, a client call from service `A` to a PostgreSQL database would be tagged as `service:postgres` or `service:A-postgres`. Changing the service name of spans is referred to as a **service override** in the rest of this guide. The initial service name is referred to as the **base service**.

In this approach, a span representing a client call from a service `auth-dotnet` to a PostgreSQL database would be tagged with `service:auth-dotnet-postgres`. In service maps, these dependencies were represented as separate services, as shown below:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/old_service_rep.ae208d66514e5f1c3f1c7d120d54eac1.png?auto=format"
   alt="Old Service Representation" /%}

### With inferred services{% #with-inferred-services %}

Dependencies are automatically inferred from span attributes collected on client spans (for example, `db.system`, `db.name`). The client span retains the base service name, and the database is inferred using other attributes. As a result, there's no need to change the `service` attribute on the client span anymore.

Using the previous example, the client span would now be tagged with the base service name `auth-dotnet`, and the database would be inferred from attributes like `db.name:user-db` and `db.system:postgres`. The service map representation would look like this:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/new_service_rep.1f5c49e4da5fe0abc3e21ffa13e78d83.png?auto=format"
   alt="New Service Representation" /%}

### Impact on service overrides{% #impact-on-service-overrides %}

With inferred service dependencies, service overrides might pollute service lists and maps. In service maps, you would see the following nodes in order:

1. The base service node, for example: `auth-dotnet`.
1. The service override node, for example: `auth-dotnet-postgres`.
1. The new inferred service node, for example: `user-db`.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/service_overrides_new_service_rep.572a7fb45cb48bceec55c75b495cf7f8.png?auto=format"
   alt="Service Overrides" /%}

The service override (`auth-dotnet-postgres`) breaks the direct connection between the base service and the inferred service. It is not useful anymore as the database dependency is now properly represented by the inferred service.

## How service overrides are set{% #how-service-overrides-are-set %}

#### Integration service overrides{% #integration-service-overrides %}

Datadog tracing libraries automatically set different service names on client spans to represent databases, queues, or third-party service dependencies in integrations. These types of service overrides are referred to as **integration service overrides** in the rest of the guide.

#### Custom service overrides{% #custom-service-overrides %}

Service names can also be set manually by users, for instance to gain visibility on specific components of the service (shared libraries, middleware layers). These types of service overrides are referred to as **custom service overrides** in the rest of the guide.

## How service overrides are represented in Datadog{% #how-service-overrides-are-represented-in-datadog %}

To give less importance to service overrides, these are treated differently visually speaking in various APM product pages.

#### In service and resource pages{% #in-service-and-resource-pages %}

Services that are service overrides are flagged as such in the service page header. On hover, find the list of base services where the service name is overridden, in a custom way, or as the default setting of the integration.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/service_overrides_service_page.a20588039bef602c9f54f1223fbab7d1.png?auto=format"
   alt="Service page overrides" /%}

#### In service maps{% #in-service-maps %}

In service maps, service overrides are represented as part of the edge going from the base service and the inferred service.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/service_overrides_service_map.536f2aeb0a6efd39f7e23bfee2b6e685.png?auto=format"
   alt="Service map overrides" /%}

#### In traces{% #in-traces %}

In the trace side panel, the client span header represents the call going from the base service to the inferred service. The top of the overview section also shows information about the base service name, the overridden service name, and the inferred entity name.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/service_overrides_traces.b5d6224e24094788ace5c2bbc4cbd141.png?auto=format"
   alt="Trace side panel service overrides" /%}

## Remove service overrides{% #remove-service-overrides %}

With inferred services, integration service overrides are no longer necessary and may clutter your service maps. You can remove them directly in Datadog. For step-by-step instructions, see [Service Override Removal](https://docs.datadoghq.com/tracing/services/service_override_removal).

## Glossary{% #glossary %}

##### Service override{% #service-override %}

A service name set for a span which differs from the default `DD_SERVICE` name. It can be set automatically by some Datadog integrations, or manually by users.

##### Base service{% #base-service %}

The default `DD_SERVICE` name.

## Further reading{% #further-reading %}

- [Remove Service Overrides](https://docs.datadoghq.com/tracing/services/service_override_removal)
- [Inferred services](https://docs.datadoghq.com/tracing/services/inferred_services)
