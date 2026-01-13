# Source: https://docs.datadoghq.com/dashboards.md

---
title: Dashboards
description: Visualize your data to gain insight
breadcrumbs: Docs > Dashboards
source_url: https://docs.datadoghq.com/index.html
---

# Dashboards

## Overview{% #overview %}

Dashboards provide real-time insights into the performance and health of systems and applications within an organization. They allow users to visually analyze data, track key performance indicators (KPIs), and monitor trends efficiently. With dashboards, teams can identify anomalies, prioritize issues, proactively detect problems, diagnose root causes, and ensure that reliability goals are met. Empower your teams to make informed decisions, optimize system operations, and drive business success by providing a centralized and user-friendly interface for monitoring and analyzing critical metrics and performance indicators.

- [Configure: Overview of the configuration options for dashboards](https://docs.datadoghq.com/dashboards/configure)
- [Dashboard List: Search, view, or create dashboards and lists](https://docs.datadoghq.com/dashboards/list)
- [Template Variable: Dynamically filter widgets in a dashboard](https://docs.datadoghq.com/dashboards/template_variables)
- [Datadog Clipboard](https://docs.datadoghq.com/incident_response/incident_management/datadog_clipboard/)
- [API: Manage dashboards programmatically](https://docs.datadoghq.com/api/latest/dashboards)

- [Widgets: Learn the configuration for different visualizations](https://docs.datadoghq.com/dashboards/widgets)
- [Querying: See the formatting options for graph queries](https://docs.datadoghq.com/dashboards/querying)
- [Functions: Modify metric queries and resulting graphs](https://docs.datadoghq.com/dashboards/functions)
- [Overlays: Automatically overlay change events on graphs](https://docs.datadoghq.com/dashboards/change_overlays)

## Get started{% #get-started %}

To create a dashboard:

1. Click **+New Dashboard** on the [Dashboard List](https://app.datadoghq.com/dashboard/lists) page or **New Dashboard** from the navigation menu.
1. Enter a dashboard name and choose a layout option.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/create-dashboard.eb5fec8e46e09ec3bb248f78c11453c3.png?auto=format"
   alt="Adding a new dashboard" /%}

{% dl %}

{% dt %}
Dashboards
{% /dt %}

{% dd %}
A grid-based layout, which can include a variety of objects such as images, graphs, and logs. They are commonly used as status boards or storytelling views which update in real time, and can represent fixed points in the past. They have a maximum width of 12 grid squares and also work well for debugging.
{% /dd %}

{% dt %}
Timeboards
{% /dt %}

{% dd %}
Automatic layouts that represent a single point in timeâeither fixed or real-timeâacross the entire dashboard. They are commonly used for troubleshooting, correlation, and general data exploration.
{% /dd %}

{% dt %}
Screenboards
{% /dt %}

{% dd %}
Dashboards with free-form layouts which can include a variety of objects such as images, graphs, and logs. They are commonly used as status boards or storytelling views that update in real time or represent fixed points in the past.
{% /dd %}

{% /dl %}

- [Getting Started with Dashboards](https://docs.datadoghq.com/getting_started/dashboards/)
- [Learning Course: Introduction to Dashboards](https://learn.datadoghq.com/courses/intro-dashboards)
- [Learning Course: Building Better Dashboards](https://learn.datadoghq.com/courses/building-better-dashboards)

## Refresh rate{% #refresh-rate %}

The refresh rate of a private dashboard depends on the time frame you are viewing. The shorter the time frame is, the more frequently the data is refreshed. Publicly shared dashboards refresh every thirty seconds, regardless of the selected time frame.

| Time frame | Refresh rate |
| ---------- | ------------ |
| 1 minute   | 10 seconds   |
| 2 minutes  | 10 seconds   |
| 5 minutes  | 10 seconds   |
| 10 minutes | 10 seconds   |
| 30 minutes | 20 seconds   |
| 1 hour     | 20 seconds   |
| 3 hours    | 1 minute     |
| 4 hours    | 1 minute     |
| 1 day      | 3 minutes    |
| 2 days     | 10 minutes   |
| 1 week     | 1 hour       |
| 1 month    | 1 hour       |
| 3 months   | 1 hour       |
| 6 months   | 1 hour       |
| 1 year     | 1 hour       |

## View dashboards on mobile devices{% #view-dashboards-on-mobile-devices %}

View your dashboards in a mobile-friendly format with the Datadog Mobile App, available on the [Apple App Store](https://apps.apple.com/app/datadog/id1391380318) and [Google Play Store](https://play.google.com/store/apps/details?id=com.datadog.app). The Mobile App comes equipped with mobile home screen widgets that allow you to monitor service health and infrastructure without opening the mobile app.

**Note**: To set up or edit a dashboard, you must log in to the Datadog browser UI. For more information on installing the app, see the [Datadog Mobile App](https://docs.datadoghq.com/mobile/) documentation.

## Further Reading{% #further-reading %}

{% callout %}
##### Try Creating Graph Widgets in the Datadog Learning Center

Explore timeseries, query value, top list, table, distribution, and pie chart widgets. Learn how to configure the widgets and develop an understanding of when each widget type should be utilized.

[ENROLL NOW](https://learn.datadoghq.com/courses/dashboard-graph-widgets)
{% /callout %}

{% callout %}
##### Try Creating Table, List, SLO, and Architecture Widgets in the Datadog Learning Center

Explore table, list, SLO, and architecture widgets. Learn how to track the metrics and performance of a web application and discover how to present important data.

[ENROLL NOW](https://learn.datadoghq.com/courses/discovering-table-list-widgets)
{% /callout %}

- [Check out the latest Datadog Dashboards releases! (App login required).](https://app.datadoghq.com/release-notes?category=Dashboards)
- [Share your Graphs outside of Datadog](https://docs.datadoghq.com/dashboards/sharing/)
- [Add Dashboard widgets to your clipboard](https://www.datadoghq.com/blog/datadog-clipboard/)
- [The new Datadog dashboards experience](https://www.datadoghq.com/blog/datadog-dashboards/)
- [Create great integration dashboards](https://datadoghq.dev/integrations-core/guidelines/dashboards/#best-practices)
- [Join an interactive session on better visualizations with Dashboards](https://dtdg.co/fe)
