# Source: https://docs.datadoghq.com/security/default_rules/def-000-f4v.md

---
title: >-
  EC2 setting 'Allowed AMIs' should be enabled and enforced by declarative
  policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 setting 'Allowed AMIs' should be
  enabled and enforced by declarative policy
---

# EC2 setting 'Allowed AMIs' should be enabled and enforced by declarative policy
 
## Description{% #description %}

Enabling the EC2 setting 'Allowed AMIs' ensures that only approved and trusted Amazon Machine Images are used to launch instances within your environment. By restricting the available AMIs, you can prevent the use of unvetted or potentially compromised images that could introduce security vulnerabilities or malware. **Note**: Previously launched instances are unaffected by this setting. The state of the setting must be `enabled` for this rule to pass.

Enforcing this EC2 setting using AWS Organizations declarative policies provides an additional layer of protection, as the setting must be configured centrally from the organization management account or a delegated administator account.

## Remediation{% #remediation %}

For guidance on enabling this EC2 setting, refer to the [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) section of the Amazon Elastic Compute Cloud User Guide. For guidance on managing declarative policies, refer to the [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) section of the AWS Organizations User Guide.
