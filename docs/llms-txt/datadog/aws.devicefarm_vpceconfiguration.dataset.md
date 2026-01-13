# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_vpceconfiguration.dataset.md

---
title: Devicefarm Vpceconfiguration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Devicefarm Vpceconfiguration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.devicefarm_vpceconfiguration.dataset/index.html
---

# Devicefarm Vpceconfiguration

This table represents the devicefarm_vpceconfiguration resource from Amazon Web Services.

```
aws.devicefarm_vpceconfiguration
```

## Fields

| Title                          | ID   | Type   | Data Type                                                                                                | Description |
| ------------------------------ | ---- | ------ | -------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string |
| account_id                     | core | string |
| arn                            | core | string | The Amazon Resource Name (ARN) of the VPC endpoint configuration.                                        |
| service_dns_name               | core | string | The DNS name that maps to the private IP address of the service you want to access.                      |
| tags                           | core | hstore |
| vpce_configuration_description | core | string | An optional description that provides details about your VPC endpoint configuration.                     |
| vpce_configuration_name        | core | string | The friendly name you give to your VPC endpoint configuration to manage your configurations more easily. |
| vpce_service_name              | core | string | The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.      |
