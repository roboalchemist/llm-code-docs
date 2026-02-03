# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeguru_profiler_finding.dataset.md

---
title: CodeGuru Profiler Finding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeGuru Profiler Finding
---

# CodeGuru Profiler Finding

This table represents the CodeGuru Profiler Finding resource from Amazon Web Services.

```
aws.codeguru_profiler_finding
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                 | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| id                       | core | string     | The universally unique identifier (UUID) of the recommendation report.                                                                                                                                                    |
| profile_end_time         | core | timestamp  | The end time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. |
| profile_start_time       | core | timestamp  | The start time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.                   |
| profiling_group_name     | core | string     | The name of the profiling group that is associated with the analysis data.                                                                                                                                                |
| tags                     | core | hstore_csv |
| total_number_of_findings | core | int64      | The total number of different recommendations that were found by the analysis.                                                                                                                                            |
