# Source: https://docs.datadoghq.com/security/default_rules/def-000-rwh.md

---
title: A GKE Cluster's Kubelet should have the eventRecordQPS entry set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A GKE Cluster's Kubelet should have the
  eventRecordQPS entry set
---

# A GKE Cluster's Kubelet should have the eventRecordQPS entry set
 
## Description{% #description %}

Security relevant information should be captured. The `eventRecordQPS` setting in the Kubelet configuration controls the rate at which events are recorded, limiting the maximum number of events created per second. Setting this value too low may result in important events not being logged. Conversely, setting it to 0 (unlimited) could lead to a denial of service on the Kubelet.

## Remediation{% #remediation %}

Choose one of the following remediation methods. For both methods, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the following JSON to the `<path-to-file>/10-kubeadm.conf` file.

```json
"eventRecordQPS": <integer>
```

**Note**: The default value is 50. The recommended value is 0 for unlimited.

### Executable arguments{% #executable-arguments %}

**Note**: The executable argument has been `deprecated` for this feature.
