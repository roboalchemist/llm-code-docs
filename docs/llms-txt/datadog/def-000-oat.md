# Source: https://docs.datadoghq.com/security/default_rules/def-000-oat.md

---
title: S3 bucket policy should deny HTTP requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 bucket policy should deny HTTP
  requests
---

# S3 bucket policy should deny HTTP requests
 
## Description{% #description %}

At the Amazon S3 bucket level, you can configure permissions through a bucket policy to make objects accessible only through HTTPS. By default, Amazon S3 allows both HTTP and HTTPS requests. To enforce HTTPS-only access, you must explicitly deny HTTP requests. Bucket policies allowing HTTPS but not explicitly denying HTTP do not comply with this security recommendation. Implementing such a policy helps safeguard data by ensuring only encrypted data transfers using HTTPS, thereby enhancing security.

## Remediation{% #remediation %}

For instructions on configuring your Amazon S3 bucket policy to require HTTPS, refer to the [Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html) and the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).
