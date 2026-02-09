# Source: https://docs.datadoghq.com/security/default_rules/8yh-cqk-qbn.md

---
title: MFA should be enabled for the 'root' account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > MFA should be enabled for the 'root'
  account
---

# MFA should be enabled for the 'root' account
 
## Description{% #description %}

The root account is the most privileged user in an AWS account. MFA (multi-factor authentication) adds an extra layer of protection on top of a username and password. With MFA enabled, users are prompted for their username, password, and an authentication code from their AWS MFA device when signing in. Datadog recommends using a dedicated non-personal device for setting up virtual MFA for root accounts to minimize risks like device loss or if the device owner leaves the company.

Enabling MFA provides increased security for console access because it requires the authenticating principal to possess a device that emits a time-sensitive key and have knowledge of a credential. Note that the IAM User root account for GovCloud (US) regions does not have console access, so this control is not applicable for GovCloud (US) regions. Additionally, when Centralized Root Management is enabled in AWS, MFA enforcement for the root user is not applicable. In this case, the root account does not have a password or access key that can be used for authentication, making MFA redundant.

## Remediation{% #remediation %}

For instructions on enabling MFA for the root account, refer to [Managing MFA for Your AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html#enable-virt-mfa-for-root).
