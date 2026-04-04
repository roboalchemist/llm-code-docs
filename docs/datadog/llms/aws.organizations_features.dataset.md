# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.organizations_features.dataset.md

---
title: Organizations Features
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Organizations Features
---

# Organizations Features

This table represents the Organizations Features resource from Amazon Web Services.

```
aws.organizations_features
```

## Fields

| Title            | ID   | Type          | Data Type                                                                 | Description |
| ---------------- | ---- | ------------- | ------------------------------------------------------------------------- | ----------- |
| _key             | core | string        |
| account_id       | core | string        |
| enabled_features | core | array<string> | Specifies the features that are currently available in your organization. |
| organization_id  | core | string        | The unique identifier (ID) of an organization.                            |
| tags             | core | hstore_csv    |
