# Source: https://docs.datadoghq.com/events/correlation/intelligent.md

---
title: Intelligent Correlation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Event Management > Correlation > Intelligent Correlation
---

# Intelligent Correlation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Intelligent Correlation uses a Machine Learning modeling approach. It automatically correlates Datadog Monitor events on your behalf, using underlying telemetry gathered within Datadog, and other heuristics.

## Enable Intelligent Correlation{% #enable-intelligent-correlation %}

To get started:

1. Navigate to the [Correlation Settings](https://app.datadoghq.com/event/settings/correlation) page, and click [Preview Cases](https://app.datadoghq.com/event/correlation/rule/new?tab=intelligent).
1. From there you can preview the intelligent correlations that are created from your organization.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/intelligent/intelligent_config_updated.206b3e8b1a6c4852e85eb62dcc3c4dde.png?auto=format"
   alt="Configure intelligent correlation" /%}

## Receiving your first case{% #receiving-your-first-case %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/intelligent/intelligent_project.92e534a1f2761ca34e524227798cf01b.png?auto=format"
   alt="Event Management - Intelligent Correlation" /%}

When you navigate to [Event Correlations](https://app.datadoghq.com/event/correlation), find a project called **Intelligent Correlation**. From this project, you can see the cases created by Intelligent Correlation.

Intelligent Correlation generates cases automatically after it finds related alerts:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/intelligent/intelligent_correlation.018ea5c91b56a2112d63ed72968fb713.png?auto=format"
   alt="Case detail page of case created from intelligent correlation, showing related alerts in the Investigation tab" /%}



## Further Reading{% #further-reading %}

- [Learn about triaging and notifiying on cases](https://docs.datadoghq.com/service_management/events/correlation/triage_and_notify)
