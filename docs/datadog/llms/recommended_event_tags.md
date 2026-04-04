# Source: https://docs.datadoghq.com/events/guides/recommended_event_tags.md

---
title: Best Practices For Tagging Events
description: Learn about recommended event tags and how to add them.
breadcrumbs: Docs > Event Management > Events Guides > Best Practices For Tagging Events
---

# Best Practices For Tagging Events

## Overview{% #overview %}

Datadog recommends using [unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) and the tags listed below on all your events for the following benefits:

- Identify potential issues faster
- Locate related events
- Filter more accurately in the [Events Explorer](https://docs.datadoghq.com/events/explorer), for example, to a specific environment

## Add tags{% #add-tags %}

You have multiple options to improve your tagging strategy for events:

- API: When using the [API](https://docs.datadoghq.com/api/latest/events/#post-an-event), you can add tags in the `tags` field.

- Monitor: When creating or editing a monitor, you can add recommended tags in the [**Say what's happening** section](https://docs.datadoghq.com/getting_started/monitors/#notify-your-services-and-your-team-members).

- Integrations: For more information about adding tags to integrations, see [Assigning Tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags) or the specific [integration](https://docs.datadoghq.com/integrations/).

You can add the following core attributes to your events:

| **Attribute** | **Description**                                                                                                                                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| env           | The environment in which the event is from, such as production, edge, or staging. This enables you to ensure that events from a lower environment are not confused as high priority.                                           |
| service       | The service name. Enables you to:- Know which service(s) are impacted if an event is related to an error- Pivot to the impacted service- Filter for all events with that service                                               |
| version       | The build or service version. This allows you to identify, for example, if an outage or event is related to a particular version.                                                                                              |
| host          | The host name. Enables you to:- Automatically enrich events at intake with additional host tags- Pivot to the **Host Infrastructure** and **Metrics** tabs in the [Events Explorer](https://app.datadoghq.com/event/explorer). |
| team          | The team that owns the event and are notified if need be.                                                                                                                                                                      |

## Further reading{% #further-reading %}

- [Learn about assigning tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags)
