# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_algorithm.dataset.md

---
title: SageMaker Algorithm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Algorithm
---

# SageMaker Algorithm

SageMaker Algorithm in AWS represents a reusable machine learning algorithm that can be used to train models or perform inference within Amazon SageMaker. It provides details about the algorithm, such as its name, description, training and inference specifications, and supported input and output formats. This resource allows you to manage and reuse algorithms across multiple training jobs and endpoints, simplifying the process of building and deploying machine learning solutions.

```
aws.sagemaker_algorithm
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                             | Description |
| ------------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| algorithm_arn            | core | string     | The Amazon Resource Name (ARN) of the algorithm.                                                      |
| algorithm_description    | core | string     | A brief summary about the algorithm.                                                                  |
| algorithm_name           | core | string     | The name of the algorithm being described.                                                            |
| algorithm_status         | core | string     | The current status of the algorithm.                                                                  |
| algorithm_status_details | core | json       | Details about the current status of the algorithm.                                                    |
| certify_for_marketplace  | core | bool       | Whether the algorithm is certified to be listed in Amazon Web Services Marketplace.                   |
| creation_time            | core | timestamp  | A timestamp specifying when the algorithm was created.                                                |
| inference_specification  | core | json       | Details about inference jobs that the algorithm runs.                                                 |
| product_id               | core | string     | The product identifier of the algorithm.                                                              |
| tags                     | core | hstore_csv |
| training_specification   | core | json       | Details about training jobs run by this algorithm.                                                    |
| validation_specification | core | json       | Details about configurations for one or more training jobs that SageMaker runs to test the algorithm. |
