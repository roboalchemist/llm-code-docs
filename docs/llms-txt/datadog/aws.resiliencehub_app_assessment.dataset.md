# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.resiliencehub_app_assessment.dataset.md

---
title: Resilience Hub App Assessment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resilience Hub App Assessment
---

# Resilience Hub App Assessment

Resilience Hub App Assessment in AWS provides a detailed evaluation of an application's resilience based on defined policies and best practices. It analyzes architecture, resources, and configurations to identify potential risks and recommends improvements to meet recovery objectives. This helps ensure applications are better prepared for disruptions and aligned with organizational resilience goals.

```
aws.resiliencehub_app_assessment
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                                              | Description |
| ----------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| app_arn                 | core | string     | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:partition:resiliencehub:region:account:app/app-id. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference guide. |
| app_version             | core | string     | Version of an application.                                                                                                                                                                                                                                             |
| assessment_arn          | core | string     | Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:partition:resiliencehub:region:account:app-assessment/app-id. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference guide.      |
| assessment_name         | core | string     | Name of the assessment.                                                                                                                                                                                                                                                |
| assessment_status       | core | string     | Current status of the assessment for the resiliency policy.                                                                                                                                                                                                            |
| compliance              | core | string     | Application compliance against the resiliency policy.                                                                                                                                                                                                                  |
| compliance_status       | core | string     | Current status of the compliance for the resiliency policy.                                                                                                                                                                                                            |
| cost                    | core | json       | Cost for the application.                                                                                                                                                                                                                                              |
| drift_status            | core | string     | Indicates if compliance drifts (deviations) were detected while running an assessment for your application.                                                                                                                                                            |
| end_time                | core | timestamp  | End time for the action.                                                                                                                                                                                                                                               |
| invoker                 | core | string     | The entity that invoked the assessment.                                                                                                                                                                                                                                |
| message                 | core | string     | Error or warning message from the assessment execution                                                                                                                                                                                                                 |
| policy                  | core | json       | Resiliency policy of an application.                                                                                                                                                                                                                                   |
| resiliency_score        | core | json       | Current resiliency score for an application.                                                                                                                                                                                                                           |
| resource_errors_details | core | json       | A resource error object containing a list of errors retrieving an application's resources.                                                                                                                                                                             |
| start_time              | core | timestamp  | Starting time for the action.                                                                                                                                                                                                                                          |
| summary                 | core | json       | Indicates the AI-generated summary for the Resilience Hub assessment, providing a concise overview that highlights the top risks and recommendations. This property is available only in the US East (N. Virginia) Region.                                             |
| tags                    | core | hstore_csv |
| version_name            | core | string     | Version name of the published application.                                                                                                                                                                                                                             |
