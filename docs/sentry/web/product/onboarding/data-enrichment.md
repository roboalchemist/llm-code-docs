---
---
title: Data Enrichment
description: "Instrument the data you send to Sentry for easier grouping and filtering."
---

By now, you should have events flowing into your project(s). If you don't, start [here](/product/onboarding/).This guide will cover essential topics such as data enrichment, filtering unwanted events, and issue grouping. If you get stuck anywhere, please [Ask Sentry AI](https://sentry.zendesk.com/hc/en-us?askAI=true) or join our [Discord](https://discord.gg/sentry) community.

## Step 1: Enriching Your Event Data

### Adding Custom Context

There are several ways you can [enrich your data](/platform-redirect?next=/enriching-events/) in Sentry. Adding tags, custom contexts, and breadcrumbs will help organize, filter, and analyze errors more effectively. See this quick walkthrough on adding a tag:

## Step 2: Ensure Your Traces Are Instrumented Properly

### Verify That Sentry's Tracing Auto-Instrumentation is Set Up Optimally

Once Tracing is turned on, Sentry will auto-instrument your spans. If any additional instrumentation is needed, look into your platform's [instrumentation documentation](/platform-redirect?next=/tracing/instrumentation/automatic-instrumentation/) for additional options. 

Learn how [Sentry helps create actionable insights](/product/sentry-basics/performance-monitoring/#ways-to-monitor-performance-in-sentry) from your performance data.

### Custom Instrumentation For Any Additional Performance Metrics

For any gaps in Sentry's auto-instrumentation, you can use [custom instrumentation](/platform-redirect/?next=/tracing/instrumentation/custom-instrumentation/) to collect additional spans and span metrics. This enables you to focus your instrumentation on critical areas of your application to optimize you configuration. For example, if you have an e-commerce app, you may want to track pageloads and checkout errors to pinpoint issues by provider, region, or app version.

The video below is an example of what's possible with custom instrumentation: 

## Step 3: Filtering Unwanted events

Filtering out events that are not actionable or expected during normal operations is essential for maintaining a clean and relevant issue tracking system. Issue and trace filtering are project-specific and can be accomplished [within the SDK](/platform-redirect?next=/configuration/filtering/#using-before-send) or the server via [inbound filters](/concepts/data-management/filtering/):

<div style={{marginBottom:'40px'}}></div>

Transactions/spans must be filtered out using `beforeSendSpan` and/or `beforeSendTransaction` [within the SDK](/platform-redirect?next=/configuration/filtering/#using-before-send).

## Step 4: Grouping Your issues

If you are noticing individual errors that should be grouped together, you can customize your issue grouping algorithm. Additional grouping customization can be accomplished via [issue merging](/concepts/data-management/event-grouping/merging-issues/) or Sentry's [custom grouping](/concepts/data-management/event-grouping/).

