# Source: https://docs.datadoghq.com/security/default_rules/def-002-rds.md

---
title: Publicly accessible RDS database stores sensitive data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible RDS database stores
  sensitive data
---

# Publicly accessible RDS database stores sensitive data

## Description{% #description %}

A publicly accessible database containing sensitive data increases the likelihood of brute force attacks successfully granting access, which can be used by an attacker for unauthorized data access or destruction of sensitive information. Sensitive data could include personally identifiable information (PII), credentials, financial information, and network or device information. For more details on how sensitive data is detected, see the [official documentation](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning/#data-security).

## Remediation{% #remediation %}

1. Modify the database instance to disable public accessibility. Review [Hiding a DB instance in a VPC from the internet](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.HidingInstance) for more information on how to disable public accessibility.
1. Confirm that the database instance is only accessible from trusted sources. See [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html) for more information on how to configure security groups.
