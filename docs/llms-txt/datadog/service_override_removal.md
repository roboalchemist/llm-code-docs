# Source: https://docs.datadoghq.com/tracing/services/service_override_removal.md

---
title: Service Override Removal
description: Learn how to remove integration service overrides from Datadog.
breadcrumbs: Docs > APM > Service Observability > Service Override Removal
source_url: https://docs.datadoghq.com/services/service_override_removal/index.html
---

# Service Override Removal

This page explains how to remove integration service overrides, which use integration-specific service names to represent calls to other services. For conceptual background, see [Service Overrides](https://docs.datadoghq.com/tracing/guide/service_overrides) and [Inferred Services](https://docs.datadoghq.com/tracing/services/inferred_services).

## Prerequisites{% #prerequisites %}

Before you remove integration service overrides:

1. You must have the `apm_service_renaming_write` permission.
1. Your Datadog SDK version must support override removal. See SDK version requirements.

### SDK version requirements{% #sdk-version-requirements %}

| Language | Minimum supported version                                               |
| -------- | ----------------------------------------------------------------------- |
| .NET     | [3.4.0](https://github.com/DataDog/dd-trace-dotnet/releases/tag/v3.4.0) |
| Go       | [1.55.0](https://github.com/DataDog/dd-trace-go/releases/tag/v1.55.0)   |
| Java     | [1.20.0](https://github.com/DataDog/dd-trace-java/releases/tag/v1.20.0) |
| Node.js  | [4.16.0](https://github.com/DataDog/dd-trace-js/releases/tag/v4.16.0)   |
| PHP      | [0.94.1](https://github.com/DataDog/dd-trace-php/releases/tag/0.94.1)   |
| Python   | [1.19.0](https://github.com/DataDog/dd-trace-py/releases/tag/v1.19.0)   |
| Ruby     | [1.15.0](https://github.com/DataDog/dd-trace-rb/releases/tag/v1.15.0)   |

## Remove service overrides{% #remove-service-overrides %}

To remove service overrides in Datadog:

1. Navigate to **Software Catalog** > **Manage** > [**Manage Remapping Rules**](https://app.datadoghq.com/software/settings/service-remapping), and click **Manage Overrides**.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/SO_removal_page.f6f674f922ccf60cb2066057652308b1.png?auto=format"
      alt="Service Overrides page showing migration progress and removal options" /%}

1. For each override you plan to remove, review the related monitors and dashboards.

These assets reference the overridden service name and stop matching after removal. Update them to use the base service name (`service:<DD_SERVICE>`) to preserve functionality.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/service_overrides/SO_removal_page_sidepanel.c20c8dc302159b7ecc12eec56842a2d5.png?auto=format"
      alt="Service override side panel showing affected monitors and dashboards" /%}

1. Remove overrides individually or in bulk:

   - **Select specific overrides to remove**: Choose individual integration service overrides to remove. A **Migration Progress** bar shows your progress as you remove overrides. This action is reversible.

   - **Remove all overrides**: Select **Remove All Overrides** to permanently remove all integration service overrides and prevent future ones from appearing as APM usage increases. Custom service overrides are not affected.
Important alert (level: danger): Removing all integration service overrides is permanent and cannot be undone.

## Examples: Service naming after removal{% #examples-service-naming-after-removal %}

Removing service overrides changes how client spans are tagged and how downstream dependencies are identified. After overrides are removed, client spans use the calling service's name (`service:<DD_SERVICE>`) instead of the integration-specific name. The called dependency is identified using [`peer.*` attributes](https://docs.datadoghq.com/tracing/services/inferred_services/#peer-tags) (for example, database or queue).

**gRPC example:**

| Scenario                  | Service name                                              | Additional `peer.*` attributes |
| ------------------------- | --------------------------------------------------------- | ------------------------------ |
| With service overrides    | `service:my-service-grpc-client` or `service:grpc-client` | None                           |
| Without service overrides | `service:myservice`                                       | `@peer.service:otherservice`   |

**MySQL example:**

| Scenario                  | Service name                                  | Additional `peer.*` attributes                   |
| ------------------------- | --------------------------------------------- | ------------------------------------------------ |
| With service overrides    | `service:my-service-mysql` or `service:mysql` | None                                             |
| Without service overrides | `service:myservice`                           | `@peer.db.name:user-db`, `@peer.db.system:mysql` |

## Configuration-based removal{% #configuration-based-removal %}

You can also remove integration service overrides by setting an environment variable in your application configuration. This approach is useful if you cannot access the Datadog UI.

1. Confirm that your SDK meets the minimum version requirements.
1. Set the following environment variable:
   ```sh
   DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAMES_ENABLED=true
   ```

This ensures the `service` attribute always uses the base service name instead of appending the integration name (for example, `*-postgres`, `*-http-client`). Custom service overrides are not affected and must be removed directly in your code.

## Further reading{% #further-reading %}

- [Service Overrides](https://docs.datadoghq.com/tracing/guide/service_overrides)
- [Inferred Services](https://docs.datadoghq.com/tracing/services/inferred_services)
