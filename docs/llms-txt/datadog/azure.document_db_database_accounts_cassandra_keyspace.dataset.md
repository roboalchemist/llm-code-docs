# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.document_db_database_accounts_cassandra_keyspace.dataset.md

---
title: Cosmos Database Accounts Cassandra Keyspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Cosmos Database Accounts Cassandra
  Keyspace
---

# Cosmos Database Accounts Cassandra Keyspace

This table represents the Cosmos Database Accounts Cassandra Keyspace resource from Microsoft Azure.

```
azure.document_db_database_accounts_cassandra_keyspace
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
