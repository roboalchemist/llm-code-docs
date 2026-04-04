# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/etcd_tls_certificate_files_not_properly_set.md

---
title: etcd TLS certificate files not properly set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > etcd TLS certificate files not properly set
---

# etcd TLS certificate files not properly set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `075ca296-6768-4322-aea2-ba5063b969a9`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://etcd.io/docs/v3.4/op-guide/security/)

### Description{% #description %}

For containers and initContainers that run `etcd`, the `--cert-file` and `--key-file` flags must be set. This rule reports resources whose container command includes `etcd` but where one or both flags are missing from the container command.

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
        args: ["--cert-file=/etc/env/file.crt", "--key-file=/etc/env/file2.key"]
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
        command: ["etcd", "--cert-file=/etc/env/file.crt", "--key-file=/etc/env/file2.key"]
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
        args: ["--key-file=/etc/env/file2.key"]
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
        command: ["etcd"]
        args: ["--cert-file=/etc/env/file.crt"]
      nodeSelector:
        kubernetes.io/hostname: worker02
    restartPolicy: OnFailure
```
