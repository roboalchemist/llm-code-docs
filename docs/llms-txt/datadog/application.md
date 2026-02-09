# Source: https://docs.datadoghq.com/getting_started/application.md

---
title: Getting Started in Datadog
description: >-
  Overview of Datadog's UI navigation, key features including dashboards,
  monitors, integrations, and core platform capabilities.
breadcrumbs: Docs > Getting Started > Getting Started in Datadog
---

# Getting Started in Datadog

{% callout %}
##### Try Datadog Core Skills in the Learning Center

Learn without cost on real cloud compute capacity and a Datadog trial account. Start these hands-on labs to get up to speed with tagging, metrics, monitors, and dashboards.

[ENROLL NOW](https://learn.datadoghq.com/bundles/core-skills-learning-path)
{% /callout %}

## Overview{% #overview %}

This page provides a high-level overview of capabilities available on the [Datadog site](https://app.datadoghq.com).

{% alert level="info" %}
The Datadog site navigation varies based on the width of your browser. You can have up to three types of navigation. To change the navigation type, adjust your browser width.You can press `Cmd`/`Ctrl` + `K` to search for pages and entities, like dashboards and monitors, across Datadog.
{% /alert %}

## Infrastructure{% #infrastructure %}

The [infrastructure list](https://docs.datadoghq.com/infrastructure/list/) serves as a central view of all your infrastructure resources (hosts, containers, processes, etc.) and their associated metadata.

**Key capabilities:**

- Investigate infrastructure performance.
- Arrange, filter, and visualize hosts based on tags and metrics.
- Inspect hosts to review their tags, performance, health, and more.

Navigate to [**Infrastructure > Hosts**](https://app.datadoghq.com/infrastructure) in the app to get started. To learn more, read the [Infrastructure List documentation](https://docs.datadoghq.com/infrastructure/list/).

## Host and container maps{% #host-and-container-maps %}

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/application/host_map_2025.49ceb88f4df79f0a69bbc4576c1d3adb.png?auto=format"
   alt="Host Map Overview grouping by availability-zone." /%}

[Host and container maps](https://docs.datadoghq.com/infrastructure/hostmap/) give you a visual overview of all your hosts and containers, color-coding them by key metrics like CPU usage so you can spot issues.

**Key capabilities**:

- View your entire infrastructure at once as a visual map.
- Color-code by a variety of metrics to help you spot performance issues, and filter and group by tags and metadata.
- Drill down into individual hosts or containers to troubleshoot.

Navigate to [**Infrastructure > Host Map**](https://app.datadoghq.com/infrastructure/map) in the app to get started. To learn more, read the [Host and Container Maps documentation](https://docs.datadoghq.com/infrastructure/hostmap/).

## Log Management{% #log-management %}

[Datadog Log Management](https://docs.datadoghq.com/logs/) lets you send and process every log produced by your applications and infrastructure. You can observe your logs in real-time using the [Live Tail](https://docs.datadoghq.com/logs/explorer/live_tail/), without indexing them.

**Key capabilities**:

- Automatically collect logs from all services, applications, and platforms.
- View and search logs in real time and filter by things like service, host, and error type.
- Choose which logs to keep and for how long, reducing storage costs.

Navigate to [Logs](https://app.datadoghq.com/logs) in the app to get started. To learn more, read the [Log Management documentation](https://docs.datadoghq.com/logs/).

## APM{% #apm %}

[Datadog Application Performance Monitoring](https://docs.datadoghq.com/tracing/) (APM or tracing) provides you with deep insight into your application's performance side by side with your logs and infrastructure monitoring.

**Key capabilities**:

- Trace requests to an application from end to end across a distributed system.
- See performance bottlenecks by visualizing time spent at each step of the request.
- Visualize service dependencies and data flows with the Service Map.
- Correlate traces with corresponding logs, metrics, and user sessions for full-stack context.

Navigate to [APM](https://app.datadoghq.com/apm/home) in the app to get started. To learn more, read the [APM documentation](https://docs.datadoghq.com/tracing/).

## RUM & Session Replay{% #rum--session-replay %}

Datadog [Real User Monitoring](https://docs.datadoghq.com/real_user_monitoring/) (RUM) allows you to visualize and analyze real-time user activities and experiences across web and mobile applications. With [Session Replay](https://docs.datadoghq.com/session_replay/browser/), you can capture and view user sessions to better understand their behavior.

**Key capabilities**:

- Monitor performance across web browsers and mobile platforms (iOS, Android, React Native, Flutter, and more) with Core Web Vitals and Mobile Vitals.
- Track and troubleshoot errors with automated grouping, crash reporting, and suspect commit identification.
- Detect user frustration signals like rage clicks and error clicks to identify UX issues.
- Monitor feature flag performance and adoption.
- Correlate frontend issues with backend traces, logs, and infrastructure metrics for full-stack visibility.

Navigate to the [RUM explorer](https://app.datadoghq.com/rum/sessions) in the app to get started. To learn more, read the [RUM documentation](https://docs.datadoghq.com/real_user_monitoring/).

## Synthetic Monitoring{% #synthetic-monitoring %}

Datadog [Synthetic Monitoring](https://docs.datadoghq.com/synthetics/) allows you to create and run API, browser, mobile, and Network Path tests that proactively monitor simulated requests and actions from around the globe. These tests monitor your applications and APIs to detect performance issues and downtime before they impact users.

**Key capabilities**:

- Test business-critical API endpoints and user journeys.
- Detect errors, identify regressions, and automate rollbacks to prevent issues from surfacing in production.
- Find and alert on performance issues for users in various locations.

Navigate to [Synthetic Monitoring & Testing](https://app.datadoghq.com/synthetics/tests) in the app to get started. To learn more, read the [Synthetic Monitoring documentation](https://docs.datadoghq.com/synthetics/).

## Integrations{% #integrations %}

Use Datadog's 1,000 [integrations](https://www.datadoghq.com/product/platform/integrations/) to bring together all of the metrics and logs from your infrastructure and gain insights into your entire observability system.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/application/integrations-2025.bd0b07a067cba35409ac302506d7af16.png?auto=format"
   alt="Integrations" /%}

**Key capabilities**:

- Available integrations cover cloud technologies, incident response, data layers, security, AI, and more.
- After integrations have been configured, all data is treated the same throughout Datadog, whether it is living in a data center or in an online service.
- Build your own integration using the [developer documentation](https://docs.datadoghq.com/developers/integrations/).

Navigate to [Integrations](https://app.datadoghq.com/integrations) in the app to get started, or browse the list of integrations in the [documentation](https://docs.datadoghq.com/integrations/).

## Dashboards{% #dashboards %}

[Dashboards](https://docs.datadoghq.com/dashboards/) contain graphs with real-time performance metrics, unifying your view of data across metrics, logs, traces, and more.

**Key capabilities**:

- Start with out-of-the-box dashboards or build your own to suit your specific questions.
- Customize dashboards with drag-and-drop widgets, custom queries, and flexible layouts.
- Combine multiple data types (including metrics, logs, APM, and RUM) in one place and view data in real time.
- Annotate your graphs with comments or events for your team's context.

Navigate to the [Dashboard List](https://app.datadoghq.com/dashboard/lists) in the app to get started. To learn more, read the [Dashboards documentation](https://docs.datadoghq.com/dashboards/).

## Monitors{% #monitors %}

[Monitors](https://docs.datadoghq.com/monitors/) provide alerts and notifications based on metric thresholds, integration availability, network endpoints, and more.

- Create monitors using any metric reporting to Datadog.
- Build complex alerting logic using multiple trigger conditions.
- Send alerts to Slack, email, PagerDuty, and more, by adding`@` in alert messages to direct notifications to the right people.
- Schedule downtimes to suppress notifications for system shutdowns, offline maintenance, and more.

Navigate to the [Monitors List](https://app.datadoghq.com/monitors/manage) in the app to get started. To learn more, read the [Monitors documentation](https://docs.datadoghq.com/monitors/).

## Further Reading{% #further-reading %}

- [Frontend Engineer Learning Path](https://learn.datadoghq.com/bundles/frontend-engineer-learning-path)
- [Backend Engineer Learning Path](https://learn.datadoghq.com/bundles/backend-engineer-learning-path)
- [Site Reliability Engineer Learning Path](https://learn.datadoghq.com/bundles/site-reliability-engineer-learning-path)
- [Join an interactive session to build a solid foundation of Datadog](https://dtdg.co/fe)
- [Introducing the Datadog quick nav menu](https://www.datadoghq.com/blog/datadog-quick-nav-menu/)
