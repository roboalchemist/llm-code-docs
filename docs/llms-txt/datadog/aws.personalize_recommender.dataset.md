# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_recommender.dataset.md

---
title: Personalize Recommender
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Recommender
---

# Personalize Recommender

Personalize Recommender in AWS is a managed resource that provides personalized item recommendations based on user behavior and item data. It uses machine learning models trained in Amazon Personalize to deliver real-time, tailored suggestions without requiring ML expertise. This service helps improve user engagement and conversions by offering relevant recommendations for applications such as e-commerce, media, and content platforms.

```
aws.personalize_recommender
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                       | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| creation_date_time        | core | timestamp  | The date and time (in Unix format) that the recommender was created.                                                                                                                                                                                                            |
| dataset_group_arn         | core | string     | The Amazon Resource Name (ARN) of the Domain dataset group that contains the recommender.                                                                                                                                                                                       |
| failure_reason            | core | string     | If a recommender fails, the reason behind the failure.                                                                                                                                                                                                                          |
| last_updated_date_time    | core | timestamp  | The date and time (in Unix format) that the recommender was last updated.                                                                                                                                                                                                       |
| latest_recommender_update | core | json       | Provides a summary of the latest updates to the recommender.                                                                                                                                                                                                                    |
| model_metrics             | core | string     | Provides evaluation metrics that help you determine the performance of a recommender. For more information, see Evaluating a recommender.                                                                                                                                       |
| name                      | core | string     | The name of the recommender.                                                                                                                                                                                                                                                    |
| recipe_arn                | core | string     | The Amazon Resource Name (ARN) of the recipe (Domain dataset group use case) that the recommender was created for.                                                                                                                                                              |
| recommender_arn           | core | string     | The Amazon Resource Name (ARN) of the recommender.                                                                                                                                                                                                                              |
| recommender_config        | core | json       | The configuration details of the recommender.                                                                                                                                                                                                                                   |
| status                    | core | string     | The status of the recommender. A recommender can be in one of the following states: CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED STOP PENDING > STOP IN_PROGRESS > INACTIVE > START PENDING > START IN_PROGRESS > ACTIVE DELETE PENDING > DELETE IN_PROGRESS |
| tags                      | core | hstore_csv |
