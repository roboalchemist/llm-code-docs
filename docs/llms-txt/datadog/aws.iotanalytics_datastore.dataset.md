# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotanalytics_datastore.dataset.md

---
title: Iotanalytics Datastore
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iotanalytics Datastore
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotanalytics_datastore.dataset/index.html
---

# Iotanalytics Datastore

This table represents the iotanalytics_datastore resource from Amazon Web Services.

```
aws.iotanalytics_datastore
```

## Fields

| Title      | ID   | Type   | Data Type                                                                                                                                                     | Description |
| ---------- | ---- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string |
| account_id | core | string |
| datastore  | core | json   | Information about the data store.                                                                                                                             |
| statistics | core | json   | Additional statistical information about the data store. Included if the <code>includeStatistics</code> parameter is set to <code>true</code> in the request. |
| tags       | core | hstore |
