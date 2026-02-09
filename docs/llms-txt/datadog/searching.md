# Source: https://docs.datadoghq.com/events/explorer/searching.md

---
title: Search Syntax
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Event Management > Events Explorer > Search Syntax
---

# Search Syntax

## Overview{% #overview %}

Events search uses the [logs search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/). Like logs search, events search permits:

- `AND`, `OR`, and `-` operators
- Wildcards
- Escape characters
- Searching tags and facets with `key:value`
- Searching within attributes with the `@` prefix

## Example queries{% #example-queries %}

{% dl %}

{% dt %}
`source:(github OR chef)`
{% /dt %}

{% dd %}
Show events from GitHub OR Chef.
{% /dd %}

{% dt %}
`host:(i-0ade23e6 AND db.myapp.com)`
{% /dt %}

{% dd %}
Show events from `i-0ade23e6` AND `db.myapp.com`.
{% /dd %}

{% dt %}
`service:kafka`
{% /dt %}

{% dd %}
Show events from the `kafka` service.
{% /dd %}

{% dt %}
`status:error`
{% /dt %}

{% dd %}
Show events with an `error` status (supports: `error`, `warning`, `info`, `ok`).
{% /dd %}

{% dt %}
`availability-zone:us-east-1a`
{% /dt %}

{% dd %}
Show events in the `us-east-1a` AWS availability zone (AZ).
{% /dd %}

{% dt %}
`container_id:foo*`
{% /dt %}

{% dd %}
Show events from all containers with an ID beginning with `foo`.
{% /dd %}

{% dt %}
`@evt.name:foo`
{% /dt %}

{% dd %}
Show the events with attribute `evt.name` equal to `foo`.
{% /dd %}

{% /dl %}

See [Logs Search Syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/) for more details.

## Further reading{% #further-reading %}

- [Getting Started with Search in Datadog](https://docs.datadoghq.com/getting_started/search/)
- [Log Search Syntax](https://docs.datadoghq.com/logs/explorer/search_syntax)
