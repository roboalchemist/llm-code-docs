# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/auto_tls_set_to_true.md

---
title: Auto TLS set to true
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Auto TLS set to true
---

# Auto TLS set to true

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `98ce8b81-7707-4734-aa39-627c6db3d84b`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://etcd.io/docs/v3.4/op-guide/security/)

### Description{% #description %}

When a container runs `etcd`, the `--auto-tls` flag should be set to `false` or omitted. Enabling `--auto-tls=true` enables automatic certificate management and can introduce security risks. This rule checks `containers` and `initContainers` for commands that invoke `etcd` and reports when `--auto-tls` is present and set to `true`.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-etcd-deployment
spec:
  selector:
    matchLabels:
      app: app
  replicas: 1
  template:
    metadata:
      labels:
        app: app
        version: v1
    spec:
      serviceAccountName: database
      containers:
      - name: database
        image: gcr.io/google_containers/etcd:v3.2.18
        imagePullPolicy: IfNotPresent
        command: ["etcd"]
        args: []
      nodeSelector:
        kubernetes.io/hostname: worker02
    restartPolicy: OnFailure
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-etcd-deployment
spec:
  selector:
    matchLabels:
      app: app
  replicas: 1
  template:
    metadata:
      labels:
        app: app
        version: v1
    spec:
      serviceAccountName: database
      containers:
      - name: database
        image: gcr.io/google_containers/etcd:v3.2.18
        imagePullPolicy: IfNotPresent
        command: ["etcd", "--auto-tls=false"]
        args: []
      nodeSelector:
        kubernetes.io/hostname: worker02
    restartPolicy: OnFailure
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-etcd-deployment
spec:
  selector:
    matchLabels:
      app: app
  replicas: 1
  template:
    metadata:
      labels:
        app: app
        version: v1
    spec:
      serviceAccountName: database
      containers:
      - name: database
        image: gcr.io/google_containers/etcd:v3.2.18
        imagePullPolicy: IfNotPresent
        command: ["etcd"]
        args: ["--auto-tls=true"]
      nodeSelector:
        kubernetes.io/hostname: worker02
    restartPolicy: OnFailure
```
