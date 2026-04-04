# Source: https://docs.datadoghq.com/security/default_rules/hsh-y5w-hxe.md

---
title: MFA should be enabled for all users with console access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > MFA should be enabled for all users
  with console access
---

# MFA should be enabled for all users with console access

## Description{% #description %}

Multi-Factor Authentication (MFA) adds an extra layer of protection on top of a username and password. With MFA enabled, when a user signs in to an AWS website, they will be prompted for their username, password, and an authentication code from their AWS MFA device. Datadog recommends that you enable MFA for all accounts that have a console password to enhance security.

Enabling MFA provides increased security for console access as it requires the user to possess a device that emits a time-sensitive key, in addition to knowing the credential.

## Remediation{% #remediation %}

For instructions on enabling a virtual multi-factor authentication (MFA) device, refer to the [AWS documentation on enabling MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html).
