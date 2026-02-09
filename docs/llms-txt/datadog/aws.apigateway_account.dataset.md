# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_account.dataset.md

---
title: API Gateway Account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Account
---

# API Gateway Account

The API Gateway Account resource in AWS represents the account-level settings for Amazon API Gateway. It includes configuration details such as the CloudWatch role ARN used for logging and monitoring, as well as limits and quotas that apply across all APIs in the account. This resource helps manage global API Gateway settings rather than individual API configurations.

```
aws.apigateway_account
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                                            | Description |
| ------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| api_key_version     | core | string        | The version of the API keys used for the account.                                                                                    |
| cloudwatch_role_arn | core | string        | The ARN of an Amazon CloudWatch role for the current Account.                                                                        |
| features            | core | array<string> | A list of features supported for the account. When usage plans are enabled, the features list will include an entry of "UsagePlans". |
| tags                | core | hstore_csv    |
| throttle_settings   | core | json          | Specifies the API request limits configured for the current Account.                                                                 |
