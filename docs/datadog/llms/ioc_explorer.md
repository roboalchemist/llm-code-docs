# Source: https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/ioc_explorer.md

---
title: IOC Explorer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud SIEM > Triage and Investigate > IOC Explorer
---

# IOC Explorer

{% callout %}
The IOC Explorer is in Preview.
{% /callout %}

## Overview{% #overview %}

Indicators of Compromise (IOC) are evidence that your systems have experienced a security breach. With the [IOC Explorer](https://app.datadoghq.com/security/siem/ioc-explorer), you can view more details about compromises, and see related signals and logs.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/ioc_explorer.ee1fbf91b5642687be21082f3754fb96.png?auto=format"
   alt="The IOC Explorer, showing an IP address that has been flagged as an indicator of compromise" /%}

## Prerequisites{% #prerequisites %}

To view data in the IOC Explorer, all of the following must be true:

- Your organization must subscribe to Cloud SIEM.
- The indicator of compromise must be in a threat feed that was available to Datadog at the time of the log acquisition.
  - For more information on the threat intelligence feeds the IOC Explorer displays content from, see [Threat intelligence sources](https://docs.datadoghq.com/security/threat_intelligence/#threat-intelligence-sources).
- A log that has a matching entity in threat intelligence must be acquired.
- The time frame for the Explorer is fixed to the last 30 days. The log must be from within that time frame.

## Use the IOC Explorer{% #use-the-ioc-explorer %}

To access the IOC Explorer in Datadog, go to **Security** > **Cloud SIEM** > **Investigate** > [**IOC Explorer**](https://app.datadoghq.com/security/siem/ioc-explorer).

### Query and filter indicators of compromise{% #query-and-filter-indicators-of-compromise %}

You can write custom queries or apply filters to determine which indicators of compromise you can see in the explorer. You can query or filter by:

- Severity score
- [Entity type](https://docs.datadoghq.com/security/threat_intelligence/#entity-types)
- [Threat intelligence source](https://docs.datadoghq.com/security/threat_intelligence/#threat-intelligence-sources)
- [Threat intelligence category](https://docs.datadoghq.com/security/threat_intelligence/#threat-intelligence-categories)

Additionally, you can click a column heading in the Explorer to sort by that column's values.

### Get more context on an indicator of compromise{% #get-more-context-on-an-indicator-of-compromise %}

Click an indicator of compromise to open a side panel that contains additional information about it:

- When the indicator was first and last seen in a threat intelligence feedImportant alert (level: info): This is distinct from the first or last time the indicator was seen in a log.
- Any categories and ratings assigned to it, and the threat intelligence feeds associated with those ratings
- A breakdown of the indicator's severity score
- Signal matches, which you can view in Signals Explorer
- Related logs, which you can view in Log Explorer

## Understand severity scoring{% #understand-severity-scoring %}

It's important to have proper context for the severity score for an indicator, so you can properly prioritize investigations. For example, [IP addresses](https://docs.datadoghq.com/security/threat_intelligence/#ip-addresses-dynamic-and-transient) can be volatile and require frequent reassessments as a result.

In the IOC Explorer side panel, you can see the factors that contribute to the severity score. Severity score starts from a base score based on classification, and increases or decreases based on additional factors:

- **Classification**: The base score associated with the indicator's category and intent
- **Corroboration**: Whether the indicator appears on multiple threat intelligent feeds
- **Persistence**: How long threat intelligence feeds have been reporting on the indicator
- **Hosting Type**: Used for IP and domain entity types; evaluates whether the hosting infrastructure type is commonly used for attacks
- **Signal Activity**: Whether the indicator has been observed in Signals

## Further reading{% #further-reading %}

- [Threat Intelligence](https://docs.datadoghq.com/security/threat_intelligence/)
- [Bring Your Own Threat Intelligence](https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/threat_intelligence)
