# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_flow_definition.dataset.md

---
title: SageMaker Flow Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Flow Definition
---

# SageMaker Flow Definition

SageMaker Flow Definition in AWS defines the configuration for human-in-the-loop workflows. It specifies how human review tasks are set up, including the workforce, UI template, and output storage. This resource is used with SageMaker Ground Truth and Augmented AI to manage data labeling or model review processes, ensuring human input is integrated into machine learning workflows.

```
aws.sagemaker_flow_definition
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                               | Description |
| ---------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| creation_time                | core | timestamp  | The timestamp when the flow definition was created.                                                                                                     |
| failure_reason               | core | string     | The reason your flow definition failed.                                                                                                                 |
| flow_definition_arn          | core | string     | The Amazon Resource Name (ARN) of the flow defintion.                                                                                                   |
| flow_definition_name         | core | string     | The Amazon Resource Name (ARN) of the flow definition.                                                                                                  |
| flow_definition_status       | core | string     | The status of the flow definition. Valid values are listed below.                                                                                       |
| human_loop_activation_config | core | json       | An object containing information about what triggers a human review workflow.                                                                           |
| human_loop_config            | core | json       | An object containing information about who works on the task, the workforce task price, and other task details.                                         |
| human_loop_request_source    | core | json       | Container for configuring the source of human task requests. Used to specify if Amazon Rekognition or Amazon Textract is used as an integration source. |
| output_config                | core | json       | An object containing information about the output file.                                                                                                 |
| role_arn                     | core | string     | The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) execution role for the flow definition.                  |
| tags                         | core | hstore_csv |
