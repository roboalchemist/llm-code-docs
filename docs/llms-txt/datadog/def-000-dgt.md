# Source: https://docs.datadoghq.com/security/default_rules/def-000-dgt.md

---
title: RDS instances should be deployed inside of a VPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS instances should be deployed inside
  of a VPC
---

# RDS instances should be deployed inside of a VPC

## Description{% #description %}

This validation verifies if an Amazon RDS instance is set up in an EC2-VPC.

VPCs offer various network security measures to protect RDS resources, such as VPC Endpoints, network ACLs, and security groups. To utilize these security measures effectively, it is advisable to deploy your RDS instances within an EC2-VPC.

## Remediation{% #remediation %}

For details on deploying RDS instances to a VPC, please refer to the [Updating the VPC for a DB instance section in the Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.VPC2VPC).
