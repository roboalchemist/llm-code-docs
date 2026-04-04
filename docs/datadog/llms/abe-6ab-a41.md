# Source: https://docs.datadoghq.com/security/default_rules/abe-6ab-a41.md

---
title: >-
  CloudFront distribution should have a security policy requiring a secure
  version of TLS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distribution should have a
  security policy requiring a secure version of TLS
---

# CloudFront distribution should have a security policy requiring a secure version of TLS

## Description{% #description %}

Ensure that AWS CloudFront distributions are configured with a security policy that mandates the use of TLS v1.2 or newer. Utilizing TLS v1.2 as the baseline protocol enhances security by providing robust encryption methods, thereby strengthening the protection of your application's data in transit.

## Remediation{% #remediation %}

To configure or update the TLS version for an AWS CloudFront distribution, please consult the AWS documentation detailing the supported protocols and ciphers between viewers and CloudFront. This will guide you in selecting an appropriate security policy that enforces TLS v1.2 or higher, ensuring your distribution meets contemporary security standards.

For detailed instructions, refer to the [AWS CloudFront Documentation on Supported Protocols and Ciphers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).
