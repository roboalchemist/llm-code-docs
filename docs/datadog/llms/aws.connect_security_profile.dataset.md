# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_security_profile.dataset.md

---
title: Connect Security Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Security Profile
---

# Connect Security Profile

A Connect Security Profile in AWS defines permissions and access controls for users within an Amazon Connect instance. It determines what actions agents or administrators can perform, such as managing contacts, configuring settings, or accessing reports. Security profiles help enforce role-based access control, ensuring users only have the level of access required for their responsibilities.

```
aws.connect_security_profile
```

## Fields

| Title                                     | ID   | Type          | Data Type                                                                                                                                        | Description |
| ----------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                      | core | string        |
| account_id                                | core | string        |
| allowed_access_control_hierarchy_group_id | core | string        | The identifier of the hierarchy group that a security profile uses to restrict access to resources in Amazon Connect.                            |
| allowed_access_control_tags               | core | hstore        | The list of tags that a security profile uses to restrict access to resources in Amazon Connect.                                                 |
| arn                                       | core | string        | The Amazon Resource Name (ARN) for the security profile.                                                                                         |
| description                               | core | string        | The description of the security profile.                                                                                                         |
| hierarchy_restricted_resources            | core | array<string> | The list of resources that a security profile applies hierarchy restrictions to in Amazon Connect. Following are acceptable ResourceNames: User. |
| id                                        | core | string        | The identifier for the security profile.                                                                                                         |
| last_modified_region                      | core | string        | The Amazon Web Services Region where this resource was last modified.                                                                            |
| last_modified_time                        | core | timestamp     | The timestamp when this resource was last modified.                                                                                              |
| organization_resource_id                  | core | string        | The organization resource identifier for the security profile.                                                                                   |
| security_profile_name                     | core | string        | The name for the security profile.                                                                                                               |
| tag_restricted_resources                  | core | array<string> | The list of resources that a security profile applies tag restrictions to in Amazon Connect.                                                     |
| tags                                      | core | hstore_csv    |
