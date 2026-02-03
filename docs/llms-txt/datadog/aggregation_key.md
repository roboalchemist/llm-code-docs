# Source: https://docs.datadoghq.com/events/pipelines_and_processors/aggregation_key.md

---
title: Aggregation Key Processor
description: >-
  Generate custom aggregation keys based on event attributes or tags to enable
  effective deduplication and improve event correlations
breadcrumbs: Docs > Event Management > Pipelines and Processors > Aggregation Key Processor
---

# Aggregation Key Processor

Use the aggregation key processor to generate a custom aggregation key (`@aggregation_key`) based on event attributes or tags. For example, you can use the aggregation key processor to create a custom aggregation key based on an event's title and source tag. Events with matching values share the same key, enabling more effective deduplication and improving the quality of [Event Correlations](https://docs.datadoghq.com/events/correlation/).

**Notes**:

- Attributes must start with the `@` symbol and follow the path of the standard attribute as it appears in your JSON. For example, `@evt.category`.
- Tag keys must follow a valid tag key format outlined in [Getting Started with Tags](https://docs.datadoghq.com/getting_started/tagging/).
- A maximum of 5 attributes or tag keys can be added to generate an aggregation key.
- Events originating from different sources or integrations receive distinct aggregation keys.
- By default, existing aggregation keys are overwritten by this processor. Adjust the toggle to configure this behavior.

{% alert level="danger" %}
Aggregation keys are included by default in Datadog Monitor alerts and are not modified by the aggregation key processor. This ensures that monitor alert events retain their original keys and are not overwritten.
{% /alert %}

The aggregation key processor performs the following actions:

- Checks if any of the selected tag keys or attributes have values, if so, an aggregation key can be generated.
- If not, an aggregation key is not set on the processed event.
- If there are multiple values in the tag key, all values are sorted alphabetically and concatenated to generate the aggregation key.
- Based on these values, it generates a hash and adds the generated aggregation key to the event.
