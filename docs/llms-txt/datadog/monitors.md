# Source: https://docs.datadoghq.com/cloud_cost_management/cost_changes/monitors.md

# Source: https://docs.datadoghq.com/tracing/error_tracking/monitors.md

# Source: https://docs.datadoghq.com/monitors.md

---
title: Monitors
description: >-
  Create monitors, configure notifications and automations, and manage your
  monitors using the alerting platform
breadcrumbs: Docs > Monitors
source_url: https://docs.datadoghq.com/index.html
---

# Monitors

## Overview{% #overview %}

Datadog Monitors provide vital visibility into your infrastructure, enabling proactive detection and real-time response to performance issues and outages. By configuring monitors to track key metrics and thresholds, organizations can receive immediate alerts and address problems before they impact customers or cause system downtime.

Monitor critical changes by checking metrics, integration availability, and network endpoints through the Alerting platform. With Datadog Monitors you can:

- Simplify monitoring and response processes
- Enhance operational efficiency
- Optimize performance

## Get started{% #get-started %}

The fastest way to start with Datadog Monitors is with [Monitor templates](https://app.datadoghq.com/monitors/templates). These are a collection of monitors within Datadog that are preconfigured by Datadog and integration partners.

You can also build your own monitors from scratch in lab environments in the Learning Center, or in your application by following the Getting Started with Monitors guide.

- [Getting started with Monitors: Guide on how to build a metric based monitor](https://docs.datadoghq.com/getting_started/monitors/)
- [Create a monitor from Monitor Types](https://docs.datadoghq.com/monitors/types/)
- [Learning Center: Build a monitor in a sandbox lab environment](https://learn.datadoghq.com/courses/getting-started-monitors)

## Analyze aggregate data{% #analyze-aggregate-data %}

Data should be well-understood, granular, tagged by scope, and long-lived. Use different data types for alerts and diagnostics, based on the level of urgency. Instrument all applications and collect as much relevant data as possible for comprehensive measurements and observability of complex systems.

Measure the health of your applications and the state of your infrastructure with Datadog. Use data from across the Datadog platform to create alerts on potential issues.

## Alert on what matters{% #alert-on-what-matters %}

Set up [Monitor Notifications](https://docs.datadoghq.com/monitors/notify) to keep your team informed of issues and provide troubleshooting guidance. Route the notifications to the correct people, leverage template variables to include details, and attach snapshots when sending the alerts by email or Slack.

Reduce alerting fatigue so teams can focus on resolving alerts when it matters. Create [downtimes](https://docs.datadoghq.com/monitors/downtimes) to mute alerts during application maintenance.

## What's next{% #whats-next %}

Monitors and alerts are essential tools for ensuring the reliability, performance, and availability of IT systems and applications. They help maintain operational efficiency, improve user experience, and mitigate potential risks by enabling quick detection and response to issues before they escalate. Learn more about Monitor features:

1. [Schedule downtimes to mute monitors.](https://docs.datadoghq.com/monitors/downtimes/?tab=bymonitorname)
1. [Organize and manage monitors.](https://docs.datadoghq.com/monitors/manage)
1. [Investigate alerts through the status page.](https://docs.datadoghq.com/monitors/status/status_page)
1. [Resolve misconfigured monitors on the Monitor Quality page.](https://docs.datadoghq.com/monitors/quality/)

## Further reading{% #further-reading %}

- [Check out the latest Datadog Alerting releases! (App login required).](https://app.datadoghq.com/release-notes?category=Alerting)
- [Join an interactive session on creating effective monitors](https://dtdg.co/fe)
- [Monitoring 101: Alerting on what matters](https://www.datadoghq.com/blog/monitoring-101-alerting/)
- [Datadog Monitors API](https://docs.datadoghq.com/api/v1/monitors/)
- [Route your monitor alerts with Datadog monitor notification rules](https://www.datadoghq.com/blog/monitor-notification-rules/)
- [Catch and remediate ECS issues faster with default monitors and the ECS Explorer](https://www.datadoghq.com/blog/ecs-default-monitors/)
- [Optimizing Datadog at scale: Cost-efficient observability at Zendesk](https://www.datadoghq.com/blog/zendesk-cost-optimization)
