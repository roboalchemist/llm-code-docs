# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotanalytics_channel.dataset.md

---
title: Iotanalytics Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iotanalytics Channel
---

# Iotanalytics Channel

This table represents the iotanalytics_channel resource from Amazon Web Services.

```
aws.iotanalytics_channel
```

## Fields

| Title      | ID   | Type       | Data Type                                                                                                                          | Description |
| ---------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| channel    | core | json       | An object that contains information about the channel.                                                                             |
| statistics | core | json       | Statistics about the channel. Included if the <code>includeStatistics</code> parameter is set to <code>true</code> in the request. |
| tags       | core | hstore_csv |
