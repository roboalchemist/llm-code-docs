# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_connection_alias.dataset.md

---
title: WorkSpaces Connection Alias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WorkSpaces Connection Alias
---

# WorkSpaces Connection Alias

A WorkSpaces Connection Alias in AWS is a unique identifier that allows you to create a seamless, user-friendly URL for accessing Amazon WorkSpaces. It enables organizations to provide a consistent login experience by mapping custom domain names to WorkSpaces directories, simplifying access for end users while supporting cross-Region redirection and centralized management.

```
aws.workspaces_connection_alias
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                             | Description |
| ----------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| alias_id          | core | string     | The identifier of the connection alias.                                                                                                                               |
| associations      | core | json       | The association status of the connection alias.                                                                                                                       |
| connection_string | core | string     | The connection string specified for the connection alias. The connection string must be in the form of a fully qualified domain name (FQDN), such as www.example.com. |
| owner_account_id  | core | string     | The identifier of the Amazon Web Services account that owns the connection alias.                                                                                     |
| state             | core | string     | The current state of the connection alias.                                                                                                                            |
| tags              | core | hstore_csv |
