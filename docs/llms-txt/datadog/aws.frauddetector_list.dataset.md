# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_list.dataset.md

---
title: Fraud Detector List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector List
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.frauddetector_list.dataset/index.html
---

# Fraud Detector List

This table represents the Fraud Detector List resource from Amazon Web Services.

```
aws.frauddetector_list
```

## Fields

| Title         | ID   | Type   | Data Type                           | Description |
| ------------- | ---- | ------ | ----------------------------------- | ----------- |
| _key          | core | string |
| account_id    | core | string |
| arn           | core | string | The ARN of the list.                |
| created_time  | core | string | The time the list was created.      |
| description   | core | string | The description of the list.        |
| name          | core | string | The name of the list.               |
| tags          | core | hstore |
| updated_time  | core | string | The time the list was last updated. |
| variable_type | core | string | The variable type of the list.      |
