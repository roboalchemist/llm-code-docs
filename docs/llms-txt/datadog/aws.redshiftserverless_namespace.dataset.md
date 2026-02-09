# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshiftserverless_namespace.dataset.md

---
title: Redshift Serverless Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Serverless Namespace
---

# Redshift Serverless Namespace

A Redshift Serverless Namespace in AWS is a logical container that holds database objects, users, and configurations for Amazon Redshift Serverless. It defines the environment where data is stored and queried, while compute resources are managed separately. This separation allows flexible scaling, simplified management, and secure multi-tenant usage without needing to manage clusters directly.

```
aws.redshiftserverless_namespace
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                                                        | Description |
| -------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| account_id                       | core | string        |
| admin_password_secret_arn        | core | string        | The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.                                                                                                                                                |
| admin_password_secret_kms_key_id | core | string        | The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.                                                                                                               |
| admin_username                   | core | string        | The username of the administrator for the first database created in the namespace.                                                                                                                                               |
| creation_date                    | core | timestamp     | The date of when the namespace was created.                                                                                                                                                                                      |
| db_name                          | core | string        | The name of the first database created in the namespace.                                                                                                                                                                         |
| default_iam_role_arn             | core | string        | The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.                                                                                                                                             |
| iam_roles                        | core | array<string> | A list of IAM roles to associate with the namespace.                                                                                                                                                                             |
| kms_key_id                       | core | string        | The ID of the Amazon Web Services Key Management Service key used to encrypt your data.                                                                                                                                          |
| log_exports                      | core | array<string> | The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.                                                                                                          |
| namespace_arn                    | core | string        | The Amazon Resource Name (ARN) associated with a namespace.                                                                                                                                                                      |
| namespace_id                     | core | string        | The unique identifier of a namespace.                                                                                                                                                                                            |
| namespace_name                   | core | string        | The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide. |
| status                           | core | string        | The status of the namespace.                                                                                                                                                                                                     |
| tags                             | core | hstore_csv    |
