# Source: https://clickhouse.ferndocs.com/cloud/get-started/query-insights.md

---
sidebar_title: Query insights
slug: /cloud/get-started/query-insights
description: >-
  Visualize system.query_log data to simplify query debugging and performance
  optimization
keywords:

- query insights
- query log
- query log ui
- system.query_log insights
title: Query insights
doc_type: guide

---

The **Query Insights** feature makes ClickHouse's built-in query log easier to use through various visualizations and tables. ClickHouse's `system.query_log` table is a key source of information for query optimization, debugging, and monitoring overall cluster health and performance.

## Query overview [#query-overview]

After selecting a service, the **Monitoring** navigation item in the left sidebar should expand to reveal a new **Query insights** sub-item. Clicking on this option opens the new Query insights page:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/2eca77ef7d93ccb34a92bf2744681afe54c94f44f1efdcff790311703b726b0d/images/cloud/sqlconsole/insights_overview.png" alt="Query Insights UI Overview"/>

## Top-level metrics [#top-level-metrics]

The stat boxes at the top represent some basic top-level query metrics over the selected period of time. Beneath it, we've exposed three time-series charts representing query volume, latency, and error rate broken down by query kind (select, insert, other) over a selected time window. The latency chart can be further adjusted to display p50, p90, and p99 latencies:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b30fe51e812197e2e6f7b6beb4561fd1f2bef2ea719e378e2df920431afd52d4/images/cloud/sqlconsole/insights_latency.png" alt="Query Insights UI Latency Chart"/>

## Recent queries [#recent-queries]

Beneath the top-level metrics, a table displays query log entries (grouped by normalized query hash and user) over the selected time window:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/407412d21fa233f77afc5a97c12f8303f692c217f4109d105c0fcdbe0bbc18b0/images/cloud/sqlconsole/insights_recent.png" alt="Query Insights UI Recent Queries Table"/>

Recent queries can be filtered and sorted by any available field. The table can also be configured to display or hide additional fields such as tables, p90, and p99 latencies.

## Query drill-down [#query-drill-down]

Selecting a query from the recent queries table will open a flyout containing metrics and information specific to the selected query:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c5ac3af53fceca8bc28de196c9d0d7840f67c2bb41dacf64311ad56392cb6d83/images/cloud/sqlconsole/insights_drilldown.png" alt="Query Insights UI Query Drill down"/>

As we can see from the flyout, this particular query has been run more than 3000 times in the last 24 hours. All metrics in the **Query info** tab are aggregated metrics, but we can also view metrics from individual runs by selecting the **Query history** tab:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e72eafcf7fef2081534ecb597b0053e0a6669bdcc030e0279b261d8617f70f10/images/cloud/sqlconsole/insights_query_info.png" alt="Query Insights UI Query Information"/>

<br />

From this pane, the `Settings` and `Profile Events` items for each query run can be expanded to reveal additional information.
