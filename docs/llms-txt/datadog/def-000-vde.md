# Source: https://docs.datadoghq.com/security/default_rules/def-000-vde.md

---
title: S3 general purpose buckets should have static website hosting disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 general purpose buckets should have
  static website hosting disabled
---

# S3 general purpose buckets should have static website hosting disabled
 
## Description{% #description %}

AWS S3 bucket website hosting should not be enabled because it increases the chance of accidentally exposing sensitive data and does not consistently support HTTPS, potentially leading to insecure connections and data interception. Additionally, it lacks advanced security features such as authentication, DDoS protection, and detailed access logging, which are provided by services like CloudFront. S3 bucket website hosting is also incompatible with the S3 Block Public Access (BPA) feature when all BPA controls are enabled.

## Remediation{% #remediation %}

For guidance on securely configuring static S3 website hosting, refer to the [Restrict access to an Amazon Simple Storage Service origin](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started-cloudfront-overview.html) section of the Amazon CloudFront Developer Guide.
