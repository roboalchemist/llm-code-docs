# Source: https://docs.datadoghq.com/events/explorer/attributes.md

---
title: Reserved Attributes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Event Management > Events Explorer > Reserved Attributes
---

# Reserved Attributes

## Overview{% #overview %}

Attributes are used for facets and tags, which are then used to filter and search in the Events Explorer.

## List of reserved attributes{% #list-of-reserved-attributes %}

This list describes automatically ingested reserved attributes with events.

| Attribute | Description                                                                                                                                                                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host`    | The name of the originating host as defined in metrics. Datadog automatically retrieves corresponding host tags from the matching host in Datadog and applies them to your events. The Agent sets this value automatically.                          |
| `source`  | This corresponds to the integration name, or the technology from which the event originated. When it matches an integration name, Datadog automatically installs the corresponding parsers and facets. For example: `nginx`, `postgresql`, and more. |
| `status`  | This corresponds to the level or severity of an event.                                                                                                                                                                                               |
| `service` | The name of the application or service generating the events.                                                                                                                                                                                        |
| `message` | By default, Datadog ingests the value of the `message` attribute as the body of the event entry.                                                                                                                                                     |

To search a tag that has the same key as a reserved attribute, use the `tags` search syntax. Example: `tags:("status:<status>")`

To create a facet on a tag that has the same key as a reserved attribute:

1. Use the [Remapper processor](https://docs.datadoghq.com/logs/log_configuration/processors/?tab=ui#remapper) to remap the tag to another tag or attribute.
1. Create a [facet](https://docs.datadoghq.com/events/explorer/facets) on the new tag/attribute.

## Further reading{% #further-reading %}

- [Learn about Event facets](https://docs.datadoghq.com/events/explorer/facets)
- [Log processing pipelines](https://docs.datadoghq.com/logs/processing/pipelines)
