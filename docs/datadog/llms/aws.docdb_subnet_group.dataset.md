# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.docdb_subnet_group.dataset.md

---
title: DocDB Subnet Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DocDB Subnet Group
---

# DocDB Subnet Group

This table represents the DocDB Subnet Group resource from Amazon Web Services.

```
aws.docdb_subnet_group
```

## Fields

| Title                       | ID   | Type       | Data Type | Description |
| --------------------------- | ---- | ---------- | --------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| db_subnet_group_arn         | core | string     |
| db_subnet_group_description | core | string     |
| db_subnet_group_name        | core | string     |
| subnet_group_status         | core | string     |
| subnets                     | core | json       |
| tags                        | core | hstore_csv |
| vpc_id                      | core | string     |
