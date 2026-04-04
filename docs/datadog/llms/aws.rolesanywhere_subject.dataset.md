# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rolesanywhere_subject.dataset.md

---
title: Rolesanywhere Subject
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Rolesanywhere Subject
---

# Rolesanywhere Subject

This table represents the rolesanywhere_subject resource from Amazon Web Services.

```
aws.rolesanywhere_subject
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                     | Description |
| ------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| created_at          | core | timestamp  | The ISO-8601 timestamp when the subject was created.                                          |
| credentials         | core | json       | The temporary session credentials vended at the last authenticating call with this subject.   |
| enabled             | core | bool       | The enabled status of the subject.                                                            |
| instance_properties | core | json       | The specified instance properties associated with the request.                                |
| last_seen_at        | core | timestamp  | The ISO-8601 timestamp of the last time this subject requested temporary session credentials. |
| subject_arn         | core | string     | The ARN of the resource.                                                                      |
| subject_id          | core | string     | The id of the resource                                                                        |
| tags                | core | hstore_csv |
| updated_at          | core | timestamp  | The ISO-8601 timestamp when the subject was last updated.                                     |
| x509_subject        | core | string     | The x509 principal identifier of the authenticating certificate.                              |
