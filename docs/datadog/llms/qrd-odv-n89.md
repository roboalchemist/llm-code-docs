# Source: https://docs.datadoghq.com/security/default_rules/qrd-odv-n89.md

---
title: IAM server certificate should be renewed 30 days before expiration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM server certificate should be
  renewed 30 days before expiration
---

# IAM server certificate should be renewed 30 days before expiration

## Description{% #description %}

Ensure that your IAM service SSL/TLS certificates are renewed 30 days prior to their validity period ending.

## Rationale{% #rationale %}

If a certificate becomes invalid, the communication between the client and AWS resource that implements certificates is no longer secure.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Managed renewal for ACM certificates](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) AWS documentation to set up renewal by validation type (DNS, email, or private PKI).

### From the command line{% #from-the-command-line %}

Follow the [Managed renewal for ACM certificates](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) AWS documentation to set up renewal by validation type (DNS, email, or private PKI).
