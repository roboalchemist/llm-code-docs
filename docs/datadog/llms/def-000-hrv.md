# Source: https://docs.datadoghq.com/security/default_rules/def-000-hrv.md

---
title: Publicly accessible EC2 instance should not have open administrative ports
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible EC2 instance should
  not have open administrative ports
---

# Publicly accessible EC2 instance should not have open administrative ports

## Description{% #description %}

This rule checks if an EC2 instance accessible from the public internet has open administrative ports, specifically port 22 (SSH) and port 3389 (RDP). Having these ports open poses a security risk as it can expose the instance to unauthorized access.

## Remediation{% #remediation %}

To remediate this issue, Datadog recommends restricting access to administrative ports (22 for SSH and 3389 for RDP) on your EC2 instances by configuring your security groups to allow connections only from trusted IP addresses. For detailed guidance, see the AWS Security Group documentation, [Amazon EC2 Security Groups for Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).
