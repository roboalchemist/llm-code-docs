# Source: https://docs.datadoghq.com/data_observability/quality_monitoring.md

---
title: Quality Monitoring
description: >-
  Detect data freshness delays, unusual patterns, and column-level metric
  changes before they impact downstream systems.
breadcrumbs: Docs > Data Observability Overview > Quality Monitoring
---

# Quality Monitoring

## Overview{% #overview %}

Quality Monitoring detects issues such as data freshness delays, unusual data patterns, and changes in column-level metrics before they affect dashboards, machine learning models, or other downstream systems. It alerts you to potential problems and provides context to trace them back to upstream jobs or sources.

## Key capabilities{% #key-capabilities %}

With Quality Monitoring, you can:

- Detect delayed updates and unexpected row count behavior in your tables
- Surface changes in column-level metrics such as null counts or uniqueness
- Set up monitors using static thresholds or historical baselines
- Trace quality issues using lineage views that show upstream jobs and downstream impact

## Supported data sources{% #supported-data-sources %}

- [Snowflake](https://docs.datadoghq.com/data_observability/quality_monitoring/data_warehouses/snowflake)
- [Databricks](https://docs.datadoghq.com/data_observability/quality_monitoring/data_warehouses/databricks)
- [BigQuery](https://docs.datadoghq.com/data_observability/quality_monitoring/data_warehouses/bigquery)

- [Databricks](https://docs.datadoghq.com/data_observability/jobs_monitoring/databricks)
- [Airflow](https://docs.datadoghq.com/data_observability/jobs_monitoring/airflow)
- [dbt Core](https://docs.datadoghq.com/data_observability/jobs_monitoring/dbt/?tab=dbtcore)
- [dbt Cloud](https://docs.datadoghq.com/data_observability/jobs_monitoring/dbt/?tab=dbtcloud)
- [Spark on Kubernetes](https://docs.datadoghq.com/data_observability/jobs_monitoring/kubernetes)
- [Spark on Amazon EMR](https://docs.datadoghq.com/data_observability/jobs_monitoring/emr)
- [Spark on Google Dataproc](https://docs.datadoghq.com/data_observability/jobs_monitoring/dataproc)
- [Custom Jobs using OpenLineage](https://docs.datadoghq.com/data_observability/jobs_monitoring/openlineage)

- [Tableau](https://docs.datadoghq.com/data_observability/quality_monitoring/business_intelligence/tableau)
- [Sigma](https://docs.datadoghq.com/data_observability/quality_monitoring/business_intelligence/sigma)
- [Metabase](https://docs.datadoghq.com/data_observability/quality_monitoring/business_intelligence/metabase)
- [Power BI](https://docs.datadoghq.com/data_observability/quality_monitoring/business_intelligence/powerbi)

## Further reading{% #further-reading %}

- [Data Observability Overview](https://docs.datadoghq.com/data_observability/)
- [Jobs Monitoring](https://docs.datadoghq.com/data_observability/jobs_monitoring)
