# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rekognition_project.dataset.md

---
title: Rekognition Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Rekognition Project
---

# Rekognition Project

An Amazon Rekognition Project represents a container for managing computer vision models within Rekognition Custom Labels. It stores information about the project, including its name, creation time, and status, and serves as the foundation for creating and managing datasets, training models, and deploying them for image and video analysis.

```
aws.rekognition_project
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                           | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| auto_update        | core | string     | Indicates whether automatic retraining will be attempted for the versions of the project. Applies only to adapters. |
| creation_timestamp | core | timestamp  | The Unix timestamp for the date and time that the project was created.                                              |
| datasets           | core | json       | Information about the training and test datasets in the project.                                                    |
| feature            | core | string     | Specifies the project that is being customized.                                                                     |
| project_arn        | core | string     | The Amazon Resource Name (ARN) of the project.                                                                      |
| status             | core | string     | The current status of the project.                                                                                  |
| tags               | core | hstore_csv |
