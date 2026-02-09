# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.servicecatalog_attribute_group.dataset.md

---
title: Service Catalog AppRegistry Attribute Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Service Catalog AppRegistry
  Attribute Group
---

# Service Catalog AppRegistry Attribute Group

Service Catalog AppRegistry Attribute Group in AWS is a resource that lets you define and manage metadata for applications. An attribute group is a collection of key-value pairs that describe application attributes, such as environment, owner, or compliance details. This helps organize and provide context for applications registered in AppRegistry, making it easier to manage resources, track metadata, and integrate with governance or automation processes.

```
aws.servicecatalog_attribute_group
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                                           | Description |
| ---------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| arn              | core | string     | The Amazon resource name (ARN) that specifies the attribute group across services.                                                                                  |
| attributes       | core | string     | A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.                     |
| created_by       | core | string     | The service principal that created the attribute group.                                                                                                             |
| creation_time    | core | timestamp  | The ISO-8601 formatted timestamp of the moment the attribute group was created.                                                                                     |
| description      | core | string     | The description of the attribute group that the user provides.                                                                                                      |
| id               | core | string     | The identifier of the attribute group.                                                                                                                              |
| last_update_time | core | timestamp  | The ISO-8601 formatted timestamp of the moment the attribute group was last updated. This time is the same as the creationTime for a newly created attribute group. |
| name             | core | string     | The name of the attribute group.                                                                                                                                    |
| tags             | core | hstore_csv |
