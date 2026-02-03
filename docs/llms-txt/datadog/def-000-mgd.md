# Source: https://docs.datadoghq.com/security/default_rules/def-000-mgd.md

---
title: The 'root' user account should use hardware-based MFA
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The 'root' user account should use
  hardware-based MFA
---

# The 'root' user account should use hardware-based MFA
 
## Description{% #description %}

The root user account is the most privileged user in an AWS account. MFA adds an extra layer of protection on top of a username and password. When a user signs in to an AWS website that has MFA enabled, they are prompted for their username and password, as well as an authentication code from their AWS MFA device. Datadog recommends for Level 2 security that you protect the root user account with a hardware MFA device due to its smaller attack surface compared to a virtual MFA. Using a hardware MFA device reduces the vulnerability introduced by mobile devices where virtual MFAs typically reside. However, if managing a single hardware MFA across many AWS accounts poses challenges, you might consider applying this recommendation selectively to the highest security accounts. In cases where [Centralized Root Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) is enabled, MFA enforcement for the root user is not applicable. In this case, the root account does not have a password or access key that can be used for authentication, making MFA redundant.

## Remediation{% #remediation %}

For instructions on enabling a hardware MFA for the root account, refer to [Enabling Hardware MFA for Your AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html#enable-hw-mfa-for-root).
