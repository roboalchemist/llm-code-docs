# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/etcd_peer_tls_certificate_files_not_properly_set.md

---
title: etcd peer TLS certificate files not properly set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > etcd peer TLS certificate files not properly
  set
---

# etcd peer TLS certificate files not properly set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `09bb9e96-8da3-4736-b89a-b36814acca60`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://etcd.io/docs/v3.4/op-guide/security/)

### Description{% #description %}

When a container command includes `etcd`, the `--peer-cert-file` and `--peer-key-file` flags should be set. The rule inspects both initContainers and containers and reports a MissingAttribute when any required flag is not present in the container's command. The result identifies the resource and the command position where the missing flag was detected.

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
        args: ["--peer-cert-file=/etc/env/file.crt", "--peer-key-file=/etc/env/file2.key"]
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
        command: ["etcd", "--peer-cert-file=/etc/env/file.crt", "--peer-key-file=/etc/env/file2.key"]
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
        args: ["--peer-key-file=/etc/env/file2.key"]
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
        args: ["--peer-cert-file=/etc/env/file.crt"]
      nodeSelector:
        kubernetes.io/hostname: worker02  
    restartPolicy: OnFailure
```
