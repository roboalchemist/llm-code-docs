# Source: https://docs.datadoghq.com/security/default_rules/def-00k-vae.md

---
title: >-
  The certificate authorities file should have permissions of 600 or more
  restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The certificate authorities file should
  have permissions of 600 or more restrictive
---

# The certificate authorities file should have permissions of 600 or more restrictive

## Description{% #description %}

The certificate authorities file should have permissions of 600 or more restrictive. The certificate authorities file controls the authorities used to validate API requests. You should restrict its file permissions to maintain the integrity of the file.

## Remediation{% #remediation %}

Run the following command to modify the file permissions of the file listed in the `--client-ca-file` argument:

```
chmod 600 <filename>
```
