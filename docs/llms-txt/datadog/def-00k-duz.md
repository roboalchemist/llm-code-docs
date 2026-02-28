# Source: https://docs.datadoghq.com/security/default_rules/def-00k-duz.md

---
title: The kubelet configuration file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet configuration file should
  be owned by root
---

# The kubelet configuration file should be owned by root

## Description{% #description %}

Ensure that if the kubelet refers to a configuration file with the `--config` argument, that file is owned by `root:root`. The kubelet reads various parameters, including security settings, from a config file specified by the `--config` argument.

## Remediation{% #remediation %}

1. Run the following command based on the file located in the `--config` parameter:

```
chown root:root /etc/kubernetes/kubelet.conf
```
