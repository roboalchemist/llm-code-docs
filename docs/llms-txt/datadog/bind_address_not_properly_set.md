# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/bind_address_not_properly_set.md

---
title: Bind address not properly set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Bind address not properly set
---

# Bind address not properly set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `46a2e9ec-6a5f-4faa-9d39-4ea44d5d87a2`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)

### Description{% #description %}

When running `kube-controller-manager` or `kube-scheduler`, the `--bind-address` flag must be set to `127.0.0.1`. The rule inspects command arguments in both `containers` and `initContainers` and reports a finding if the `--bind-address=127.0.0.1` flag is missing or set to a different value.

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
      args: ["--bind-address=127.0.0.1"]
  restartPolicy: OnFailure
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: kube-scheduler
    tier: control-plane
  name: kube-scheduler
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: kube-controller-manager
  template:
    metadata:
      labels:
        app: kube-controller-manager
  containers:
    - name: command-demo-container
      image: k8s.gcr.io/kube-scheduler:v1.19.0
      command: ["kube-scheduler","--bind-address=127.0.0.1"]
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
      image: gcr.io/google_containers/kube-controller-manager-amd64:v1.6.0
      command: ["kube-controller-manager","--bind-address=127.0.0.1"]
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
      args: []
  restartPolicy: OnFailure
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: kube-scheduler
    tier: control-plane
  name: kube-scheduler
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: kube-controller-manager
  template:
    metadata:
      labels:
        app: kube-controller-manager
  containers:
    - name: command-demo-container
      image: k8s.gcr.io/kube-scheduler:v1.19.0
      command: ["kube-scheduler"]
      args: []
  restartPolicy: OnFailure
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: kube-scheduler
    tier: control-plane
  name: kube-scheduler
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: kube-controller-manager
  template:
    metadata:
      labels:
        app: kube-controller-manager
  containers:
    - name: command-demo-container
      image: k8s.gcr.io/kube-scheduler:v1.19.0
      command: ["kube-scheduler","--bind-address=0.0.0.0"]
      args: []
  restartPolicy: OnFailure
```
