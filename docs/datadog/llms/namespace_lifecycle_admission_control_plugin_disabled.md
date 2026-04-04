# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/namespace_lifecycle_admission_control_plugin_disabled.md

---
title: Namespace lifecycle admission control plugin disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Namespace lifecycle admission control plugin
  disabled
---

# Namespace lifecycle admission control plugin disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1ffe7bf7-563b-4b3d-a71d-ba6bd8d49b37`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Build Process

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)

### Description{% #description %}

When running `kube-apiserver`, the `--disable-admission-plugins` flag should not include the `NamespaceLifecycle` plugin. Disabling the `NamespaceLifecycle` admission plugin can bypass namespace lifecycle checks and may lead to orphaned resources or unexpected behavior across namespaces. This rule identifies `kube-apiserver` containers and flags any `--disable-admission-plugins` setting that contains `NamespaceLifecycle`.

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
      image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
      command: ["kube-apiserver"]
      args: ["--enable-admission-plugins=NamespaceLifecycle", "--admission-control-config-file=path/to/plugin/config/file.yaml"]
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
      image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
      command: ["kube-apiserver"]
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
      image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
      command: ["kube-apiserver","--disable-admission-plugins=NamespaceLifecycle"]
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
      image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
      command: ["kube-apiserver"]
      args: ["--disable-admission-plugins=NamespaceLifecycle"]
  restartPolicy: OnFailure
```
