# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_authentication_profile.dataset.md

---
title: Connect Authentication Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Authentication Profile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.connect_authentication_profile.dataset/index.html
---

# Connect Authentication Profile

Connect Authentication Profile in AWS defines the authentication settings used within Amazon Connect. It allows you to configure and manage how users are authenticated when accessing your contact center, supporting integration with identity providers and ensuring secure access. This resource helps maintain consistent security policies and simplifies user management across your Connect environment.

```
aws.connect_authentication_profile
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                                               | Description |
| ------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| account_id                | core | string        |
| allowed_ips               | core | array<string> | A list of IP address range strings that are allowed to access the Amazon Connect instance. For more information about how to configure IP addresses, see Configure IP address based access control in the Amazon Connect Administrator Guide.                                           |
| arn                       | core | string        | The Amazon Resource Name (ARN) for the authentication profile.                                                                                                                                                                                                                          |
| blocked_ips               | core | array<string> | A list of IP address range strings that are blocked from accessing the Amazon Connect instance. For more information about how to configure IP addresses, see Configure IP address based access control in the Amazon Connect Administrator Guide.                                      |
| created_time              | core | timestamp     | The timestamp when the authentication profile was created.                                                                                                                                                                                                                              |
| description               | core | string        | The description for the authentication profile.                                                                                                                                                                                                                                         |
| id                        | core | string        | A unique identifier for the authentication profile.                                                                                                                                                                                                                                     |
| is_default                | core | bool          | Shows whether the authentication profile is the default authentication profile for the Amazon Connect instance. The default authentication profile applies to all agents in an Amazon Connect instance, unless overridden by another authentication profile.                            |
| last_modified_region      | core | string        | The Amazon Web Services Region where the authentication profile was last modified.                                                                                                                                                                                                      |
| last_modified_time        | core | timestamp     | The timestamp when the authentication profile was last modified.                                                                                                                                                                                                                        |
| max_session_duration      | core | int64         | The long lived session duration for users logged in to Amazon Connect, in minutes. After this time period, users must log in again. For more information, see Configure the session duration in the Amazon Connect Administrator Guide.                                                 |
| name                      | core | string        | The name for the authentication profile.                                                                                                                                                                                                                                                |
| periodic_session_duration | core | int64         | The short lived session duration configuration for users logged in to Amazon Connect, in minutes. This value determines the maximum possible time before an agent is authenticated. For more information, see Configure the session duration in the Amazon Connect Administrator Guide. |
| tags                      | core | hstore        |
