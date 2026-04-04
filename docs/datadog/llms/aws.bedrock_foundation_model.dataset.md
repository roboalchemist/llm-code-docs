# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_foundation_model.dataset.md

---
title: Bedrock Foundation Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Foundation Model
---

# Bedrock Foundation Model

Bedrock Foundation Model in AWS provides access to large-scale machine learning models through Amazon Bedrock. It allows developers to use pre-trained foundation models for tasks like text generation, summarization, classification, and more without managing infrastructure or training models from scratch.

```
aws.bedrock_foundation_model
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                 | Description |
| ---------------------------- | ---- | ------------- | ------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| customizations_supported     | core | array<string> | The customization that the model supports.                                |
| inference_types_supported    | core | array<string> | The inference types that the model supports.                              |
| input_modalities             | core | array<string> | The input modalities that the model supports.                             |
| model_arn                    | core | string        | The model Amazon Resource Name (ARN).                                     |
| model_id                     | core | string        | The model identifier.                                                     |
| model_lifecycle              | core | json          | Contains details about whether a model version is available or deprecated |
| model_name                   | core | string        | The model name.                                                           |
| output_modalities            | core | array<string> | The output modalities that the model supports.                            |
| provider_name                | core | string        | The model's provider name.                                                |
| response_streaming_supported | core | bool          | Indicates whether the model supports streaming.                           |
