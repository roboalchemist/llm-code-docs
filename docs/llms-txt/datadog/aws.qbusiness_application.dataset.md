# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qbusiness_application.dataset.md

---
title: Q Business Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Q Business Application
---

# Q Business Application

Q Business Application in AWS represents an application resource within the Amazon Q Business service. It provides details about a specific application instance, including its configuration, status, and metadata. This resource is typically used to retrieve information about an existing Q Business application so that you can manage or integrate it with other AWS services.

```
aws.qbusiness_application
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                | Description |
| ------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| account_id                      | core | string        |
| application_arn                 | core | string        | The Amazon Resource Name (ARN) of the Amazon Q Business application.                                                                     |
| application_id                  | core | string        | The identifier of the Amazon Q Business application.                                                                                     |
| attachments_configuration       | core | json          | Settings for whether end users can upload files directly during chat.                                                                    |
| auto_subscription_configuration | core | json          | Settings for auto-subscription behavior for this application. This is only applicable to SAML and OIDC applications.                     |
| client_ids_for_oidc             | core | array<string> | The OIDC client ID for a Amazon Q Business application.                                                                                  |
| created_at                      | core | timestamp     | The Unix timestamp when the Amazon Q Business application was last updated.                                                              |
| description                     | core | string        | A description for the Amazon Q Business application.                                                                                     |
| encryption_configuration        | core | json          | The identifier of the Amazon Web Services KMS key that is used to encrypt your data. Amazon Q Business doesn't support asymmetric keys.  |
| error                           | core | json          | If the Status field is set to ERROR, the ErrorMessage field contains a description of the error that caused the synchronization to fail. |
| iam_identity_provider_arn       | core | string        | The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.                                   |
| identity_center_application_arn | core | string        | The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance attached to your Amazon Q Business application.                   |
| identity_type                   | core | string        | The authentication type being used by a Amazon Q Business application.                                                                   |
| personalization_configuration   | core | json          | Configuration information about chat response personalization. For more information, see Personalizing chat responses.                   |
| q_apps_configuration            | core | json          | Settings for whether end users can create and use Amazon Q Apps in the web experience.                                                   |
| quick_sight_configuration       | core | json          | The Amazon QuickSight authentication configuration for the Amazon Q Business application.                                                |
| role_arn                        | core | string        | The Amazon Resource Name (ARN) of the IAM with permissions to access your CloudWatch logs and metrics.                                   |
| status                          | core | string        | The status of the Amazon Q Business application.                                                                                         |
| tags                            | core | hstore_csv    |
| updated_at                      | core | timestamp     | The Unix timestamp when the Amazon Q Business application was last updated.                                                              |
