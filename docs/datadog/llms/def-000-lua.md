# Source: https://docs.datadoghq.com/security/default_rules/def-000-lua.md

---
title: >-
  EC2 setting 'IMDS Defaults' should enforce IMDSv2 by default and be enforced
  by declarative policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 setting 'IMDS Defaults' should
  enforce IMDSv2 by default and be enforced by declarative policy
---

# EC2 setting 'IMDS Defaults' should enforce IMDSv2 by default and be enforced by declarative policy

## Description{% #description %}

Configuring the EC2 setting 'IMDS Defaults' to require instance metadata service (IMDS) version 2 reduces the chance of launching exploitable EC2 instances. Enforcing IMDSv2 is a critical security measure for EC2 instances as it helps to mitigate server-side request forgery (SSRF) vulnerabilities present in IMDSv1. The session-oriented approach of IMDSv2 requires a PUT request to retrieve a session token, which protects against unauthorized metadata access. **Note**: This setting is configured at a per-account, per-region level. Additionally, you can override the IMDS defaults during or after launching an instance, therefore this is not a fully preventative feature.

Enforcing this EC2 setting using AWS Organizations declarative policies provides an additional layer of protection, as the setting must be configured centrally from the organization management account or a delegated administator account.

## Remediation{% #remediation %}

For guidance on enabling this EC2 setting, refer to the [Require the use of IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html) section of the Amazon Elastic Compute Cloud User Guide. For guidance on managing declarative policies, refer to the [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) section of the AWS Organizations User Guide.
