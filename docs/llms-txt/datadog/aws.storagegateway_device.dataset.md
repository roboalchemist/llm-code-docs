# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.storagegateway_device.dataset.md

---
title: Storage Gateway Device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Gateway Device
---

# Storage Gateway Device

This table represents the Storage Gateway Device resource from Amazon Web Services.

```
aws.storagegateway_device
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                    | Description |
| ----------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| devicei_scsi_attributes       | core | json       | A list of iSCSI information about a VTL device.                                              |
| tags                          | core | hstore_csv |
| vtl_device_arn                | core | string     | Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media changer). |
| vtl_device_product_identifier | core | string     | Specifies the model number of device that the VTL device emulates.                           |
| vtl_device_type               | core | string     | Specifies the type of device that the VTL device emulates.                                   |
| vtl_device_vendor             | core | string     | Specifies the vendor of the device that the VTL device object emulates.                      |
