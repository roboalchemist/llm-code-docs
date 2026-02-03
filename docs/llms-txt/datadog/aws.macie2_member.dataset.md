# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.macie2_member.dataset.md

---
title: Macie Member Account Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Macie Member Account Association
---

# Macie Member Account Association

Macie Member Account Association in AWS allows you to link member accounts to an Amazon Macie administrator account. This enables centralized management of sensitive data discovery and security findings across multiple accounts. The administrator can view and manage Macie results for all associated member accounts, helping organizations maintain consistent data security and compliance at scale.

```
aws.macie2_member
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                             | Description |
| ------------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     | The Amazon Web Services account ID for the account.                                                                                                                                                                   |
| administrator_account_id | core | string     | The Amazon Web Services account ID for the administrator account.                                                                                                                                                     |
| arn                      | core | string     | The Amazon Resource Name (ARN) of the account.                                                                                                                                                                        |
| email                    | core | string     | The email address for the account. This value is null if the account is associated with the administrator account through Organizations.                                                                              |
| invited_at               | core | timestamp  | The date and time, in UTC and extended ISO 8601 format, when an Amazon Macie membership invitation was last sent to the account. This value is null if a Macie membership invitation hasn't been sent to the account. |
| master_account_id        | core | string     | (Deprecated) The Amazon Web Services account ID for the administrator account. This property has been replaced by the administratorAccountId property and is retained only for backward compatibility.                |
| relationship_status      | core | string     | The current status of the relationship between the account and the administrator account.                                                                                                                             |
| tags                     | core | hstore_csv |
| updated_at               | core | timestamp  | The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status of the relationship between the account and the administrator account.                                                |
