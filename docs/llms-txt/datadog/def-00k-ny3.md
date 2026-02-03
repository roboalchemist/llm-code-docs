# Source: https://docs.datadoghq.com/security/default_rules/def-00k-ny3.md

---
title: The client certificate authorities file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The client certificate authorities file
  should be owned by root
---

# The client certificate authorities file should be owned by root
 
## Description{% #description %}

The certificate authorities file ownership should be set to `root:root`. The certificate authorities file controls the authorities used to validate API requests. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to modify the ownership of the file listed in the `--client-ca-file` argument:

```
chown root:root <filename>
```
