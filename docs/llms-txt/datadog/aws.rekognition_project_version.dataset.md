# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rekognition_project_version.dataset.md

---
title: Rekognition Project Version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Rekognition Project Version
---

# Rekognition Project Version

Rekognition Project Version represents a trained model version within Amazon Rekognition Custom Labels. It contains details about the model such as its status, training and evaluation metrics, creation time, and associated project. Each project version is a snapshot of a trained model that can be deployed for image or video analysis tasks like object detection or classification.

```
aws.rekognition_project_version
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                                      | Description |
| --------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| base_model_version                | core | string     | The base detection model version used to create the project version.                                                                                                           |
| billable_training_time_in_seconds | core | int64      | The duration, in seconds, that you were billed for a successful training of the model version. This value is only returned if the model version has been successfully trained. |
| creation_timestamp                | core | timestamp  | The Unix datetime for the date and time that training started.                                                                                                                 |
| evaluation_result                 | core | json       | The training results. EvaluationResult is only returned if training is successful.                                                                                             |
| feature                           | core | string     | The feature that was customized.                                                                                                                                               |
| feature_config                    | core | json       | Feature specific configuration that was applied during training.                                                                                                               |
| kms_key_id                        | core | string     | The identifer for the AWS Key Management Service key (AWS KMS key) that was used to encrypt the model during training.                                                         |
| manifest_summary                  | core | json       | The location of the summary manifest. The summary manifest provides aggregate data validation results for the training and test datasets.                                      |
| max_inference_units               | core | int64      | The maximum number of inference units Amazon Rekognition uses to auto-scale the model. Applies only to Custom Labels projects. For more information, see StartProjectVersion.  |
| min_inference_units               | core | int64      | The minimum number of inference units used by the model. Applies only to Custom Labels projects. For more information, see StartProjectVersion.                                |
| output_config                     | core | json       | The location where training results are saved.                                                                                                                                 |
| project_version_arn               | core | string     | The Amazon Resource Name (ARN) of the project version.                                                                                                                         |
| source_project_version_arn        | core | string     | If the model version was copied from a different project, SourceProjectVersionArn contains the ARN of the source model version.                                                |
| status                            | core | string     | The current status of the model version.                                                                                                                                       |
| status_message                    | core | string     | A descriptive message for an error or warning that occurred.                                                                                                                   |
| tags                              | core | hstore_csv |
| testing_data_result               | core | json       | Contains information about the testing results.                                                                                                                                |
| training_data_result              | core | json       | Contains information about the training results.                                                                                                                               |
| training_end_timestamp            | core | timestamp  | The Unix date and time that training of the model ended.                                                                                                                       |
| version_description               | core | string     | A user-provided description of the project version.                                                                                                                            |
