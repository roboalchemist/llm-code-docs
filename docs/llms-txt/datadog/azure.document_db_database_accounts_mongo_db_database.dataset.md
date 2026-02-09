# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.document_db_database_accounts_mongo_db_database.dataset.md

---
title: Cosmos Database Accounts MongoDB Database
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Cosmos Database Accounts MongoDB
  Database
---

# Cosmos Database Accounts MongoDB Database

This table represents the Cosmos Database Accounts MongoDB Database resource from Microsoft Azure.

```
azure.document_db_database_accounts_mongo_db_database
```

## Fields

| Title             | ID   | Type       | Data Type                                                         | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| id                | core | string     | The unique resource identifier of the ARM resource.               |
| location          | core | string     | The location of the resource group to which the resource belongs. |
| name              | core | string     | The name of the ARM resource.                                     |
| options           | core | json       |
| resource          | core | json       |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | The type of Azure resource.                                       |
