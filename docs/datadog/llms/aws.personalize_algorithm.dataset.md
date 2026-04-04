# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_algorithm.dataset.md

---
title: Personalize Algorithm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Algorithm
---

# Personalize Algorithm

Personalize Algorithm in AWS refers to a custom or predefined machine learning algorithm used within Amazon Personalize to generate personalized recommendations. It defines the logic and training approach behind recommendation models, such as collaborative filtering or deep learning methods. The resource provides details about the algorithm, including its name, ARN, supported features, and training requirements, helping users understand how it can be applied to build tailored recommendation systems.

```
aws.personalize_algorithm
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                                                                                           | Description |
| ------------------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| algorithm_arn                  | core | string     | The Amazon Resource Name (ARN) of the algorithm.                                                                                                                                    |
| algorithm_image                | core | json       | The URI of the Docker container for the algorithm image.                                                                                                                            |
| creation_date_time             | core | timestamp  | The date and time (in Unix time) that the algorithm was created.                                                                                                                    |
| default_hyper_parameter_ranges | core | json       | Specifies the default hyperparameters, their ranges, and whether they are tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO). |
| default_hyper_parameters       | core | hstore     | Specifies the default hyperparameters.                                                                                                                                              |
| default_resource_config        | core | hstore     | Specifies the default maximum number of training jobs and parallel training jobs.                                                                                                   |
| last_updated_date_time         | core | timestamp  | The date and time (in Unix time) that the algorithm was last updated.                                                                                                               |
| name                           | core | string     | The name of the algorithm.                                                                                                                                                          |
| role_arn                       | core | string     | The Amazon Resource Name (ARN) of the role.                                                                                                                                         |
| tags                           | core | hstore_csv |
| training_input_mode            | core | string     | The training input mode.                                                                                                                                                            |
