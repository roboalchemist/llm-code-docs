# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_ipam_scope.dataset.md

---
title: IPAM Scope
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IPAM Scope
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_ipam_scope.dataset/index.html
---

# IPAM Scope

An IPAM Scope in AWS is a logical container within Amazon VPC IP Address Manager (IPAM) that organizes and manages IP address space. Scopes allow you to separate IP address allocations for different purposes, such as separating private and public IP addresses. Each IPAM has default public and private scopes, and you can create additional scopes to match your network design.

```
aws.ec2_ipam_scope
```

## Fields

| Title           | ID   | Type   | Data Type                                                     | Description |
| --------------- | ---- | ------ | ------------------------------------------------------------- | ----------- |
| _key            | core | string |
| account_id      | core | string |
| description     | core | string | The description of the scope.                                 |
| ipam_arn        | core | string | The ARN of the IPAM.                                          |
| ipam_region     | core | string | The Amazon Web Services Region of the IPAM scope.             |
| ipam_scope_arn  | core | string | The Amazon Resource Name (ARN) of the scope.                  |
| ipam_scope_id   | core | string | The ID of the scope.                                          |
| ipam_scope_type | core | string | The type of the scope.                                        |
| is_default      | core | bool   | Defines if the scope is the default scope or not.             |
| owner_id        | core | string | The Amazon Web Services account ID of the owner of the scope. |
| pool_count      | core | int64  | The number of pools in the scope.                             |
| state           | core | string | The state of the IPAM scope.                                  |
| tags            | core | hstore |
