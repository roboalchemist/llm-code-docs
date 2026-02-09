# Source: https://docs.datadoghq.com/security/default_rules/def-000-ohu.md

---
title: CloudFront distributions should use origin access control
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distributions should use
  origin access control
---

# CloudFront distributions should use origin access control
 
## Description{% #description %}

This control verifies that every S3-based origin used in an Amazon CloudFront distribution has origin access control (OAC) enabled. S3-based origins that use static website hosting domains (such as `bucket-name.s3-website.<region>.amazonaws.com`) are excluded from this control, as they are assumed to be intentionally public.

When an S3 bucket serves as the origin for a CloudFront distribution, OAC should be activated to restrict access. This ensures that content is accessible only through the designated CloudFront distribution while preventing direct access from the bucket or other distributions.

Note that origin access identity (OAI) has been deprecated by Amazon in favor of OAC. CloudFront distributions using OAI should be migrated to OAC to benefit from enhanced security controls.

## Remediation{% #remediation %}

For instructions on enabling OAC for a CloudFront distribution, refer to the [Restrict access to an Amazon Simple Storage Service origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) section of the Amazon CloudFront Developer Guide.
