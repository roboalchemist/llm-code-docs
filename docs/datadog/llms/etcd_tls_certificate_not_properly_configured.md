# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/etcd_tls_certificate_not_properly_configured.md

---
title: etcd TLS certificate not properly configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > etcd TLS certificate not properly configured
---

# etcd TLS certificate not properly configured

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `895a5a95-3756-4b04-9924-2f3bc93181bd`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)

### Description{% #description %}

When using `kube-apiserver`, the `--etcd-certfile` and `--etcd-keyfile` flags should be set. The rule checks `containers` and `initContainers` for containers whose command includes `kube-apiserver` and reports a MissingAttribute issue when either flag is not defined.

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
      args: ["--etcd-keyfile=/path/to/key/file.key","--etcd-certfile=/path/to/cert/file.crt"]
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
      command: ["kube-apiserver","--etcd-keyfile=/path/to/key/file.key","--etcd-certfile=/path/to/cert/file.crt"]
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
      command: ["kube-apiserver"]
      args: ["--etcd-certfile=/path/to/cert/file.crt"]
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
      args: ["--etcd-keyfile=/path/to/key/file.key"]
  restartPolicy: OnFailure
```
