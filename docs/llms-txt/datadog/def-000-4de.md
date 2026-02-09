# Source: https://docs.datadoghq.com/security/default_rules/def-000-4de.md

---
title: >-
  EC2 setting 'EC2 Serial Console access' should be disabled and be enforced by
  declarative policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 setting 'EC2 Serial Console access'
  should be disabled and be enforced by declarative policy
---

# EC2 setting 'EC2 Serial Console access' should be disabled and be enforced by declarative policy
 
## Description{% #description %}

Disabling the EC2 setting 'EC2 Serial Console access' prevents the use of low-level serial connections to EC2 instances, which can be abused to bypass higher-level security controls. This access method provides an alternative path for interaction that may not be monitored by logging and security tools, creating a potential blind spot. By deactivating it, you reduce the overall attack surface of your instances and minimize potential vectors for unauthorized access.

Enforcing this EC2 setting using AWS Organizations declarative policies provides an additional layer of protection, as the setting must be configured centrally from the organization management account or a delegated administator account.

## Remediation{% #remediation %}

For guidance on enabling this EC2 setting, refer to the [Configure access to the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html) section of the Amazon Elastic Compute Cloud User Guide. For guidance on managing declarative policies, refer to the [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) section of the AWS Organizations User Guide.
