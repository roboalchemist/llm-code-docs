# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_launch_template.dataset.md

---
title: EC2 Launch Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Launch Template
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_launch_template.dataset/index.html
---

# EC2 Launch Template

An EC2 Launch Template in AWS is a resource that defines configuration details for launching EC2 instances. It allows you to specify settings such as instance type, AMI, key pairs, security groups, networking, and storage. Launch Templates simplify instance provisioning by enabling versioning, reusability, and consistency across deployments.

```
aws.ec2_launch_template
```

## Fields

| Title                  | ID   | Type      | Data Type                                                         | Description |
| ---------------------- | ---- | --------- | ----------------------------------------------------------------- | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| create_time            | core | timestamp | The time launch template was created.                             |
| created_by             | core | string    | The principal that created the launch template.                   |
| default_version_number | core | int64     | The version number of the default version of the launch template. |
| latest_version_number  | core | int64     | The version number of the latest version of the launch template.  |
| launch_template_arn    | core | string    |
| launch_template_id     | core | string    | The ID of the launch template.                                    |
| launch_template_name   | core | string    | The name of the launch template.                                  |
| operator               | core | json      | The entity that manages the launch template.                      |
| tags                   | core | hstore    |
