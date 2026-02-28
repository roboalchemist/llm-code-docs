# Source: https://docs.datadoghq.com/security/default_rules/def-000-kft.md

---
title: >-
  EC2 setting 'Block public access for EBS snapshots' should be enabled and
  enforced by declarative policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 setting 'Block public access for
  EBS snapshots' should be enabled and enforced by declarative policy
---

# EC2 setting 'Block public access for EBS snapshots' should be enabled and enforced by declarative policy

## Description{% #description %}

Enabling the EC2 setting 'Block public access for EBS snapshots' ensures that EBS snapshots cannot accidentally be shared publicly. This setting helps avoid inadvertent data exposure by preventing unauthorised users from accessing EBS snapshots containing sensitive information. **Note**: This setting is configured at a per-account, per-region level. The setting can be configured as either 'Block all sharing' or 'Block new sharing' depending on your requirements.

Enforcing this EC2 setting using AWS Organizations declarative policies provides an additional layer of protection, as the setting must be configured centrally from the organization management account or a delegated administator account.

## Remediation{% #remediation %}

For guidance on enabling this EC2 setting, refer to the [Block public access for Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots.html) section of the Amazon EBS User Guide. For guidance on modifying public access permissions for existing EBS snapshots, refer to the [Share an Amazon EBS snapshot with other AWS accounts](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modifying-snapshot-permissions.html) section of the Amazon EBS User Guide. For guidance on managing declarative policies, refer to the [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) section of the AWS Organizations User Guide.
