# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/root_container_not_mounted_as_read_only.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/root_container_not_mounted_as_read_only.md

---
title: Root container not mounted as read-only
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Root container not mounted as read-only
---

# Root container not mounted as read-only

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a9c2f49d-0671-4fc9-9ece-f4e261e128d0`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Build Process

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

### Description{% #description %}

The root container filesystem should be mounted as read-only. This rule checks both `containers` and `initContainers` and expects `securityContext.readOnlyRootFilesystem` to be set to `true` for each container. It reports `IncorrectValue` when the field is present and `false`, and `MissingAttribute` when the field is undefined.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: goproxy
  labels:
    app: goproxy
spec:
  containers:
  - name: goproxy
    image: k8s.gcr.io/goproxy:0.1
    securityContext:
      readOnlyRootFilesystem: true
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rootfalse
  labels:
    app: goproxy
spec:
  containers:
  - name: contain1_1
    image: k8s.gcr.io/goproxy:0.1
    securityContext:
      readOnlyRootFilesystem: false
---
apiVersion: v1
kind: Pod
metadata:
  name: noroot
  labels:
    app: goproxy
spec:
  containers:
  - name: contain1_2
    image: k8s.gcr.io/goproxy:0.1
    securityContext:
      someotherthing: true
```
