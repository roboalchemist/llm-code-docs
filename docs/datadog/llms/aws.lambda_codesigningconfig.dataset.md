# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lambda_codesigningconfig.dataset.md

---
title: Lambda Code Signing Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lambda Code Signing Config
---

# Lambda Code Signing Config

This table represents the Lambda Code Signing Config resource from Amazon Web Services.

```
aws.lambda_codesigningconfig
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                               | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| allowed_publishers      | core | json       | List of allowed publishers.                                                                                             |
| code_signing_config_arn | core | string     | The Amazon Resource Name (ARN) of the Code signing configuration.                                                       |
| code_signing_config_id  | core | string     | Unique identifer for the Code signing configuration.                                                                    |
| code_signing_policies   | core | json       | The code signing policy controls the validation failure action for signature mismatch or expiry.                        |
| description             | core | string     | Code signing configuration description.                                                                                 |
| last_modified           | core | string     | The date and time that the Code signing configuration was last modified, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD). |
| tags                    | core | hstore_csv |
