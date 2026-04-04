# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/psp_allows_sharing_host_ipc.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/psp_allows_sharing_host_ipc.md

---
title: PSP allows sharing host IPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > PSP allows sharing host IPC
---

# PSP allows sharing host IPC

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `80f93444-b240-4ebb-a4c6-5c40b76c04ea`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)

### Description{% #description %}

PodSecurityPolicy 'spec.hostIPC' allows containers to share the host IPC namespace when set to true. Sharing the host IPC namespace lets processes in a container observe or interfere with IPC resources of other containers or the host, increasing the risk of information disclosure and privilege escalation. 'spec.hostIPC' should be set to false or left undefined to preserve IPC isolation.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  hostIPC: false
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  hostIPC: true
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
```
