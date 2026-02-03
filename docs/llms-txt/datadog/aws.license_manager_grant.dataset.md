# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.license_manager_grant.dataset.md

---
title: License Manager Grant
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > License Manager Grant
---

# License Manager Grant

This table represents the license_manager_grant resource from Amazon Web Services.

```
aws.license_manager_grant
```

## Fields

| Title                 | ID   | Type          | Data Type                                | Description |
| --------------------- | ---- | ------------- | ---------------------------------------- | ----------- |
| _key                  | core | string        |
| account_id            | core | string        |
| grant_arn             | core | string        | Amazon Resource Name (ARN) of the grant. |
| grant_name            | core | string        | Grant name.                              |
| grant_status          | core | string        | Grant status.                            |
| granted_operations    | core | array<string> | Granted operations.                      |
| grantee_principal_arn | core | string        | The grantee principal ARN.               |
| home_region           | core | string        | Home Region of the grant.                |
| license_arn           | core | string        | License ARN.                             |
| options               | core | json          | The options specified for the grant.     |
| parent_arn            | core | string        | Parent ARN.                              |
| status_reason         | core | string        | Grant status reason.                     |
| tags                  | core | hstore_csv    |
| version               | core | string        | Grant version.                           |
