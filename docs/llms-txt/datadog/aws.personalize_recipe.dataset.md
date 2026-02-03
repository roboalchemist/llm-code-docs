# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_recipe.dataset.md

---
title: Personalize Recipe
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Recipe
---

# Personalize Recipe

An AWS Personalize Recipe is a predefined algorithm that guides how data is processed to generate personalized recommendations. Recipes define the underlying machine learning model and training approach, such as user personalization, ranking, or related items. When creating a solution in Amazon Personalize, you select a recipe that best matches your use case, and the service handles the training and deployment of the model.

```
aws.personalize_recipe
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                        | Description |
| -------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------ | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| algorithm_arn              | core | string     | The Amazon Resource Name (ARN) of the algorithm that Amazon Personalize uses to train the model. |
| creation_date_time         | core | timestamp  | The date and time (in Unix format) that the recipe was created.                                  |
| description                | core | string     | The description of the recipe.                                                                   |
| feature_transformation_arn | core | string     | The ARN of the FeatureTransformation object.                                                     |
| last_updated_date_time     | core | timestamp  | The date and time (in Unix format) that the recipe was last updated.                             |
| name                       | core | string     | The name of the recipe.                                                                          |
| recipe_arn                 | core | string     | The Amazon Resource Name (ARN) of the recipe.                                                    |
| recipe_type                | core | string     | One of the following values: PERSONALIZED_RANKING RELATED_ITEMS USER_PERSONALIZATION             |
| status                     | core | string     | The status of the recipe.                                                                        |
| tags                       | core | hstore_csv |
