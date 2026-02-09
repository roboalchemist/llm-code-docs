# Source: https://docs.datadoghq.com/mobile/widgets.md

# Source: https://docs.datadoghq.com/dashboards/widgets.md

---
title: Widgets
description: >-
  Dashboard building blocks for visualizing and correlating data across
  infrastructure with various chart types and displays.
breadcrumbs: Docs > Dashboards > Widgets
---

# Widgets

## Overview{% #overview %}

Dashboard widgets are visual representations of data. They serve as the building blocks for your [dashboards](https://docs.datadoghq.com/dashboards/) to visualize and correlate your data across your infrastructure. They can contain different types of information, such as graphs, images, logs, and statuses, to give you an overview of your systems and environments.

## Get started{% #get-started %}

The fastest way to onboard widgets relevant to your data is to clone a dashboard from the [preset list](https://app.datadoghq.com/dashboard/lists/preset/1) which includes dashboards created by other members of your organization and out-of-the-box templates for your installed integrations. After you clone a dashboard, you can customize widgets to your use case.

- [Getting Started with Dashboards: Walkthrough of building out a dashboard with widgets](https://docs.datadoghq.com/getting_started/dashboards/)
- [Dashboard Graph Widgets: Learning center course explaining how to create, configure, and use dashboard graph widgets](https://learn.datadoghq.com/courses/dashboard-graph-widgets)
- [Introduction to Dashboards: Learning center course explaining how to build a dashboard in a sandbox environment](https://learn.datadoghq.com/courses/intro-dashboards)

### Add a widget to your dashboard{% #add-a-widget-to-your-dashboard %}

To begin using widgets in your dashboards:

1. Navigate to the [Dashboards List](https://app.datadoghq.com/dashboard/lists/preset/1) in Datadog.
1. Click **New Dashboard** or select an existing dashboard to edit.
1. Click **Add Widget**. Choose from a variety of widget types such as timeseries, bar chart, table, or event stream.
1. Configure your widget:
   - Select data source: Choose metrics, logs, traces, or other data sources.
   - Customize visualization: Adjust display settings, units, and timeframes to fit your needs.
   - Add context: Use custom links, conditional formatting, and grouping for enhanced insights.
1. Save your dashboard and share it with your team or externally as needed.

For more information, see [Widget Configuration](https://docs.datadoghq.com/dashboards/widgets/configuration/) and explore the available [Widget Types](https://docs.datadoghq.com/dashboards/widgets/types/).

## Data sources{% #data-sources %}

Widgets can visualize data from multiple Datadog sources including:

- **APM Traces**: Application performance monitoring data
- **Events**: Custom events, deployments, and annotations
- **Logs**: Log events, log analytics, and log-based metrics
- **Metrics**: Infrastructure, application, and custom metrics
- **RUM**: Real User Monitoring and synthetic test data
- **SLOs**: Service Level Objectives and error budgets
- **Security**: Security signals and compliance data

## Common use cases{% #common-use-cases %}

{% collapsible-section %}
#### Infrastructure Monitoring

- Use **Timeseries** widgets for CPU, memory, and network metrics over time

- Use **Hostmap** widgets to visualize resource usage across your infrastructure

- Use **Top List** widgets to identify the most resource-intensive hosts or services

{% /collapsible-section %}

{% collapsible-section %}
#### Application Performance

- Use **Timeseries** widgets to track response times, error rates, and throughput

- Use **Service Summary** widgets for high-level service health overviews

- Use **Topology Map** widgets to visualize service dependencies and data flow

{% /collapsible-section %}

{% collapsible-section %}
#### Business Intelligence

- Use **Query Value** widgets for key performance indicators and business metrics

- Use **Funnel** widgets to track user conversion through your application

- Use **Retention** widgets to analyze user engagement and churn

{% /collapsible-section %}

{% collapsible-section %}
#### Incident Response

- Use **Alert Graph** widgets to show alert history and trends

- Use **Monitor Summary** widgets for current alert status across your infrastructure

- Use **Event Stream** widgets for real-time event monitoring

{% /collapsible-section %}

## Further reading{% #further-reading %}

- [Learn more about Dashboards](https://docs.datadoghq.com/dashboards/)
- [Learn about widget configuration options and best practice](https://docs.datadoghq.com/dashboards/widgets/configuration)
- [Explore all available widget types](https://docs.datadoghq.com/dashboards/widgets/types/)
