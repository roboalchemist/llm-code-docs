# Source: https://docs.datadoghq.com/security/default_rules/def-000-hec.md

---
title: Publicly accessible Lambda function has a critical vulnerability
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible Lambda function has
  a critical vulnerability
---

# Publicly accessible Lambda function has a critical vulnerability

## Description{% #description %}

The policy evaluates AWS Lambda functions to determine if they are publicly accessible and have one or more critical-severity vulnerabilities. Publicly accessible functions with critical vulnerabilities are at a higher risk of malicious attacks, which can compromise data integrity and system security.

## Remediation{% #remediation %}

1. Identify Lambda functions that are publicly accessible and review the associated critical vulnerabilities.
1. Prioritize and apply security patches or updates to address the identified vulnerabilities. If patches are not available, consider implementing alternative security measures.
1. Evaluate the need for public accessibility of the Lambda function. If unnecessary, modify the function's access settings to restrict public access.
