# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transcribe_language_model.dataset.md

---
title: Transcribe Language Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transcribe Language Model
---

# Transcribe Language Model

A Transcribe Language Model in AWS is a custom language model resource used with Amazon Transcribe. It allows you to train and deploy domain-specific models that improve speech-to-text accuracy for specialized vocabularies, such as industry terms, product names, or jargon. This helps generate more accurate transcripts tailored to your use case.

```
aws.transcribe_language_model
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| -------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| base_model_name      | core | string     | The Amazon Transcribe standard language model, or base model, used to create your custom language model.                                                                                                                                                                                                                                                                                                                                                         |
| create_time          | core | timestamp  | The date and time the specified custom language model was created. Timestamps are in the format YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC. For example, 2022-05-04T12:32:58.761000-07:00 represents 12:32 PM UTC-7 on May 4, 2022.                                                                                                                                                                                                                                        |
| failure_reason       | core | string     | If ModelStatus is FAILED, FailureReason contains information about why the custom language model request failed. See also: Common Errors.                                                                                                                                                                                                                                                                                                                        |
| input_data_config    | core | json       | The Amazon S3 location of the input files used to train and tune your custom language model, in addition to the data access role ARN (Amazon Resource Name) that has permissions to access these data.                                                                                                                                                                                                                                                           |
| language_code        | core | string     | The language code used to create your custom language model. Each custom language model must contain terms in only one language, and the language you select for your custom language model must match the language of your training and tuning data. For a list of supported languages and their associated language codes, refer to the Supported languages table. Note that US English (en-US) is the only language supported with Amazon Transcribe Medical. |
| last_modified_time   | core | timestamp  | The date and time the specified custom language model was last modified. Timestamps are in the format YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC. For example, 2022-05-04T12:32:58.761000-07:00 represents 12:32 PM UTC-7 on May 4, 2022.                                                                                                                                                                                                                                  |
| model_name           | core | string     | A unique name, chosen by you, for your custom language model. This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account.                                                                                                                                                                                                                                                                                      |
| model_status         | core | string     | The status of the specified custom language model. When the status displays as COMPLETED the model is ready for use.                                                                                                                                                                                                                                                                                                                                             |
| tags                 | core | hstore_csv |
| upgrade_availability | core | bool       | Shows if a more current base model is available for use with the specified custom language model. If false, your custom language model is using the most up-to-date base model. If true, there is a newer base model available than the one your language model is using. Note that to update a base model, you must recreate the custom language model using the new base model. Base model upgrades for existing custom language models are not supported.     |
