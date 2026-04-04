# Source: https://docs.datadoghq.com/security/default_rules/z23-f9p-six.md

---
title: Password policy should prevent password reuse
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Password policy should prevent password
  reuse
---

# Password policy should prevent password reuse

## Description{% #description %}

IAM password policies can prevent the reuse of a given password by the same user. Datadog recommends that the password policy prevents the reuse of passwords to enhance security.

Preventing password reuse increases account resiliency against brute force login attempts by ensuring that users create unique passwords over time, which strengthens the security posture of the AWS account.

## Remediation{% #remediation %}

For instructions on preventing password reuse in IAM password policies, refer to [Managing an IAM User Password Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html).
