# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_dimension.dataset.md

---
title: IoT Dimension
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Dimension
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iot_dimension.dataset/index.html
---

# IoT Dimension

An AWS IoT Dimension is a reusable filter that defines a specific set of criteria to limit the scope of IoT data, such as restricting metrics or logs to certain devices or device groups. It helps simplify the management of IoT rules and security policies by allowing you to apply consistent filtering logic across multiple resources.

```
aws.iot_dimension
```

## Fields

| Title              | ID   | Type          | Data Type                                                                                                                                       | Description |
| ------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| arn                | core | string        | The Amazon Resource Name (ARN) for the dimension.                                                                                               |
| creation_date      | core | timestamp     | The date the dimension was created.                                                                                                             |
| last_modified_date | core | timestamp     | The date the dimension was last modified.                                                                                                       |
| name               | core | string        | The unique identifier for the dimension.                                                                                                        |
| string_values      | core | array<string> | The value or list of values used to scope the dimension. For example, for topic filters, this is the pattern used to match the MQTT topic name. |
| tags               | core | hstore        |
| type               | core | string        | The type of the dimension.                                                                                                                      |
