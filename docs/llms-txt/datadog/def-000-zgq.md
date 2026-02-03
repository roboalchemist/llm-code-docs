# Source: https://docs.datadoghq.com/security/default_rules/def-000-zgq.md

---
title: EC2 setting 'EBS encryption by default' should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 setting 'EBS encryption by default'
  should be enabled
---

# EC2 setting 'EBS encryption by default' should be enabled
 
## Description{% #description %}

Enabling the EC2 setting 'EBS encryption by default' ensures that all new block storage volumes and snapshots are automatically encrypted, providing data protection at rest. This setting helps to prevent inadvertent data exposure by eliminating the need for manual encryption configuration for each new volume. This aids in maintaining a consistent security posture and simplifies compliance with regulatory requirements for data protection. **Note**: This setting is configured at a per-account, per-region level.

## Remediation{% #remediation %}

For guidance on enforcing encryption of new EBS volumes and snapshots, refer to the [Enable Amazon EBS encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html) section of the Amazon EBS User Guide.
