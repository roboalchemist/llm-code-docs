# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_human_task_ui.dataset.md

---
title: SageMaker HumanTaskUi
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker HumanTaskUi
---

# SageMaker HumanTaskUi

SageMaker HumanTaskUi is an Amazon SageMaker resource that defines the user interface workers interact with when performing human-in-the-loop tasks. It provides the layout and instructions shown to human annotators or reviewers, enabling consistent and guided input for tasks such as data labeling, content moderation, or custom workflows.

```
aws.sagemaker_human_task_ui
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                          | Description |
| -------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| creation_time        | core | timestamp  | The timestamp when the human task user interface was created.                                      |
| human_task_ui_arn    | core | string     | The Amazon Resource Name (ARN) of the human task user interface (worker task template).            |
| human_task_ui_name   | core | string     | The name of the human task user interface (worker task template).                                  |
| human_task_ui_status | core | string     | The status of the human task user interface (worker task template). Valid values are listed below. |
| tags                 | core | hstore_csv |
| ui_template          | core | json       | Container for user interface template information.                                                 |
