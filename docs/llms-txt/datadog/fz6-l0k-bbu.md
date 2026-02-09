# Source: https://docs.datadoghq.com/security/default_rules/fz6-l0k-bbu.md

---
title: Certificate managed by ACM should be renewed within 7 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Certificate managed by ACM should be
  renewed within 7 days
---

# Certificate managed by ACM should be renewed within 7 days
 
## Description{% #description %}

Renew your SSL/TLS certificate managed by AWS Certificate Manager (ACM) as there are seven day left to renew.

## Rationale{% #rationale %}

Certificates that are not renewed prior to their expiration date become invalid. Invalid certificates make communication between the client and AWS resources insecure.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

ACM automatically renews certificates (if you are using DNS validation) or sends an email notification when expiration is approaching. Follow the [Managed renewal for ACM certificates](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) docs for more information.

### From the command line{% #from-the-command-line %}

1. Run `import-certificate` using the [ARN of the SSL/TLS certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/import-certificate.html) that you want to renew. This will return the ARN of the renewed SSL/TLS certificate.

In the `import-certificate.sh` file:

```bash
    aws acm import-certificate
      --certificate-arn <value>
      --certificate <value>
      --private-key <value>
      --certificate-chain <value>
  
```
