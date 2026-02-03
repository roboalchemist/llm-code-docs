# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.analyzer_finding.dataset.md

---
title: Analyzer Finding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Analyzer Finding
---

# Analyzer Finding

This table represents the Analyzer Finding resource from Amazon Web Services.

```
aws.analyzer_finding
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                            | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| analyzed_at            | core | timestamp  | The time at which the resource-based policy or IAM entity that generated the finding was analyzed.                                                                                                                                                                                   |
| analyzer_finding_arn   | core | string     |
| created_at             | core | timestamp  | The time at which the finding was created.                                                                                                                                                                                                                                           |
| error                  | core | string     | An error.                                                                                                                                                                                                                                                                            |
| finding_details        | core | json       | A localized message that explains the finding and provides guidance on how to address it.                                                                                                                                                                                            |
| finding_type           | core | string     | The type of the finding. For external access analyzers, the type is <code>ExternalAccess</code>. For unused access analyzers, the type can be <code>UnusedIAMRole</code>, <code>UnusedIAMUserAccessKey</code>, <code>UnusedIAMUserPassword</code>, or <code>UnusedPermission</code>. |
| id                     | core | string     | The ID of the finding to retrieve.                                                                                                                                                                                                                                                   |
| next_token             | core | string     | A token used for pagination of results returned.                                                                                                                                                                                                                                     |
| resource               | core | string     | The resource that generated the finding.                                                                                                                                                                                                                                             |
| resource_owner_account | core | string     | Tye Amazon Web Services account ID that owns the resource.                                                                                                                                                                                                                           |
| resource_type          | core | string     | The type of the resource identified in the finding.                                                                                                                                                                                                                                  |
| status                 | core | string     | The status of the finding.                                                                                                                                                                                                                                                           |
| tags                   | core | hstore_csv |
| updated_at             | core | timestamp  | The time at which the finding was updated.                                                                                                                                                                                                                                           |
