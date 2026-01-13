# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeguru_profiler_profilinggroup.dataset.md

---
title: CodeGuru Profiler Profilinggroup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeGuru Profiler Profilinggroup
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.codeguru_profiler_profilinggroup.dataset/index.html
---

# CodeGuru Profiler Profilinggroup

This table represents the CodeGuru Profiler Profilinggroup resource from Amazon Web Services.

```
aws.codeguru_profiler_profilinggroup
```

## Fields

| Title                      | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                                       | Description |
| -------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string    |
| account_id                 | core | string    |
| agent_orchestration_config | core | json      | An <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig.html"> <code>AgentOrchestrationConfig</code> </a> object that indicates if the profiling group is enabled for profiled or not.                                                                                                                                                |
| arn                        | core | string    | The Amazon Resource Name (ARN) identifying the profiling group resource.                                                                                                                                                                                                                                                                                                        |
| compute_platform           | core | string    | The compute platform of the profiling group. If it is set to <code>AWSLambda</code>, then the profiled application runs on AWS Lambda. If it is set to <code>Default</code>, then the profiled application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. The default is <code>Default</code>. |
| created_at                 | core | timestamp | The time when the profiling group was created. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.                                                                                                                                                                                              |
| name                       | core | string    | The name of the profiling group.                                                                                                                                                                                                                                                                                                                                                |
| profiling_status           | core | json      | A <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus.html"> <code>ProfilingStatus</code> </a> object that includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile.                                      |
| tags                       | core | hstore    |
| updated_at                 | core | timestamp | The date and time when the profiling group was last updated. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.                                                                                                                                                                                |
