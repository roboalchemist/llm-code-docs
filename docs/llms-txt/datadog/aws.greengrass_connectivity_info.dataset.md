# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_connectivity_info.dataset.md

---
title: Greengrass Connectivity Info
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Greengrass Connectivity Info
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.greengrass_connectivity_info.dataset/index.html
---

# Greengrass Connectivity Info

This table represents the greengrass_connectivity_info resource from Amazon Web Services.

```
aws.greengrass_connectivity_info
```

## Fields

| Title             | ID   | Type   | Data Type                                             | Description |
| ----------------- | ---- | ------ | ----------------------------------------------------- | ----------- |
| _key              | core | string |
| account_id        | core | string |
| connectivity_info | core | json   | The connectivity information for the core device.     |
| message           | core | string | A message about the connectivity information request. |
| tags              | core | hstore |
