# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_ipam_external_resource_verification_token.dataset.md

---
title: IPAM External Resource Verification Token
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > IPAM External Resource Verification
  Token
---

# IPAM External Resource Verification Token

An IPAM External Resource Verification Token in AWS is a temporary token used by Amazon VPC IP Address Manager (IPAM) to verify ownership or association of external resources. It helps ensure that resources outside of IPAM's direct management can be validated and tracked within IPAM workflows, supporting accurate IP address management across accounts and environments.

```
aws.ec2_ipam_external_resource_verification_token
```

## Fields

| Title                                         | ID   | Type       | Data Type                                  | Description |
| --------------------------------------------- | ---- | ---------- | ------------------------------------------ | ----------- |
| _key                                          | core | string     |
| account_id                                    | core | string     |
| ipam_arn                                      | core | string     | ARN of the IPAM that created the token.    |
| ipam_external_resource_verification_token_arn | core | string     | Token ARN.                                 |
| ipam_external_resource_verification_token_id  | core | string     | The ID of the token.                       |
| ipam_id                                       | core | string     | The ID of the IPAM that created the token. |
| ipam_region                                   | core | string     | Region of the IPAM that created the token. |
| not_after                                     | core | timestamp  | Token expiration.                          |
| state                                         | core | string     | Token state.                               |
| status                                        | core | string     | Token status.                              |
| tags                                          | core | hstore_csv |
| token_name                                    | core | string     | Token name.                                |
| token_value                                   | core | string     | Token value.                               |
