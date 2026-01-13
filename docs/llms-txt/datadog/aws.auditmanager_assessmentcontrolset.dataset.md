# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.auditmanager_assessmentcontrolset.dataset.md

---
title: Auditmanager Assessment Control Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Auditmanager Assessment Control Set
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.auditmanager_assessmentcontrolset.dataset/index.html
---

# Auditmanager Assessment Control Set

This table represents the Auditmanager Assessment Control Set resource from Amazon Web Services.

```
aws.auditmanager_assessmentcontrolset
```

## Fields

| Title                 | ID   | Type   | Data Type                                                                                                   | Description |
| --------------------- | ---- | ------ | ----------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string |
| account_id            | core | string |
| controls              | core | json   | The list of controls that's contained with the control set.                                                 |
| delegations           | core | json   | The delegations that are associated with the control set.                                                   |
| description           | core | string | The description for the control set.                                                                        |
| id                    | core | string | The identifier of the control set in the assessment. This is the control set name in a plain string format. |
| manual_evidence_count | core | int64  | The total number of evidence objects that are uploaded manually to the control set.                         |
| roles                 | core | json   | The roles that are associated with the control set.                                                         |
| status                | core | string | The current status of the control set.                                                                      |
| system_evidence_count | core | int64  | The total number of evidence objects that are retrieved automatically for the control set.                  |
| tags                  | core | hstore |
