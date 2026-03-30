# Source: https://docs.datadoghq.com/security/default_rules/def-000-ocr.md

---
title: Route 53 DNS record pointing to external or nonexistent S3 bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route 53 DNS record pointing to
  external or nonexistent S3 bucket
---

# Route 53 DNS record pointing to external or nonexistent S3 bucket

## Description{% #description %}

This control identifies misconfigured Amazon Route 53 DNS records that point to external or nonexistent S3 buckets. Such misconfigurations can introduce significant security risks, including unauthorized access or domain hijacking. If a DNS record points to an S3 bucket domain that no longer exists, an attacker can register the bucket name and intercept or manipulate traffic intended for the original destination. This could lead to data breaches, phishing attacks, or distribution of unauthorized content, impacting both security and compliance.

## Remediation{% #remediation %}

If the DNS record is a resource record, look at its `value` field. If the DNS record is an alias target, look at its `dns_name` field.

- If the offending S3 bucket exists and belongs to an AWS account that you own but is not integrated to Datadog, follow the [Datadog AWS integration documentation](https://docs.datadoghq.com/integrations/amazon_web_services/) to onboard the account to Datadog. Ensure that resource collection and Cloud Security are correctly configured.
- If the offending S3 bucket exists and belongs to a trusted third-party AWS account, mute the finding and leave a comment documenting the justification.
- If the offending S3 bucket does not exist, refer to the [Editing records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html) section of the Amazon Route 53 Developer Guide for instructions on how to delete or modify the offending record.
