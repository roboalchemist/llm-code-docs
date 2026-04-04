# Source: https://docs.datadoghq.com/data_observability.md

---
title: Data Observability Overview
description: >-
  Monitor data quality, performance, and cost with Data Observability to detect
  anomalies, analyze data lineage, and prevent issues affecting downstream
  systems.
breadcrumbs: Docs > Data Observability Overview
---

# Data Observability Overview

## Overview{% #overview %}

Data Observability (DO) helps data teams improve the reliability of data for analytics and AI applications and optimize the performance and costs of data pipelines. By unifying quality and jobs monitoring from production to consumption, teams can detect and remediate issues faster while optimizing cost and performance.

{% image
   source="https://datadog-docs.imgix.net/images/data_observability/do_suite_root_cause_analysis-1.4a5a0289a0077cfaf11272d9395c81ba.png?auto=format"
   alt="Datadog Data Observability end-to-end lineage with Spark job traces." /%}

## Key capabilities{% #key-capabilities %}

- **Detect failures early**: Catch bad data in warehouses like Snowflake, Databricks, and BigQuery through ML-powered monitors before dashboards, stakeholders, or AI models are impacted. Detect upstream pipeline failures in jobs run on Databricks, Spark, Airflow, or dbt.
- **Accelerate remediation**: Triage faster using end-to-end lineage to pinpoint root causes, assess incident blast radius, and route to the right owner. View which job in the pipeline failed or was delayed, and pivot into job execution traces and logs to determine why.
- **Optimize cost & performance**: Get visibility into the cost and efficiency of Spark and Databricks jobs and clusters, and use recommendations to optimize cluster configuration, code, and queries.
- **Unify end-to-end observability**: Correlate data quality, pipeline execution, and infrastructure signals in one place, spanning the entire data lifecycle.

## Get started{% #get-started %}

- [Quality Monitoring: Identify data issues before downstream BI and AI applications are impacted.](https://docs.datadoghq.com/data_observability/quality_monitoring/)
- [Jobs Monitoring: Observe, troubleshoot, and optimize jobs across your data pipelines.](https://docs.datadoghq.com/data_observability/jobs_monitoring/)
