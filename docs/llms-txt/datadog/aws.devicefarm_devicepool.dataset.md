# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_devicepool.dataset.md

---
title: Devicefarm Devicepool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Devicefarm Devicepool
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.devicefarm_devicepool.dataset/index.html
---

# Devicefarm Devicepool

This table represents the devicefarm_devicepool resource from Amazon Web Services.

```
aws.devicefarm_devicepool
```

## Fields

| Title       | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ----------- | ---- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key        | core | string |
| account_id  | core | string |
| arn         | core | string | The device pool's ARN.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| description | core | string | The device pool's description.                                                                                                                                                                                                                                                                                                                                                                                                            |
| max_devices | core | int64  | The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the <code>rules</code> parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter. By specifying the maximum number of devices, you can control the costs that you incur by running tests. |
| name        | core | string | The device pool's name.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| rules       | core | json   | Information about the device pool's rules.                                                                                                                                                                                                                                                                                                                                                                                                |
| tags        | core | hstore |
| type        | core | string | The device pool's type. Allowed values include: <ul> <li> CURATED: A device pool that is created and managed by AWS Device Farm. </li> <li> PRIVATE: A device pool that is created and managed by the device pool developer. </li> </ul>                                                                                                                                                                                                  |
