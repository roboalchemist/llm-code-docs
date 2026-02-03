# Source: https://docs.datadoghq.com/security/default_rules/def-000-jrr.md

---
title: >-
  A GKE Cluster's kubelet configuration file should have permissions set to 600
  or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A GKE Cluster's kubelet configuration
  file should have permissions set to 600 or more restrictive
---

# A GKE Cluster's kubelet configuration file should have permissions set to 600 or more restrictive
 
## Description{% #description %}

If the kubelet refers to a configuration file with the `--config` argument, ensure that the file has permissions set to `600` or to a more restrictive setting. If a file is specified, you should restrict its file permissions to maintain the integrity of the file. The file should be writable only by the administrators on the system.

## Remediation{% #remediation %}

Run the following command to fix the kubelet configuration file's permissions:

```bash
chmod 600 /etc/kubernetes/kubelet/kubelet-config.json
```

**Note**: The path above is the default location.
