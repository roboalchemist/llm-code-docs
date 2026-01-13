# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_system_defined_inference_profile.dataset.md

---
title: Bedrock System-Defined Inference Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Bedrock System-Defined Inference
  Profile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_system_defined_inference_profile.dataset/index.html
---

# Bedrock System-Defined Inference Profile

The Bedrock System-Defined Inference Profile in AWS provides predefined configurations for running inference with foundation models on Amazon Bedrock. These profiles specify optimized settings such as compute resources and performance characteristics, allowing users to quickly deploy and run model inference without manually tuning infrastructure. They simplify the process of selecting the right environment for workloads, ensuring efficiency and consistency across model deployments.

```
aws.bedrock_system_defined_inference_profile
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
