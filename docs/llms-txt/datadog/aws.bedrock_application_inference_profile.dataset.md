# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_application_inference_profile.dataset.md

---
title: Bedrock Application Inference Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Bedrock Application Inference
  Profile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_application_inference_profile.dataset/index.html
---

# Bedrock Application Inference Profile

An AWS Bedrock Application Inference Profile defines the configuration and details of an inference setup for running foundation model applications. It provides information about the model, supported input and output formats, performance characteristics, and usage parameters. This profile helps developers understand how to interact with the model for inference tasks and ensures applications can integrate with Bedrock services efficiently.

```
aws.bedrock_application_inference_profile
```

## Fields

| Title                  | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ---------------------- | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| created_at             | core | timestamp | The time at which the inference profile was created.                                                                                                                                                                                                                                                                                                                                                                                               |
| description            | core | string    | The description of the inference profile.                                                                                                                                                                                                                                                                                                                                                                                                          |
| inference_profile_arn  | core | string    | The Amazon Resource Name (ARN) of the inference profile.                                                                                                                                                                                                                                                                                                                                                                                           |
| inference_profile_id   | core | string    | The unique identifier of the inference profile.                                                                                                                                                                                                                                                                                                                                                                                                    |
| inference_profile_name | core | string    | The name of the inference profile.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| models                 | core | json      | A list of information about each model in the inference profile.                                                                                                                                                                                                                                                                                                                                                                                   |
| status                 | core | string    | The status of the inference profile. ACTIVE means that the inference profile is ready to be used.                                                                                                                                                                                                                                                                                                                                                  |
| tags                   | core | hstore    |
| type                   | core | string    | The type of the inference profile. The following types are possible: SYSTEM_DEFINED â The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles. APPLICATION â The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions. |
| updated_at             | core | timestamp | The time at which the inference profile was last updated.                                                                                                                                                                                                                                                                                                                                                                                          |
