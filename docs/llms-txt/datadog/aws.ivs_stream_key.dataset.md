# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_stream_key.dataset.md

---
title: IVS Stream Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IVS Stream Key
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ivs_stream_key.dataset/index.html
---

# IVS Stream Key

An IVS Stream Key in AWS is a unique credential used to authenticate and authorize live video streams into an Amazon Interactive Video Service (IVS) channel. It links a broadcaster to a specific channel, ensuring that only authorized streams are ingested. Stream keys are managed per channel and can be created, listed, or revoked as needed for secure and controlled streaming.

```
aws.ivs_stream_key
```

## Fields

| Title       | ID   | Type   | Data Type                   | Description |
| ----------- | ---- | ------ | --------------------------- | ----------- |
| _key        | core | string |
| account_id  | core | string |
| arn         | core | string | Stream-key ARN.             |
| channel_arn | core | string | Channel ARN for the stream. |
| tags        | core | hstore |
