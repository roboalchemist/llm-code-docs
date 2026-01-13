# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_guardrail.dataset.md

---
title: Bedrock Guardrail
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Guardrail
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_guardrail.dataset/index.html
---

# Bedrock Guardrail

Bedrock Guardrail is an AWS resource that helps manage and enforce safety, compliance, and responsible use policies for generative AI applications built with Amazon Bedrock. It allows you to define rules and controls that guide model behavior, ensuring outputs align with organizational standards and reducing risks such as inappropriate or unsafe content generation.

```
aws.bedrock_guardrail
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                    | Description |
| ---------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                         | core | string        |
| account_id                   | core | string        |
| blocked_input_messaging      | core | string        | The message that the guardrail returns when it blocks a prompt.                                                                                              |
| blocked_outputs_messaging    | core | string        | The message that the guardrail returns when it blocks a model response.                                                                                      |
| content_policy               | core | json          | The content policy that was configured for the guardrail.                                                                                                    |
| contextual_grounding_policy  | core | json          | The contextual grounding policy used in the guardrail.                                                                                                       |
| created_at                   | core | timestamp     | The date and time at which the guardrail was created.                                                                                                        |
| cross_region_details         | core | json          | Details about the system-defined guardrail profile that you're using with your guardrail, including the guardrail profile ID and Amazon Resource Name (ARN). |
| description                  | core | string        | The description of the guardrail.                                                                                                                            |
| failure_recommendations      | core | array<string> | Appears if the status of the guardrail is FAILED. A list of recommendations to carry out before retrying the request.                                        |
| guardrail_arn                | core | string        | The ARN of the guardrail.                                                                                                                                    |
| guardrail_id                 | core | string        | The unique identifier of the guardrail.                                                                                                                      |
| kms_key_arn                  | core | string        | The ARN of the KMS key that encrypts the guardrail.                                                                                                          |
| name                         | core | string        | The name of the guardrail.                                                                                                                                   |
| sensitive_information_policy | core | json          | The sensitive information policy that was configured for the guardrail.                                                                                      |
| status                       | core | string        | The status of the guardrail.                                                                                                                                 |
| status_reasons               | core | array<string> | Appears if the status is FAILED. A list of reasons for why the guardrail failed to be created, updated, versioned, or deleted.                               |
| tags                         | core | hstore        |
| topic_policy                 | core | json          | The topic policy that was configured for the guardrail.                                                                                                      |
| updated_at                   | core | timestamp     | The date and time at which the guardrail was updated.                                                                                                        |
| version                      | core | string        | The version of the guardrail.                                                                                                                                |
| word_policy                  | core | json          | The word policy that was configured for the guardrail.                                                                                                       |
