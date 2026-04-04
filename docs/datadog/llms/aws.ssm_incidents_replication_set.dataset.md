# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_incidents_replication_set.dataset.md

---
title: Systems Manager Incidents Replication Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Systems Manager Incidents
  Replication Set
---

# Systems Manager Incidents Replication Set

This table represents the Systems Manager Incidents Replication Set resource from Amazon Web Services.

```
aws.ssm_incidents_replication_set
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                | Description |
| ------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The Amazon Resource Name (ARN) of the replication set.                                                                                                                                   |
| created_by         | core | string     | Details about who created the replication set.                                                                                                                                           |
| created_time       | core | timestamp  | When the replication set was created.                                                                                                                                                    |
| deletion_protected | core | bool       | Determines if the replication set deletion protection is enabled or not. If deletion protection is enabled, you can't delete the last Amazon Web Services Region in the replication set. |
| last_modified_by   | core | string     | Who last modified the replication set.                                                                                                                                                   |
| last_modified_time | core | timestamp  | When the replication set was last updated.                                                                                                                                               |
| region_map         | core | string     | The map between each Amazon Web Services Region in your replication set and the KMS key that's used to encrypt the data in that Region.                                                  |
| status             | core | string     | The status of the replication set. If the replication set is still pending, you can't use Incident Manager functionality.                                                                |
| tags               | core | hstore_csv |
