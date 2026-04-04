# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_web_trust_store.dataset.md

---
title: Workspaces Web Trust Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Workspaces Web Trust Store
---

# Workspaces Web Trust Store

This table represents the workspaces_web_trust_store resource from Amazon Web Services.

```
aws.workspaces_web_trust_store
```

## Fields

| Title                  | ID   | Type          | Data Type                                                           | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| associated_portal_arns | core | array<string> | A list of web portal ARNs that this trust store is associated with. |
| tags                   | core | hstore_csv    |
| trust_store_arn        | core | string        | The ARN of the trust store.                                         |
