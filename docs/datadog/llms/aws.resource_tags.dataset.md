# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.resource_tags.dataset.md

---
title: Resource Tags
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resource Tags
---

# Resource Tags

This table represents the Resource Tags resource from Amazon Web Services.

```
aws.resource_tags
```

## Fields

| Title      | ID   | Type       | Data Type | Description |
| ---------- | ---- | ---------- | --------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| arn        | core | string     |
| region     | core | string     |
| service    | core | string     |
| tags       | core | hstore_csv |
