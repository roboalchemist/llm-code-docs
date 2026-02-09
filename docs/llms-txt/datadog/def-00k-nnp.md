# Source: https://docs.datadoghq.com/security/default_rules/def-00k-nnp.md

---
title: >-
  The kubelet configuration file should have permissions of 600 or more
  restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet configuration file should
  have permissions of 600 or more restrictive
---

# The kubelet configuration file should have permissions of 600 or more restrictive
 
## Description{% #description %}

Ensure that if the kubelet refers to a configuration file with the `--config` argument, that file has permissions of 600 or more restrictive. The kubelet reads various parameters, including security settings, from the config file. The file should be writable by only the administrators on the system.

## Remediation{% #remediation %}

1. Run the following command based on the file located in the `--config` parameter:

```gdscript3
chmod 600 /var/lib/kubelet/config.yaml
```
