# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_deviceinstance.dataset.md

---
title: Devicefarm Deviceinstance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Devicefarm Deviceinstance
---

# Devicefarm Deviceinstance

This table represents the devicefarm_deviceinstance resource from Amazon Web Services.

```
aws.devicefarm_deviceinstance
```

## Fields

| Title            | ID   | Type          | Data Type                                                        | Description |
| ---------------- | ---- | ------------- | ---------------------------------------------------------------- | ----------- |
| _key             | core | string        |
| account_id       | core | string        |
| arn              | core | string        | The Amazon Resource Name (ARN) of the device instance.           |
| device_arn       | core | string        | The ARN of the device.                                           |
| instance_profile | core | json          | A object that contains information about the instance profile.   |
| labels           | core | array<string> | An array of strings that describe the device instance.           |
| status           | core | string        | The status of the device instance. Valid values are listed here. |
| tags             | core | hstore_csv    |
| udid             | core | string        | Unique device identifier for the device instance.                |
