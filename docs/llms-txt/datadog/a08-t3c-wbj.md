# Source: https://docs.datadoghq.com/security/default_rules/a08-t3c-wbj.md

---
title: Certificates managed by ACM should be validated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Certificates managed by ACM should be
  validated
---

# Certificates managed by ACM should be validated
 
## Description{% #description %}

All Secure Socket Layer/Transport Layer Security (SSL/TLS) certificates in Amazon Certificate Manager (ACM) should be validated.

## Rationale{% #rationale %}

[Requests for ACM certificates time out if they are not validated within 72 hours](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-timed-out.html). ACM provides managed renewal for your Amazon-issued SSL/TLS certificates that are used with other AWS resources.

[ACM either renews your certificates automatically (if you are using DNS validation)](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html), or it sends you email notices when expiration is approaching. These services are provided for both public and private ACM certificates. However, renewal for other certificates must be done manually. If a certificate is not validated, it can interrupt an application or service.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Setting Up DNS Validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html#setting-up-dns-validation) or [Resending Validation Email](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html#gs-acm-resend) docs to validate a certificate in the AWS Console or by email.

### From the command line{% #from-the-command-line %}

1. Run `resend-validation-email` using the ARN of the invalid certificate with your `domain` and `validation-domain`.

   ```
   aws acm resend-validation-email
     --certificate-arn arn:aws:acm:us-east-1:1234567890:certificate/a1b2345c-d678-9123-4567-89ab12c2345d
     --domain www.example.com
     --validation-domain example.com
   ```

1. Click the link in the generated email to navigate to the Amazon Certificates Approvals page, and click the `I Approve` button.
