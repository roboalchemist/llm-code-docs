# Source: https://docs.datadoghq.com/incident_response/incident_management/analytics.md

# Source: https://docs.datadoghq.com/events/explorer/analytics.md

# Source: https://docs.datadoghq.com/events/correlation/analytics.md

---
title: Analytics from Cases and Events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Event Management > Correlation > Analytics from Cases and Events
---

# Analytics from Cases and Events

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Keep track of your teams' workload by charting and creating dashboards for events, alerts, and cases.

## Case Metrics{% #case-metrics %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/case_analytics.e25bf176b2cf72203b1ddd08702eb51a.png?auto=format"
   alt="Configure case analytics" /%}

You can query Case analytics in a variety of graph widgets to analyze team productivity and identify patterns in issues. Display analytic graphs on both Dashboards and Notebooks. To get started, in the widget configuration, select **Cases** in the data source dropdown under the *Graph your data* section.

The following widgets support Case Analytics:

- timeseries
- top list
- query value
- table
- tree map
- pie chart
- change
- list

## Event Metrics{% #event-metrics %}

Break down event metrics by source, host, service, and more. Find out where your problematic alerts are coming from and learn if your operational load is increasing or decreasing over time.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/event_analytics.c83f8dd3900b2320fd0fa86715d82ba2.png?auto=format"
   alt="Configure event analytics" /%}

To get started, in the widget configuration, select **Events** in the data source dropdown under the *Graph your data* section.

## Further Reading{% #further-reading %}

- [Learn about Event Correlation](https://docs.datadoghq.com/service_management/events/correlation/)
