# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/audit_log_maxage_not_properly_set.md

---
title: Audit log maxage not properly set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Audit log maxage not properly set
---

# Audit log maxage not properly set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `da9f3aa8-fbfb-472f-b5a1-576127944218`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)

### Description{% #description %}

When a container runs `kube-apiserver`, the `--audit-log-maxage` flag should be set to 30 days or more. This rule flags containers (including `initContainers`) where the flag is missing or set to a value less than 30. It reports the resource and the command location when the flag is absent or incorrectly configured.

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
      args: ["--audit-log-maxage=30"]
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
      command: ["kube-apiserver","--audit-log-maxage=35"]
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
          args: []
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
          args: []
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
      args: []
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
      args: ["--audit-log-maxage=26"]
  restartPolicy: OnFailure
```
