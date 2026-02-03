# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_verified_access_group.dataset.md

---
title: EC2 Verified Access Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Verified Access Group
---

# EC2 Verified Access Group

An EC2 Verified Access Group in AWS is a logical container that defines access policies for applications using Verified Access. It allows you to group applications and apply consistent security and access controls without requiring a VPN. This helps enforce zero-trust principles by verifying user identity and device posture before granting access.

```
aws.ec2_verified_access_group
```

## Fields

| Title                       | ID   | Type       | Data Type                                                        | Description |
| --------------------------- | ---- | ---------- | ---------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| creation_time               | core | string     | The creation time.                                               |
| deletion_time               | core | string     | The deletion time.                                               |
| description                 | core | string     | A description for the Amazon Web Services Verified Access group. |
| last_updated_time           | core | string     | The last updated time.                                           |
| owner                       | core | string     | The Amazon Web Services account number that owns the group.      |
| policy_document             | core | string     | The Verified Access policy document.                             |
| policy_enabled              | core | bool       | The status of the Verified Access policy.                        |
| sse_specification           | core | json       | The options in use for server side encryption.                   |
| tags                        | core | hstore_csv |
| verified_access_group_arn   | core | string     | The ARN of the Verified Access group.                            |
| verified_access_group_id    | core | string     | The ID of the Verified Access group.                             |
| verified_access_instance_id | core | string     | The ID of the Amazon Web Services Verified Access instance.      |
