# Source: https://docs.datadoghq.com/security/default_rules/2g5-b7o-dqd.md

---
title: Certificate managed by ACM should not be expired
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Certificate managed by ACM should not
  be expired
---

# Certificate managed by ACM should not be expired
 
## Description{% #description %}

Remove expired Secure Socket Layer/Transport Layer Security (SSL/TLS) certificates with AWS Certificate Manager (ACM).

## Rationale{% #rationale %}

Expired AWS ACM SSL/TLS certificates that are deployed to another resource are at risk of triggering front-end errors and compromising the credibility of a web application.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Deleting Certificates Managed by ACM](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-delete.html) docs to learn how to delete SSL/TLS certifications in the AWS Console.

### From the command line{% #from-the-command-line %}

1. Run the [`delete-certificate`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/delete-certificate.html) command to remove the invalid certificate.

   ```
   aws acm delete-certificate --certificate-arn insert-certificate-arn-here
   ```
