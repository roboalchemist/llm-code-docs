# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_playback_key_pair.dataset.md

---
title: IVS Playback Key Pair
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IVS Playback Key Pair
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ivs_playback_key_pair.dataset/index.html
---

# IVS Playback Key Pair

An IVS Playback Key Pair in AWS is a resource used with Amazon Interactive Video Service to enable secure playback authorization. It consists of a public-private key pair where the public key is registered with IVS, and the private key is used by your application to generate signed playback authorization tokens. This ensures that only authorized viewers can access your video streams.

```
aws.ivs_playback_key_pair
```

## Fields

| Title      | ID   | Type   | Data Type                                                     | Description |
| ---------- | ---- | ------ | ------------------------------------------------------------- | ----------- |
| _key       | core | string |
| account_id | core | string |
| arn        | core | string | Key-pair ARN.                                                 |
| name       | core | string | Playback-key-pair name. The value does not need to be unique. |
| tags       | core | hstore |
