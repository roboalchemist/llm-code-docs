# Source: https://docs.datadoghq.com/security/default_rules/def-000-1vr.md

---
title: Publicly accessible EC2 host is running IMDSv1 and has an SSRF vulnerability
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible EC2 host is running
  IMDSv1 and has an SSRF vulnerability
---

# Publicly accessible EC2 host is running IMDSv1 and has an SSRF vulnerability

## Description{% #description %}

A publicly accessible compute instance is affected by an SSRF vulnerability and is running IMDSv1.

Using IMDSv1 increases the risk of attackers stealing your AWS IAM credentials with this vulnerability. In this scenario, attackers can abuse applications running on an EC2 instance to steal your keys and begin accessing your cloud environment. For more information, see our Datadog Security Labs [article](https://securitylabs.datadoghq.com/articles/misconfiguration-spotlight-imds/) on IMDS security and why upgrading to IMDSv2 is essential.

## Remediation{% #remediation %}

1. Review the associated vulnerabilities in your service and perform remediation.
1. Follow the [Transition to using Instance Metadata Service Version 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.html) docs to learn how to transition and reconfigure your software.
