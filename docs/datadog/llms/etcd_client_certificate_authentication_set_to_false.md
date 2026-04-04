# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/etcd_client_certificate_authentication_set_to_false.md

---
title: etcd client certificate authentication set to false
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > etcd client certificate authentication set to
  false
---

# etcd client certificate authentication set to false

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9391103a-d8d7-4671-ac5d-606ba7ccb0ac`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://etcd.io/docs/v3.4/op-guide/security/)

### Description{% #description %}

When containers run `etcd`, the `--client-cert-auth` flag must be set to `true`. This enforces client certificate authentication to prevent unauthenticated access to the etcd server. The rule reports `IncorrectValue` when the flag is explicitly set to `false`, and `MissingAttribute` when the flag is not defined.

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
        args: ["--client-cert-auth=true"]
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
        command: ["etcd"]
        args: ["--client-cert-auth=false"]
      nodeSelector:
        kubernetes.io/hostname: worker02
    restartPolicy: OnFailure
```
