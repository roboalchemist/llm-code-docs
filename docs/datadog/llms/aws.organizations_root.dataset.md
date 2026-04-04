# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.organizations_root.dataset.md

---
title: Organizations Root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Organizations Root
---

# Organizations Root

The AWS Organizations Root is the top-level container in an AWS Organization. It serves as the starting point for all accounts within the organization and allows you to apply service control policies (SCPs) across all organizational units and accounts. Every organization has exactly one root, and it cannot be removed.

```
aws.organizations_root
```

## Fields

| Title        | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key         | core | string     |
| account_id   | core | string     |
| arn          | core | string     | The Amazon Resource Name (ARN) of the root. For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the Amazon Web Services Service Authorization Reference.                                                                                                                                                                                                         |
| id           | core | string     | The unique identifier (ID) for the root. The ID is unique to the organization only. The regex pattern for a root ID string requires "r-" followed by from 4 to 32 lowercase letters or digits.                                                                                                                                                                                                               |
| name         | core | string     | The friendly name of the root. The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.                                                                                                                                                                                                                                                  |
| policy_types | core | json       | The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts. Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using EnablePolicyType and DisablePolicyType. Use DescribeOrganization to see the availability of the policy types in that organization. |
| tags         | core | hstore_csv |
