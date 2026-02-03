# Source: https://docs.datadoghq.com/security/default_rules/def-000-rno.md

---
title: CloudFront distributions should encrypt traffic to custom origins
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distributions should encrypt
  traffic to custom origins
---

# CloudFront distributions should encrypt traffic to custom origins
 
## Description{% #description %}

This check verifies if Amazon CloudFront distributions are securing traffic to custom origins. Failure for this control occurs when a CloudFront distribution permits the 'http-only' origin protocol policy. Additionally, failure is also flagged if the distribution's origin protocol policy is 'match-viewer' while the viewer protocol policy is set to 'allow-all'.

Using HTTPS (TLS) can enhance security by safeguarding against eavesdropping or manipulation of network traffic. It is advisable to only allow encrypted connections through HTTPS (TLS).

## Remediation{% #remediation %}

For instructions on how to mandate encryption for communication between CloudFront and your custom origin by updating the Origin Protocol Policy, refer to [Requiring HTTPS for communication between CloudFront and your custom origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html) in the Amazon CloudFront Developer Guide.
