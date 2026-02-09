# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_parameter.dataset.md

---
title: Systems Manager Parameter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Parameter
---

# Systems Manager Parameter

Systems Manager Parameter in AWS is a resource that stores configuration data and secrets in a secure, hierarchical way. It allows you to manage values such as database strings, passwords, or license codes, and retrieve them programmatically or through the AWS Management Console. Parameters can be plain text, encrypted with AWS KMS, or organized with naming conventions for easier management. This helps centralize configuration, improve security, and simplify automation across AWS services and applications.

```
aws.ssm_parameter
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                 | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| allowed_pattern    | core | string     | A parameter name can include only the following letters and symbols. a-zA-Z0-9_.-                                         |
| arn                | core | string     | The Amazon Resource Name (ARN) of the parameter.                                                                          |
| data_type          | core | string     | The data type of the parameter, such as text or aws:ec2:image. The default is text.                                       |
| description        | core | string     | Description of the parameter actions.                                                                                     |
| key_id             | core | string     | The alias of the Key Management Service (KMS) key used to encrypt the parameter. Applies to SecureString parameters only. |
| last_modified_date | core | timestamp  | Date the parameter was last changed or updated.                                                                           |
| last_modified_user | core | string     | Amazon Resource Name (ARN) of the Amazon Web Services user who last changed the parameter.                                |
| name               | core | string     | The parameter name.                                                                                                       |
| policies           | core | json       | A list of policies associated with a parameter.                                                                           |
| tags               | core | hstore_csv |
| tier               | core | string     | The parameter tier.                                                                                                       |
| type               | core | string     | The type of parameter. Valid parameter types include the following: String, StringList, and SecureString.                 |
| version            | core | int64      | The parameter version.                                                                                                    |
