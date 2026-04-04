# Source: https://docs.datadoghq.com/watchdog/impact_analysis.md

---
title: Watchdog Impact Analysis
description: >-
  Discover performance issues in your application impacting end users with
  Watchdog Impact Analysis.
breadcrumbs: Docs > Datadog Watchdogâ¢ > Watchdog Impact Analysis
---

# Watchdog Impact Analysis

## Overview{% #overview %}

Whenever Watchdog finds an APM anomaly, it simultaneously analyzes a variety of latency and error metrics that are submitted from the RUM SDKs to evaluate if the anomaly is adversely impacting any web or mobile pages visited by your users.

If Watchdog determines that the end-user experience is impacted, it provides a summary of the impacts in Watchdog APM Alert. This includes:

- A list of impacted RUM views
- An estimated number of impacted users
- A link to the list of impacted users, so that you can reach out to them, if needed.

{% video
   url="https://datadog-docs.imgix.net/images/watchdog/watchdog_impact_analysis.mp4" /%}

This feature is automatically enabled for all APM and RUM users. Whenever Watchdog APM alerts are associated with end-user impacts, affected **users** and **view paths** appear in the **Impacts** section of your Watchdog alerts. Click **users** to view the affected users' contact information if you need to reach out to them. Click **view paths** to access the impacted RUM views for additional information.

## Further Reading{% #further-reading %}

- [Understand the scope of user impact with Watchdog Impact Analysis](https://www.datadoghq.com/blog/watchdog-impact-analysis/)
- [Learn about Watchdog Insights for RUM](https://docs.datadoghq.com/real_user_monitoring/explorer/watchdog_insights/)
- [Connect RUM and Traces](https://docs.datadoghq.com/real_user_monitoring/connect_rum_and_traces/)
