# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_launch_template_version.dataset.md

---
title: EC2 Launch Template Version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Launch Template Version
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_launch_template_version.dataset/index.html
---

# EC2 Launch Template Version

An EC2 Launch Template Version in AWS defines a specific configuration of an EC2 launch template, including details like instance type, AMI, key pairs, security groups, and network settings. Each version is immutable, allowing you to maintain multiple versions of a template for different use cases or environments. This makes it easier to manage, update, and roll back EC2 instance configurations consistently and reliably.

```
aws.ec2_launch_template_version
```

## Fields

| Title                       | ID   | Type      | Data Type                                             | Description |
| --------------------------- | ---- | --------- | ----------------------------------------------------- | ----------- |
| _key                        | core | string    |
| account_id                  | core | string    |
| create_time                 | core | timestamp | The time the version was created.                     |
| created_by                  | core | string    | The principal that created the version.               |
| default_version             | core | bool      | Indicates whether the version is the default version. |
| launch_template_data        | core | json      | Information about the launch template.                |
| launch_template_id          | core | string    | The ID of the launch template.                        |
| launch_template_name        | core | string    | The name of the launch template.                      |
| launch_template_version_arn | core | string    |
| operator                    | core | json      | The entity that manages the launch template.          |
| tags                        | core | hstore    |
| version_description         | core | string    | The description for the version.                      |
| version_number              | core | int64     | The version number.                                   |
