# Source: https://docs.datadoghq.com/security/default_rules/def-000-i9l.md

---
title: Publicly accessible EC2 instance uses IMDSv1
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible EC2 instance uses
  IMDSv1
---

# Publicly accessible EC2 instance uses IMDSv1

## Description{% #description %}

A publicly-accessible EC2 instance uses the Instance Metadata Service (IMDS) Version 1.

Using IMDSv1 increases the risk of attackers stealing your AWS IAM credentials via vulnerabilities like Server-Side Request Forgery (SSRF). In this scenario, attackers can abuse applications running on an EC2 instance to steal your keys and begin accessing your cloud environment. For more information, see our Datadog Security Labs [article](https://securitylabs.datadoghq.com/articles/misconfiguration-spotlight-imds/) on IMDS security and why upgrading to IMDSv2 is essential.

## Remediation{% #remediation %}

1. Follow the [Transition to using Instance Metadata Service Version 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.html) docs to learn how to transition and reconfigure your software.
