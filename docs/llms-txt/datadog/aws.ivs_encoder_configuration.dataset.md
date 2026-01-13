# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_encoder_configuration.dataset.md

---
title: Ivs Encoder Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ivs Encoder Configuration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ivs_encoder_configuration.dataset/index.html
---

# Ivs Encoder Configuration

This table represents the ivs_encoder_configuration resource from Amazon Web Services.

```
aws.ivs_encoder_configuration
```

## Fields

| Title      | ID   | Type   | Data Type                                                                          | Description |
| ---------- | ---- | ------ | ---------------------------------------------------------------------------------- | ----------- |
| _key       | core | string |
| account_id | core | string |
| arn        | core | string | ARN of the EncoderConfiguration resource.                                          |
| name       | core | string | Optional name to identify the resource.                                            |
| tags       | core | hstore |
| video      | core | json   | Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps |
