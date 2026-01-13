# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eks_insight.dataset.md

---
title: EKS Insight
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EKS Insight
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.eks_insight.dataset/index.html
---

# EKS Insight

This table represents the EKS Insight resource from Amazon Web Services.

```
aws.eks_insight
```

## Fields

| Title                     | ID   | Type      | Data Type                                                                                                                                         | Description |
| ------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string    |
| account_id                | core | string    |
| additional_info           | core | hstore    | Links to sources that provide additional context on the insight.                                                                                  |
| category                  | core | string    | The category of the insight.                                                                                                                      |
| category_specific_summary | core | json      | Summary information that relates to the category of the insight. Currently only returned with certain insights having category UPGRADE_READINESS. |
| description               | core | string    | The description of the insight which includes alert criteria, remediation recommendation, and additional resources (contains Markdown).           |
| id                        | core | string    | The ID of the insight.                                                                                                                            |
| insight_status            | core | json      | An object containing more detail on the status of the insight resource.                                                                           |
| kubernetes_version        | core | string    | The Kubernetes minor version associated with an insight if applicable.                                                                            |
| last_refresh_time         | core | timestamp | The time Amazon EKS last successfully completed a refresh of this insight check on the cluster.                                                   |
| last_transition_time      | core | timestamp | The time the status of the insight last changed.                                                                                                  |
| name                      | core | string    | The name of the insight.                                                                                                                          |
| recommendation            | core | string    | A summary of how to remediate the finding of this insight if applicable.                                                                          |
| resources                 | core | json      | The details about each resource listed in the insight check result.                                                                               |
| tags                      | core | hstore    |
