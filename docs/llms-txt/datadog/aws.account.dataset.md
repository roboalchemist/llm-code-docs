# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.account.dataset.md

---
title: Account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Account
source_url: https://docs.datadoghq.com/data_directory/aws/aws.account.dataset/index.html
---

# Account

The AWS Account resource provides details about an AWS account's contact information. It includes alternate contacts for billing, operations, or security, the primary contact information associated with the account, and the registered primary email address. This resource helps manage and retrieve essential account-level details for communication and compliance purposes.

```
aws.account
```

## Fields

| Title               | ID   | Type   | Data Type                                                                                               | Description |
| ------------------- | ---- | ------ | ------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string |
| account_arn         | core | string |
| account_id          | core | string |
| alternate_contacts  | core | json   | A structure that contains the details for the specified alternate contact.                              |
| contact_information | core | json   | Contains the details of the primary contact information associated with an Amazon Web Services account. |
| tags                | core | hstore |
