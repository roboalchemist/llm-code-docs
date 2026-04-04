# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/container_is_privileged.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/container_is_privileged.md

---
title: Container is privileged
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Container is privileged
---

# Container is privileged

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dd29336b-fe57-445b-a26e-e6aa867ae609`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/workloads/pods/#privileged-mode-for-containers)

### Description{% #description %}

Privileged containers lack essential security restrictions and should be avoided. The `privileged` flag should be removed or set to `false` to prevent containers from gaining host-level privileges that bypass kernel security controls. This rule checks both `containers` and `initContainers` and flags any container where `securityContext.privileged` is true.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo-4
spec:
  containers:
  - name: sec-ctx-4
    image: gcr.io/google-samples/node-hello:1.0
    securityContext:
      privileged: false
      capabilities:
        add: ["NET_ADMIN", "SYS_TIME"]
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-deployment
  labels:
    app: test
spec:
  replicas: 3
  selector:
    matchLabels:
      app: test
  template:
    metadata:
      labels:
        app: test
    spec:
      containers:
        - name:  pause
          image: k8s.gcr.io/pause
          securityContext:
            privileged: true
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo-4
spec:
  containers:
  - name: sec-ctx-4
    image: gcr.io/google-samples/node-hello:1.0
    securityContext:
      privileged: true
      capabilities:
        add: ["NET_ADMIN", "SYS_TIME"]
---
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo-5
spec:
  initContainers:
  - name: sec-ctx-4
    image: gcr.io/google-samples/node-hello:1.0
    securityContext:
      privileged: true
      capabilities:
        add: ["NET_ADMIN", "SYS_TIME"]
  containers:
  - name: sec-ctx-4
    image: gcr.io/google-samples/node-hello:1.0
```
