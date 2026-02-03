# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_web_network_settings.dataset.md

---
title: Workspaces Web Network Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Workspaces Web Network Settings
---

# Workspaces Web Network Settings

This table represents the workspaces_web_network_settings resource from Amazon Web Services.

```
aws.workspaces_web_network_settings
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                              | Description |
| ---------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| associated_portal_arns | core | array<string> | A list of web portal ARNs that this network settings is associated with.                                                                                               |
| network_settings_arn   | core | string        | The ARN of the network settings.                                                                                                                                       |
| security_group_ids     | core | array<string> | One or more security groups used to control access from streaming instances to your VPC.                                                                               |
| subnet_ids             | core | array<string> | The subnets in which network interfaces are created to connect streaming instances to your VPC. At least two of these subnets must be in different availability zones. |
| tags                   | core | hstore_csv    |
| vpc_id                 | core | string        | The VPC that streaming instances will connect to.                                                                                                                      |
