# Source: https://docs.datadoghq.com/events/pipelines_and_processors/category_processor.md

---
title: Category Processor
description: >-
  Add a new attribute to events matching a search query to create groups for
  analytical views
breadcrumbs: Docs > Event Management > Pipelines and Processors > Category Processor
---

# Category Processor

Use the category processor to add a new attribute (without spaces or special characters in the new attribute name) to an event matching a provided search query. Then, use categories to create groups for an analytical view (for example, URL groups, machine groups, environments, and response time buckets).

**Notes**:

- The syntax of the query is the one in the Event Explorer search bar. This query can be done on any event attribute or tag, whether it is a facet or not. Wildcards can also be used inside your query.
- Once the event has matched one of the processor queries, it stops. Make sure they are properly ordered in case an event could match several queries.
- The names of the categories must be unique.
- Once defined in the category processor, you can map categories to status using the status remapper

Example category processor to categorize your web access events based on the status code range value (`"OK" for a response code between 200 and 299, "Notice" for a response code between 300 and 399, ...`) add this processor:

{% image
   source="https://datadog-docs.imgix.net/images/logs/log_configuration/processor/category_processor.021b511f06b4c1450e6af7ad34f6c4bc.png?auto=format"
   alt="category processor" /%}

This processor produces the following result:

{% image
   source="https://datadog-docs.imgix.net/images/logs/log_configuration/processor/category_processor_result.9540302809d1572f6ca9c3ae7cb268e2.png?auto=format"
   alt="category processor result" /%}
