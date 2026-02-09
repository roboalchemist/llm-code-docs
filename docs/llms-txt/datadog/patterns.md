# Source: https://docs.datadoghq.com/events/correlation/patterns.md

---
title: Pattern-based Correlation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Event Management > Correlation > Pattern-based Correlation
---

# Pattern-based Correlation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Pattern-based correlation allows you to control how the events are correlated. Datadog also uses machine learning to automatically enrich your pattern with related Datadog Monitor events, using underlying telemetry gathered within Datadog and other heuristics.

To get you started, Datadog automatically suggests [pattern-based correlations](https://app.datadoghq.com/event/correlation) according to your environment. Click any of the recommendations to open the configuration for the recommended pattern. Configuration fields are pre-populated.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/pattern/recommended_patterns_preview.657232a8558adc65d9d2d7668d5307f5.png?auto=format"
   alt="Correlation recommended patterns with the preview panel showing potential cases the pattern would create" /%}

## Create a pattern{% #create-a-pattern %}

To create a pattern:

1. Navigate to [Correlation](https://app.datadoghq.com/event/correlation).
1. Click **+ Add a Pattern**, at the top of the Pattern table. This opens a pattern configuration page that displays out-of-the-box suggested patterns on the left side, and a pattern output preview on the right side.
1. You can adjust a suggested pattern by clicking **+ Continue With Pattern**. This takes you to the pre-populated configuration page for additional tuning. Or, you can choose to create your own pattern by clicking **+ Personalize From Scratch**

First, events are deduplicated to alert based on event aggregation key. Then, alerts are correlated to a case based on configuration.

{% video
   url="https://datadog-docs.imgix.net/images/service_management/events/correlation/correlation_helper.mp4" /%}
For more information on how to sends events with aggregation key, see [send events to datadog](https://docs.datadoghq.com/events/ingest/). Events without an aggregation key are deduped to one single alert within the timeframe.


### Suggested patterns{% #suggested-patterns %}

Suggested patterns are recommended based on your commonly used service and environment tags to help you get started with event correlation quickly.

### Configuration{% #configuration %}

From the [correlation configuration page](https://app.datadoghq.com/event/correlation/rule/new)

1. Select the event source you want to group on from the dropdown.
1. To exclude any events from the source defined above, add an event query in **Filter by these events or tags** to filter them out.
1. Add related events to associate changes or other supplementary events to support case investigation. Related events will be appended to a case but will not create new cases.
1. Define the grouping tags. Grouping tags are event facets. See the advanced settings section below if you don't see the tag from the dropdown. **Note**: you can create facets on both event attribute and tag. To learn more, see the [facets](https://docs.datadoghq.com/events/explorer/facets) documentation.

### Advanced settings (optional){% #advanced-settings-optional %}

1. Click **Show Advanced Settings**.

1. You can add grouping tags to correlate events and customize case title.

   {% dl %}
   
   {% dt %}
Add grouping tags
   {% /dt %}

   {% dd %}
   to add new grouping tags, this is same as adding [new event facet](https://docs.datadoghq.com/events/explorer/facets/#create-a-facet).
      {% /dd %}

   {% dt %}
Customize case title
   {% /dt %}

   {% dd %}
to create a template to replace the automatically generated case title. You can reference tag template variables using handlebars syntax, for example "{{tag.service}}", to include a comma-separated list of tag values.
   {% /dd %}

      {% /dl %}

1. Under **Advanced correlation logic**, you can specify the minimum number of correlated events it takes to create a case and update the timeframe.

**Timeframes**

Correlate alerts to a case for : The max duration that net new alerts will be added to a case

Deduplicate events for those alerts for : The max duration to reflect status transitions for current alerts which have been correlated, but continue to flap or have not resolved. Events are deduped to the corresponding alert in the existing case before opening a new case

## Preview pattern output{% #preview-pattern-output %}

Preview the possible patterns and cases your configuration would potentially create. The preview panel displays

- the total number of ingested events (limited to the first 1000 events).
- the number of alerts that would be deduped from events.
- the number of cases that would be created based on the configuration.

Use this data to preview the impact of your correlations and understand the expected output of a pattern.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/pattern/preview_pattern_output.40a04946925f0cca7ce27f5671dc214a.png?auto=format"
   alt="Configuration for pattern-based correlation highlighting the preview panel; panel shows the number of ingested events that match your configuration, how many of those events alert, how much deduplication would occur, and the number of cases that would result." /%}

**Notes**: the default title in the preview case is the first alert in correlation. After you save a pattern, the event management case title is intelligently generated.

## Select a Case Management destination{% #select-a-case-management-destination %}

1. From the *Project* dropdown menu, select from an existing Case to send your grouped events to.
1. (Optional) Add a tag to resulting cases.
1. Click **Save and Activate** to activate this pattern and group events into cases.

## Update existing pattern{% #update-existing-pattern %}

After you update an existing pattern, all live cases will stop processing. New events that match the pattern will create a new case.

## Further Reading{% #further-reading %}

- [Learn about triaging and notifiying on cases](https://docs.datadoghq.com/service_management/events/correlation/triage_and_notify)
