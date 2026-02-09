# Source: https://docs.datadoghq.com/security/default_rules/def-000-sr2.md

---
title: EC2 instances managed by SSM should have a compliant patch status
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 instances managed by SSM should
  have a compliant patch status
---

# EC2 instances managed by SSM should have a compliant patch status
 
## Description{% #description %}

This control verifies the status of Systems Manager patch compliance, ensuring that patch installations on EC2 instances are successful. If there are any patch compliance events with a status of `NON_COMPLIANT`, the control will fail. This check applies only to EC2 instances managed by Systems Manager Patch Manager.

Keeping your EC2 instances patched according to organizational requirements helps to minimize the attack surface within your AWS accounts.

## Remediation{% #remediation %}

For guidance on configuring and troubleshooting Patch Manager, refer to the [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) section of the AWS Systems Manager User Guide.
