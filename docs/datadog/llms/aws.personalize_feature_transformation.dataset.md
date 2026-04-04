# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_feature_transformation.dataset.md

---
title: Personalize Feature Transformation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Feature Transformation
---

# Personalize Feature Transformation

Personalize Feature Transformation in AWS is part of Amazon Personalize, which prepares and processes input data for machine learning models. It applies transformations such as normalization, encoding, and handling of categorical or numerical features to ensure the data is in the right format for training recommendation models. This step improves the quality and accuracy of personalized recommendations.

```
aws.personalize_feature_transformation
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                                                 | Description |
| -------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| creation_date_time         | core | timestamp  | The creation date and time (in Unix time) of the feature transformation.                                                                                                  |
| default_parameters         | core | hstore     | Provides the default parameters for feature transformation.                                                                                                               |
| feature_transformation_arn | core | string     | The Amazon Resource Name (ARN) of the FeatureTransformation object.                                                                                                       |
| last_updated_date_time     | core | timestamp  | The last update date and time (in Unix time) of the feature transformation.                                                                                               |
| name                       | core | string     | The name of the feature transformation.                                                                                                                                   |
| status                     | core | string     | The status of the feature transformation. A feature transformation can be in one of the following states: CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED |
| tags                       | core | hstore_csv |
