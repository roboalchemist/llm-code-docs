# Source: https://docs.datadoghq.com/security/default_rules/def-000-asx.md

---
title: >-
  Publicly accessible Google VM instance contains critical vulnerability
  CVE-2024-3094 (RCE in liblzma and xz versions 5.6.0 and 5.6.1)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible Google VM instance
  contains critical vulnerability CVE-2024-3094 (RCE in liblzma and xz versions
  5.6.0 and 5.6.1)
---

# Publicly accessible Google VM instance contains critical vulnerability CVE-2024-3094 (RCE in liblzma and xz versions 5.6.0 and 5.6.1)

## Description{% #description %}

A publicly accessible host is affected by [CVE-2024-3094](https://nvd.nist.gov/vuln/detail/CVE-2024-3094). The vulnerability is found in `liblzma` and `xz` versions 5.6.0 and 5.6.1. The vulnerable libraries contained the ability for remote code execution.

Not all distributions are affected, for more information see the [security center post](https://app.datadoghq.com/security/csm?fa_account=subscription_name%23pde-research-staging&panels=security-center%7Cscp-singleton%7CsecurityCardId%3A27&sort=&timestamp=1711981381204&live=true).

## Remediation{% #remediation %}

1. Evaluate the need for public accessability for your instance and remove it from the public internet if possible.
1. To manually determine if your systems are running the affected version you can use the following shell command: `$ xz --version`
1. It is recommended to downgrade the XZ Utils library to an uncompromised version such as 5.4.6. In addition, if you are using an affected distribution it is encouraged to hunt for any malicious activity involving the impacted instance.
