# Source: https://docs.datadoghq.com/security/default_rules/def-000-cbi.md

---
title: >-
  EC2 setting 'VPC Block Public Access' should be enabled and be enforced by
  declarative policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 setting 'VPC Block Public Access'
  should be enabled and be enforced by declarative policy
---

# EC2 setting 'VPC Block Public Access' should be enabled and be enforced by declarative policy

## Description{% #description %}

Enabling the EC2 setting 'VPC Block Public Access' is an important preventative measure against inadvertent exposure of EC2 instances and other resources within a Virtual Private Cloud (VPC). This setting acts as a centralized control, overriding individual security group or network ACL configurations that might otherwise allow unrestricted public access. By enforcing this boundary, it helps to mitigate the risk of data breaches and unauthorized access stemming from misconfigurations.

For this control to pass, the option 'Internet gateway block direction' must be set to `block-bidirectional` or `block-ingress`. Exclusions can be configured as necessary for VPCs or subnets that are required to have public access.

Enforcing this EC2 setting using AWS Organizations declarative policies provides an additional layer of protection, as the setting must be configured centrally from the organization management account or a delegated administator account.

## Remediation{% #remediation %}

For guidance on enabling this EC2 setting, refer to the [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) section of the Amazon Virtual Private Cloud User Guide. For guidance on managing declarative policies, refer to the [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) section of the AWS Organizations User Guide.
