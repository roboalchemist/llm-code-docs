# Source: https://docs.datadoghq.com/security/default_rules/def-000-mcz.md

---
title: CloudFront distribution contains S3 origin with external or nonexistent bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distribution contains S3
  origin with external or nonexistent bucket
---

# CloudFront distribution contains S3 origin with external or nonexistent bucket
 
## Description{% #description %}

This control identifies AWS CloudFront distributions with S3 origins pointing to external or nonexistent buckets. A misconfiguration like this could expose the distribution to unauthorized access or hijacking risks. When a CloudFront distribution is configured with a nonexistent S3 bucket as its origin, traffic routed to the origin is at risk. Attackers could exploit this misconfiguration by creating a new S3 bucket with the same name in a different AWS account, potentially serving malicious content through the affected CloudFront distribution. This could lead to data breaches, phishing attacks, or distribution of unauthorized content, any of which would impact both security and compliance.

The actual exploitability of a CloudFront distribution with a nonexistent S3 origin depends on multiple additional factors, including but not limited to:

- CloudFront distribution behaviour configuration
- CloudFront Functions or Lambda@Edge configuration
- AWS WAF configuration

These additional factors are not assessed by this control.

**Note**: Only CloudFront distributions that are enabled and fully deployed are assessed.

## Remediation{% #remediation %}

Assess each item in the distribution origin configuration that refers to an S3 bucket.

- If the offending S3 bucket exists and belongs to an AWS account that you own but is not integrated to Datadog, follow the [Datadog AWS integration documentation](https://docs.datadoghq.com/integrations/amazon_web_services/) to onboard the account. Ensure that resource collection and Cloud Security are correctly configured.
- If the offending S3 bucket exists and belongs to a trusted third-party AWS account, mute the finding and leave a comment documenting the justification.
- If the offending S3 bucket does not exist, refer to the [Origin settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOrigin) section of the Amazon CloudFront Developer Guide for instructions on how to delete or modify the offending origin.
