# Source: https://docs.datadoghq.com/events/pipelines_and_processors/date_remapper.md

---
title: Date Remapper
description: >-
  Define a custom date attribute as the official event timestamp for events with
  dates not in the default attribute list
breadcrumbs: Docs > Event Management > Pipelines and Processors > Date Remapper
---

# Date Remapper

As Datadog receives dates, it timestamps them using the value(s) from any of these default attributes:

- `timestamp`
- `date`
- `_timestamp`
- `Timestamp`
- `eventTime`
- `published_date`

If your events have dates in an attribute that are not in this list, use the date remapper processor to define their date attribute as the official event timestamp:

{% alert level="info" %}
The recognized date formats are: [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html), [UNIX (the milliseconds EPOCH format)](https://en.wikipedia.org/wiki/Unix_time), and [RFC3164](https://www.ietf.org/rfc/rfc3164.txt).
{% /alert %}

If your events don't have a timestamp that conforms to the formats listed above, use the grok processor to extract the epoch time from the timestamp to a new attribute. The date remapper uses the newly defined attribute.

To see how a custom date and time format can be parsed in Datadog, see [Parsing dates](https://docs.datadoghq.com/logs/log_configuration/parsing/?tab=matchers#parsing-dates).

**Notes**:

- As of ISO 8601-1:2019, the basic format is `T[hh][mm][ss]` and the extended format is `T[hh]:[mm]:[ss]`. Earlier versions omitted the T (representing time) in both formats.
- If multiple date remapper processors are applied to a given pipeline, the last one (according to the pipeline's order) is taken into account.

Example date remapper processor

{% image
   source="https://datadog-docs.imgix.net/images/logs/log_configuration/processor/date_remapper.8543cb319df2db268ec8d6a391c48087.png?auto=format"
   alt="Define a date attribute" /%}
