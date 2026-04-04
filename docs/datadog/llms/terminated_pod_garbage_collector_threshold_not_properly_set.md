# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/terminated_pod_garbage_collector_threshold_not_properly_set.md

---
title: Terminated pod garbage collector threshold not properly set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Terminated pod garbage collector threshold not
  properly set
---

# Terminated pod garbage collector threshold not properly set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `49113af4-29ca-458e-b8d4-724c01a4a24f`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Availability

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)

### Description{% #description %}

For containers running `kube-controller-manager`, the `--terminated-pod-gc-threshold` flag must be set to a value between `0` and `12501`. The rule checks the `command` fields in both `initContainers` and `containers` and reports when the flag is missing or set to an incorrect value.

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
      image: gcr.io/google_containers/kube-controller-manager-amd64:v1.6.0
      command: ["kube-controller-manager"]
      args: ["--terminated-pod-gc-threshold=10"]
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
      image: gcr.io/google_containers/kube-controller-manager-amd64:v1.6.0
      command: ["kube-controller-manager","--terminated-pod-gc-threshold=10"]
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
      image: gcr.io/google_containers/kube-controller-manager-amd64:v1.6.0
      command: ["kube-controller-manager"]
      args: ["--terminated-pod-gc-threshold=12501"]
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
      image: gcr.io/google_containers/kube-controller-manager-amd64:v1.6.0
      command: ["kube-controller-manager","--terminated-pod-gc-threshold=0"]
      args: []
  restartPolicy: OnFailure
```
