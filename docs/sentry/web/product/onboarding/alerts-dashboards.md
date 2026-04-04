---
---
title: Sentry Alerts and Dashboards
description: "Get started with Sentry alerts and dashboards to monitor key metrics, track issue trends, and gain real-time insights into your application's performance."
---

By the end of this guide you'll be able to create and customize Sentry alerts and dashboards to monitor key metrics, track issue trends, and gain real-time insights in to your application performance. If you get stuck anywhere, try [asking Sentry AI](/?askAI=true) or join our [Discord](https://discord.gg/sentry) community.

## 1. Alerting Strategy

After [integrating with Slack](https://sentry-docs-git-ob-alerts.sentry.dev/organization/integrations/notification-incidents/slack/) and adding your members and teams, it's time to create [Sentry alerts](/product/alerts/best-practices/) to ensure real-time issue detection, enabling faster debugging and reducing downtime. Configuring alerts using specific thresholds or conditions helps prioritize problems, improving system reliability and incident response time.

### Alert Recommendations

- **Error Alert (High-Frequency)** - Triggers when a new or existing production issue suddenly spikes in frequency.

- **Performance Alert** - Detects and alerts for specific performance metrics when they exceed a specified threshold.

- **Crash Rate Alert** - Monitors application stability by tracking the percentage of users experiencing crashes within a given time frame. 

- **Anomaly Detection** - Sentry can simplify your alerting needs by automatically detecting anomalies and proactively alerting you.

You can also create metric alerts for all you custom-instrumented transactions/spans based on key performance indicators such as [throughput](/product/alerts/alert-types/#performance).

## 2. Sentry Dashboards and Discover

Setting up Sentry dashboards is crucial for speeding up triage and offering a real-time view of critical issues, trends, and performance in your app. If an irregularity is observed, Sentry dashboards allow users to jump directly into troubleshooting with a few clicks.

### Recommended Dashboards

1. **Error Overview Dashboard** - Provides a high-level view of application health, showing you error trends, most frequent issues, and spikes in error occurrences.

2. **Performance Monitoring Dashboard** - Tracks transaction durations, slow API calls, and database query performance to identify bottlenecks.

3. **Mobile Crash Rate and Release Health Dashboard** - Monitors application stability and release impact by tracking crash rates across different versions.

4. **Critical Experience Dashboard** - Tracks errors or performance bottlenecks in your application's critical experiences. [See an example](https://sandbox.sentry.io/dashboard/126679/).

### Congratulations on completing the Sentry onboarding guide! 

You now have the foundation to make the most out of Sentry. Here are some highlights on what you've implemented:

- **Track errors** and performance by connecting projects and integrating your tools.

- **Add custom context** and performance instrumentation.

- **Stay on top of critical issues** with alerts.

- **Create dashboards** for insights, and filter or group issues for easy tracking.