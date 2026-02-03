# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/kubelet_read_only_port_is_not_set_to_zero.md

---
title: Kubelet read-only port is not set to zero
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Kubelet read-only port is not set to zero
---

# Kubelet read-only port is not set to zero

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2940d48a-dc5e-4178-a3f8-bfbd80720b41`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/)

### Description{% #description %}

When running `kubelet`, the read-only port should be set to `0` by specifying `--read-only-port=0`. This rule detects containers that invoke `kubelet` with a `--read-only-port` flag not set to `0`, and `KubeletConfiguration` resources whose `readOnlyPort` attribute is not `0`. Disabling the read-only port prevents exposure of the unauthenticated read-only HTTP endpoint.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kubelet-demo
  labels:
    purpose: kubelet-demo
spec:
  containers:
    - name: kubelet-demo-container
      image: foo/bar
      command: ["kubelet"]
      args: ["--read-only-port=0"]
  restartPolicy: OnFailure
```

```json
{
    "kind": "KubeletConfiguration",
    "apiVersion": "kubelet.config.k8s.io/v1beta1",
    "address": "192.168.0.8"
  }
```

```json
{
    "kind": "KubeletConfiguration",
    "apiVersion": "kubelet.config.k8s.io/v1beta1",
    "address": "192.168.0.8",
    "readOnlyPort": 0
  }
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
      command: ["kubelet", "--read-only-port=1"]
  restartPolicy: OnFailure
```

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
address: "192.168.0.8"
port: 20250
serializeImagePulls: false
evictionHard:
  memory.available: "200Mi"
readOnlyPort: 1
```

```json
{
    "kind": "KubeletConfiguration",
    "apiVersion": "kubelet.config.k8s.io/v1beta1",
    "address": "192.168.0.8",
    "readOnlyPort": 1
  }
```
