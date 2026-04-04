# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/psp_with_unrestricted_access_to_host_path.md

---
title: PSP with unrestricted access to host path
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > PSP with unrestricted access to host path
---

# PSP with unrestricted access to host path

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `de4421f1-4e35-43b4-9783-737dd4e4a47e`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Resource Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems)

### Description{% #description %}

PodSecurityPolicy should set `readOnly` to `true` for every entry in `spec.allowedHostPaths`. The `spec.allowedHostPaths` attribute must be defined and not null, and each allowed host path must include `readOnly: true`. Entries with `readOnly` undefined or set to `false`, or a missing `spec.allowedHostPaths`, are reported.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  hostIPC: false
  allowedHostPaths:
    - pathPrefix: "/foo"
      readOnly: true
  runAsUser:
    rule: 'RunAsAny'
  seLinux:
    rule: 'RunAsAny'
  supplementalGroups:
    rule: 'RunAsAny'
  fsGroup:
    rule: 'RunAsAny'
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  hostIPC: false
  allowedHostPaths:
  - pathPrefix: /dev
  runAsUser:
    rule: 'RunAsAny'
  seLinux:
    rule: 'RunAsAny'
  supplementalGroups:
    rule: 'RunAsAny'
  fsGroup:
    rule: 'RunAsAny'
```

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  hostIPC: false
  allowedHostPaths:
  - pathPrefix: /dev
    readOnly: false
  runAsUser:
    rule: 'RunAsAny'
  seLinux:
    rule: 'RunAsAny'
  supplementalGroups:
    rule: 'RunAsAny'
  fsGroup:
    rule: 'RunAsAny'
```

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  hostIPC: false
  runAsUser:
    rule: 'RunAsAny'
  seLinux:
    rule: 'RunAsAny'
  supplementalGroups:
    rule: 'RunAsAny'
  fsGroup:
    rule: 'RunAsAny'
```
