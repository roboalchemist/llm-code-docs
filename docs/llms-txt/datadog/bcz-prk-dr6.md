# Source: https://docs.datadoghq.com/security/default_rules/bcz-prk-dr6.md

---
title: Access keys should be rotated every 90 days or less
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Access keys should be rotated every 90
  days or less
---

# Access keys should be rotated every 90 days or less
 
## Description{% #description %}

Access keys consist of an access key ID and a secret access key, and they are used to sign programmatic requests made to AWS. AWS users need their own access keys to perform tasks using the AWS CLI, Tools for Windows PowerShell, AWS SDKs, or direct HTTP calls using the APIs for individual AWS services. It is important to regularly rotate all access keys to maintain security.

Rotating access keys reduces the risk of keys associated with a compromised or terminated account being exploited. Regular rotation ensures that old keys, which may have been lost, cracked, or stolen, cannot be used to access data.

## Remediation{% #remediation %}

For instructions on rotating access keys safely and effectively, refer to [Rotating Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials).
