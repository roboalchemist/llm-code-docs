# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_user.dataset.md

---
title: Connect User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect User
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.connect_user.dataset/index.html
---

# Connect User

Connect User in AWS refers to an Amazon Connect user account, which represents an individual agent or administrator within a contact center. It contains details such as user identity, security profile, hierarchy group, and routing profile. This resource is used to manage and retrieve information about users, enabling administrators to control access, assign roles, and configure permissions for handling customer interactions in Amazon Connect.

```
aws.connect_user
```

## Fields

| Title                | ID   | Type          | Data Type                                                                         | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| account_id           | core | string        |
| arn                  | core | string        | The Amazon Resource Name (ARN) of the user account.                               |
| directory_user_id    | core | string        | The identifier of the user account in the directory used for identity management. |
| hierarchy_group_id   | core | string        | The identifier of the hierarchy group for the user.                               |
| id                   | core | string        | The identifier of the user account.                                               |
| identity_info        | core | json          | Information about the user identity.                                              |
| last_modified_region | core | string        | The Amazon Web Services Region where this resource was last modified.             |
| last_modified_time   | core | timestamp     | The timestamp when this resource was last modified.                               |
| phone_config         | core | json          | Information about the phone configuration for the user.                           |
| routing_profile_id   | core | string        | The identifier of the routing profile for the user.                               |
| security_profile_ids | core | array<string> | The identifiers of the security profiles for the user.                            |
| tags                 | core | hstore        |
| username             | core | string        | The user name assigned to the user account.                                       |
