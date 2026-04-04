# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lookoutequipment_label_group.dataset.md

---
title: Lookout for Equipment Label Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lookout for Equipment Label Group
---

# Lookout for Equipment Label Group

Lookout for Equipment Label Group in AWS is a resource that organizes and manages labels used for training machine learning models in Amazon Lookout for Equipment. A label group contains labels that represent specific equipment conditions or events, such as failures or anomalies, which help improve the accuracy of predictive maintenance models.

```
aws.lookoutequipment_label_group
```

## Fields

| Title            | ID   | Type          | Data Type                                                                            | Description |
| ---------------- | ---- | ------------- | ------------------------------------------------------------------------------------ | ----------- |
| _key             | core | string        |
| account_id       | core | string        |
| created_at       | core | timestamp     | The time at which the label group was created.                                       |
| fault_codes      | core | array<string> | Codes indicating the type of anomaly associated with the labels in the lagbel group. |
| label_group_arn  | core | string        | The Amazon Resource Name (ARN) of the label group.                                   |
| label_group_name | core | string        | The name of the label group.                                                         |
| tags             | core | hstore_csv    |
| updated_at       | core | timestamp     | The time at which the label group was updated.                                       |
