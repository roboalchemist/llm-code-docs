# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_public_fpga_image.dataset.md

---
title: EC2 Public FPGA Image
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Public FPGA Image
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_public_fpga_image.dataset/index.html
---

# EC2 Public FPGA Image

An EC2 Public FPGA Image (AFI) is a pre-built, reusable image that contains a hardware design for use with AWS F1 instances. It allows developers to share and deploy custom FPGA logic without needing to rebuild or recompile the design. Public FPGA Images are published by AWS or third parties and can be used directly to accelerate workloads such as genomics, financial analytics, or real-time data processing.

```
aws.ec2_public_fpga_image
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                              | Description |
| ---------------------- | ---- | ------------- | -------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| create_time            | core | timestamp     | The date and time the AFI was created.                                                 |
| data_retention_support | core | bool          | Indicates whether data retention support is enabled for the AFI.                       |
| description            | core | string        | The description of the AFI.                                                            |
| fpga_image_global_id   | core | string        | The global FPGA image identifier (AGFI ID).                                            |
| fpga_image_id          | core | string        | The FPGA image identifier (AFI ID).                                                    |
| instance_types         | core | array<string> | The instance types supported by the AFI.                                               |
| name                   | core | string        | The name of the AFI.                                                                   |
| owner_alias            | core | string        | The alias of the AFI owner. Possible values include self, amazon, and aws-marketplace. |
| owner_id               | core | string        | The ID of the Amazon Web Services account that owns the AFI.                           |
| pci_id                 | core | json          | Information about the PCI bus.                                                         |
| product_codes          | core | json          | The product codes for the AFI.                                                         |
| public                 | core | bool          | Indicates whether the AFI is public.                                                   |
| shell_version          | core | string        | The version of the Amazon Web Services Shell that was used to create the bitstream.    |
| state                  | core | json          | Information about the state of the AFI.                                                |
| tags                   | core | hstore        |
| update_time            | core | timestamp     | The time of the most recent update to the AFI.                                         |
