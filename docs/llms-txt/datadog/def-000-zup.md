# Source: https://docs.datadoghq.com/security/default_rules/def-000-zup.md

---
title: >-
  Publicly accessible AWS EC2 instance is vulnerable to CUPS remote code
  execution attack chain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible AWS EC2 instance is
  vulnerable to CUPS remote code execution attack chain
---

# Publicly accessible AWS EC2 instance is vulnerable to CUPS remote code execution attack chain

## Description{% #description %}

Identify when an EC2 instance is publicly accessible on port 631 and is vulnerable to the four vulnerabilities allowing for [remote code execution in CUPS](https://securitylabs.datadoghq.com/articles/emerging-vulnerability-cups).
