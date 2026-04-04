# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/audit_log_maxsize_not_properly_set.md

---
title: Audit log maxsize not properly set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Audit log maxsize not properly set
---

# Audit log maxsize not properly set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `35c0a471-f7c8-4993-aa2c-503a3c712a66`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)

### Description{% #description %}

When a container runs `kube-apiserver`, the `--audit-log-maxsize` flag should be set to 100 megabytes or more.This rule inspects `containers` and `initContainers` and checks container commands for `kube-apiserver`; it verifies that `--audit-log-maxsize` is present and has a value of at least 100 megabytes.The rule reports `MissingAttribute` if the flag is absent and `IncorrectValue` if the flag is set to less than 100 megabytes.

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
      args: ["--audit-log-maxsize=150"]
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
      command: ["kube-apiserver","--audit-log-maxsize=100"]
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
      args: []
  restartPolicy: OnFailure
```

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: dummy
  namespace: knative-sequence
spec:
  template:
    spec:
      containers:
      - name: command-demo-container
        image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
        command: ["kube-apiserver"]
        args: ["--audit-log-maxsize=50"]
    restartPolicy: OnFailure
---
apiVersion: serving.knative.dev/v1
kind: Configuration
metadata:
  name: dummy-config
  namespace: knative-sequence
spec:
  template:
    spec:
      containers:
        - name: command-demo-container
          image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
          command: ["kube-apiserver"]
          args: ["--audit-log-maxsize=50"]
      restartPolicy: OnFailure
---
apiVersion: serving.knative.dev/v1
kind: Revision
metadata:
  name: dummy-rev
  namespace: knative-sequence
spec:
  containers:
    - name: command-demo-container
      image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
      command: ["kube-apiserver"]
      args: ["--audit-log-maxsize=50"]
  restartPolicy: OnFailure
---
apiVersion: sources.knative.dev/v1
kind: ContainerSource
metadata:
  name: dummy-cs
  namespace: knative-sequence
spec:
  template:
    spec:
      containers:
        - name: command-demo-container
          image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0
          command: ["kube-apiserver"]
          args: ["--audit-log-maxsize=50"]
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
      args: ["--audit-log-maxsize=50"]
  restartPolicy: OnFailure
```
