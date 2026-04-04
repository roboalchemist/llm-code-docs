# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.organizations_account.dataset.md

---
title: Organizations Account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Organizations Account
---

# Organizations Account

An AWS Organizations Account represents an AWS account that is part of an organization managed through AWS Organizations. It can be either the management account, which has full control over the organization, or a member account, which is governed by policies and consolidated billing. This resource helps centralize account management, apply service control policies, and streamline billing across multiple accounts.

```
aws.organizations_account
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ---------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| arn              | core | string     | The Amazon Resource Name (ARN) of the account. For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the Amazon Web Services Service Authorization Reference.                                                                                                                                                                                                                                |
| email            | core | string     | The email address associated with the Amazon Web Services account. The regex pattern for this parameter is a string of characters that represents a standard internet email address.                                                                                                                                                                                                                                                   |
| id               | core | string     | The unique identifier (ID) of the account. The regex pattern for an account ID string requires exactly 12 digits.                                                                                                                                                                                                                                                                                                                      |
| joined_method    | core | string     | The method by which the account joined the organization.                                                                                                                                                                                                                                                                                                                                                                               |
| joined_timestamp | core | timestamp  | The date the account became a part of the organization.                                                                                                                                                                                                                                                                                                                                                                                |
| name             | core | string     | The friendly name of the account. The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.                                                                                                                                                                                                                                                                         |
| status           | core | string     | The status of the account in the organization. The Status parameter in the Account object will be retired on September 9, 2026. Although both the account State and account Status parameters are currently available in the Organizations APIs (DescribeAccount, ListAccounts, ListAccountsForParent), we recommend that you update your scripts or other code to use the State parameter instead of Status before September 9, 2026. |
| tags             | core | hstore_csv |
