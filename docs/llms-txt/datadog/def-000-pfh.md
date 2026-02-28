# Source: https://docs.datadoghq.com/security/default_rules/def-000-pfh.md

---
title: CloudFront distributions should use custom SSL/TLS certificates
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distributions should use
  custom SSL/TLS certificates
---

# CloudFront distributions should use custom SSL/TLS certificates

## Description{% #description %}

This check verifies whether CloudFront distributions are using the SSL/TLS certificate provided by CloudFront as the default option. The check is successful if a custom SSL/TLS certificate is being used by the CloudFront distribution. Conversely, the check fails if the CloudFront distribution is still using the default SSL/TLS certificate.

Custom SSL/TLS certificates enable users to access content using different domain names. It is recommended to store custom certificates in AWS Certificate Manager or IAM.

## Remediation{% #remediation %}

For instructions on adding an alternate domain name to a CloudFront distribution that uses a custom SSL/TLS certificate, refer to [Adding an alternate domain name](https://docs.aws.amazon.com/config/latest/developerguide/aws-config-managed-rules-cloudformation-templates.html) in the Amazon CloudFront Developer Guide.
