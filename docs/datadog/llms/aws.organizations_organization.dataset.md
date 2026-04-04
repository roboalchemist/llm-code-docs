# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.organizations_organization.dataset.md

---
title: Organizations Organization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Organizations Organization
---

# Organizations Organization

AWS Organizations Organization represents the entity that contains all accounts within an AWS Organization. It provides details about the organization such as its unique ID, master account, feature set, and policy support. This resource is used to centrally manage multiple AWS accounts, apply governance controls, and consolidate billing under a single structure.

```
aws.organizations_organization
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Name (ARN) of an organization. For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the Amazon Web Services Service Authorization Reference.                                                                                                                                                                                 |
| available_policy_types | core | json       | Do not use. This field is deprecated and doesn't provide complete information about the policies in your organization. To determine the policies that are enabled and available for use in your organization, use the ListRoots operation instead.                                                                                                                                          |
| feature_set            | core | string     | Specifies the functionality that currently is available to the organization. If set to "ALL", then all features are enabled and policies can be applied to accounts in the organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing functionality is available. For more information, see Enabling all features in your organization in the Organizations User Guide. |
| id                     | core | string     | The unique identifier (ID) of an organization. The regex pattern for an organization ID string requires "o-" followed by from 10 to 32 lowercase letters or digits.                                                                                                                                                                                                                         |
| master_account_arn     | core | string     | The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization. For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the Amazon Web Services Service Authorization Reference.                                                                                                                   |
| master_account_email   | core | string     | The email address that is associated with the Amazon Web Services account that is designated as the management account for the organization.                                                                                                                                                                                                                                                |
| master_account_id      | core | string     | The unique identifier (ID) of the management account of an organization. The regex pattern for an account ID string requires exactly 12 digits.                                                                                                                                                                                                                                             |
| tags                   | core | hstore_csv |
