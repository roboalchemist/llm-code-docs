# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/kubelet_hostname_override_is_set.md

---
title: Kubelet hostname override is set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Kubelet hostname override is set
---

# Kubelet hostname override is set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `bf36b900-b5ef-4828-adb7-70eb543b7cfb`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)

### Description{% #description %}

Hostnames should not be overridden. This rule detects containers (including `initContainers`) whose command invokes `kubelet` and includes the `--hostname-override=` flag. Overriding the node hostname can create duplicate or incorrect hostnames and may disrupt node identity and cluster operations.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
  labels:
    purpose: demonstrate-command
spec:
  containers:
    - name: command-demo-container
      image: foo/bar
      command: ["kubelet"]
      args: []
  restartPolicy: OnFailure
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
  labels:
    purpose: demonstrate-command
spec:
  containers:
    - name: command-demo-container
      image: foo/bar
      command: ["kubelet","--hostname-override=host"]
      args: []
  restartPolicy: OnFailure
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
  labels:
    purpose: demonstrate-command
spec:
  containers:
    - name: command-demo-container
      image: foo/bar
      command: ["kubelet"]
      args: ["--hostname-override=host"]
  restartPolicy: OnFailure
```
