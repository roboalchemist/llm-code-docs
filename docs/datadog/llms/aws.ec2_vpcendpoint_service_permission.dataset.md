# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_vpcendpoint_service_permission.dataset.md

---
title: Ec2 Vpcendpoint Service Permission
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ec2 Vpcendpoint Service Permission
---

# Ec2 Vpcendpoint Service Permission

This table represents the ec2_vpcendpoint_service_permission resource from Amazon Web Services.

```
aws.ec2_vpcendpoint_service_permission
```

## Fields

| Title                 | ID   | Type       | Data Type                                        | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------ | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| principal             | core | string     | The Amazon Resource Name (ARN) of the principal. |
| principal_type        | core | string     | The type of principal.                           |
| service_id            | core | string     | The ID of the service.                           |
| service_permission_id | core | string     | The ID of the service permission.                |
| tags                  | core | hstore_csv |
