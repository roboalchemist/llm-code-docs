# Source: https://docs.datadoghq.com/security/default_rules/def-000-x5f.md

---
title: >-
  EC2 setting 'Block public access for AMIs' should be enabled and enforced by
  declarative policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 setting 'Block public access for
  AMIs' should be enabled and enforced by declarative policy
---

# EC2 setting 'Block public access for AMIs' should be enabled and enforced by declarative policy

## Description{% #description %}

Enabling the EC2 setting 'Block public access for AMIs' ensures that AMIs cannot accidentally be shared publicly. This setting helps avoid inadvertent data exposure by preventing unauthorised users from accessing AMIs containing sensitive information. **Note**: This setting is configured at a per-account, per-region level. Additionally, the setting only prevents public access from the time it is enabled. AMIs made publicly accessible before the setting is enabled continue to be publicly accessible and must be manually remediated.

Enforcing this EC2 setting using AWS Organizations declarative policies provides an additional layer of protection, as the setting must be configured centrally from the organization management account or a delegated administator account.

## Remediation{% #remediation %}

For guidance on enabling this EC2 setting, refer to the [Manage the block public access setting for AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-block-public-access-for-amis.html) section of the Amazon Elastic Compute Cloud User Guide. For guidance on modifying public access permissions for existing AMIs, refer to the [Make your AMI publicly available for use in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-intro.html) section of the Amazon Elastic Compute Cloud User Guide. For guidance on managing declarative policies, refer to the [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) section of the AWS Organizations User Guide.
