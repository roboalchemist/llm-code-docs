# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.auditmanager_assessmentframework.dataset.md

---
title: Auditmanager Assessment Framework
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Auditmanager Assessment Framework
---

# Auditmanager Assessment Framework

This table represents the Auditmanager Assessment Framework resource from Amazon Web Services.

```
aws.auditmanager_assessmentframework
```

## Fields

| Title           | ID   | Type       | Data Type                                                                      | Description |
| --------------- | ---- | ---------- | ------------------------------------------------------------------------------ | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| arn             | core | string     | The Amazon Resource Name (ARN) of the framework.                               |
| compliance_type | core | string     | The compliance type that the framework supports, such as CIS or HIPAA.         |
| control_sets    | core | json       | The control sets that are associated with the framework.                       |
| control_sources | core | string     | The control data sources where Audit Manager collects evidence from.           |
| created_at      | core | timestamp  | The time when the framework was created.                                       |
| created_by      | core | string     | The user or role that created the framework.                                   |
| description     | core | string     | The description of the framework.                                              |
| id              | core | string     | The unique identifier for the framework.                                       |
| last_updated_at | core | timestamp  | The time when the framework was most recently updated.                         |
| last_updated_by | core | string     | The user or role that most recently updated the framework.                     |
| logo            | core | string     | The logo that's associated with the framework.                                 |
| name            | core | string     | The name of the framework.                                                     |
| tags            | core | hstore_csv |
| type            | core | string     | Specifies whether the framework is a standard framework or a custom framework. |
