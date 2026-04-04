# Source: https://docs.datadoghq.com/dashboards/change_overlays.md

---
title: Change Overlays
description: >-
  Overlay your change events on graphs to correlate performance anomalies with
  changes in your application
breadcrumbs: Docs > Dashboards > Change Overlays
---

# Change Overlays

## Overview{% #overview %}

As teams iterate, deploy code, and make changes to their applications and services, identifying the exact change that caused a spike in errors, increased latency, or slower page load times can be challenging. Use Change Overlays to visualize changes on your dashboard like deployments or feature flags, and quickly correlate performance issues with them.

## Overlay changes on graphs{% #overlay-changes-on-graphs %}

To get started, click **Show Overlays** in the upper right corner of your dashboard. Now you can enable the [Change Tracking](https://docs.datadoghq.com/change_tracking/) timeline and change overlays on timeseries widgets.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/change_overlays/show_overlays_button.c35eea95f80d0fecea86a1f0dec83c52.png?auto=format"
   alt="Overlays button on dashboard header" /%}

When activated, the **Service** search bar displays the **Most Relevant** service by default. Datadog automatically selects the service most frequently referenced in the queries supporting the widgets on the dashboard.

Override the automatic service detection by using the search bar to find the service of interest.

All changes displayed on the change timeline and as overlays tie back to the selected service. Use the **Show On** dropdown to limit change overlays to relevant widgets, or shown them on all widgets on your dashboard.

To view additional details or take additional actions, click on a change overlay or change within the change timeline.

## FAQ{% #faq %}

### What are deployments changes scoped to?{% #what-are-deployments-changes-scoped-to %}

For APM deployments, an `env` must be specified. If you have an `env` or `datacenter` template variable set in your dashboard, deployments are filtered to match the selection. Otherwise, the `env` defaults to `prod`.

## Further Reading{% #further-reading %}

- [Getting started with APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/)
- [Monitor code deployments with Deployment Tracking in Datadog APM](https://www.datadoghq.com/blog/datadog-deployment-tracking/)
- [Release code confidently with Automatic Faulty Deployment Detection](https://www.datadoghq.com/blog/faulty-deployment-detection/)
- [Getting started with RUM Deployment Tracking](https://docs.datadoghq.com/real_user_monitoring/guide/setup-rum-deployment-tracking/?tab=npm)
- [Troubleshoot faulty frontend deployments with Deployment Tracking in RUM](https://www.datadoghq.com/blog/datadog-rum-deployment-tracking/)
- [Quickly spot and revert faulty deployments with Change Overlays](https://www.datadoghq.com/blog/change-overlays/)
