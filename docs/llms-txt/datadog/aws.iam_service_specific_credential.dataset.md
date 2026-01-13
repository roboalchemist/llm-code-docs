# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_service_specific_credential.dataset.md

---
title: Service-Specific Credential Metadata
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service-Specific Credential Metadata
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iam_service_specific_credential.dataset/index.html
---

# Service-Specific Credential Metadata

Service-Specific Credential Metadata in AWS IAM provides details about credentials that are created for a specific AWS service. These credentials allow a user to authenticate directly with the service without using their standard IAM credentials. The metadata includes information such as the service name, user name, status, and creation details, helping administrators manage and track the use of these specialized credentials.

```
aws.iam_service_specific_credential
```

## Fields

| Title                          | ID   | Type      | Data Type                                                                                                                                                    | Description |
| ------------------------------ | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                           | core | string    |
| account_id                     | core | string    |
| create_date                    | core | timestamp | The date and time, in ISO 8601 date-time format, when the service-specific credential were created.                                                          |
| expiration_date                | core | timestamp | The date and time when the service specific credential expires. This field is only present for Bedrock API keys that were created with an expiration period. |
| service_credential_alias       | core | string    | For Bedrock API keys, this is the public portion of the credential that includes the IAM user name and a suffix containing version and creation information. |
| service_name                   | core | string    | The name of the service associated with the service-specific credential.                                                                                     |
| service_specific_credential_id | core | string    | The unique identifier for the service-specific credential.                                                                                                   |
| service_user_name              | core | string    | The generated user name for the service-specific credential.                                                                                                 |
| status                         | core | string    | The status of the service-specific credential. Active means that the key is valid for API calls, while Inactive means it is not.                             |
| tags                           | core | hstore    |
| user_name                      | core | string    | The name of the IAM user associated with the service-specific credential.                                                                                    |
