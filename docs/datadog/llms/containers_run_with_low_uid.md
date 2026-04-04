# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/containers_run_with_low_uid.md

---
title: Container with low UID
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Container with low UID
---

# Container with low UID

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `02323c00-cdc3-4fdc-a310-4f2b3e7a1660`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

### Description{% #description %}

Containers should not run with a UID below 10000, as this may cause conflicts with the host's user table. A container can inherit runAsUser from the pod; both pod- and container-level runAsUser are evaluated. This rule flags containers whose runAsUser is undefined or set to a UID less than 10000.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo-2
spec:
  securityContext:
    runAsUser: 10000
  containers:
    - name: sec-ctx-demo-2
      image: gcr.io/google-samples/node-hello:1.0
      securityContext:
        runAsUser: 10100
        allowPrivilegeEscalation: false
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: securitydemo
  labels:
    app: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      securityContext:
        runAsUser: 65532
      containers:
        - name: frontend
          image: nginx
          ports:
            - containerPort: 80
          securityContext:
            readOnlyRootFilesystem: true
        - name: echoserver
          image: k8s.gcr.io/echoserver:1.4
          ports:
            - containerPort: 8080
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: securitydemo
  labels:
    app: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      securityContext:
        runAsUser: 19000
      containers:
        - name: frontend
          image: nginx
          ports:
            - containerPort: 80
          securityContext:
            runAsUser: 12000
            readOnlyRootFilesystem: true
        - name: echoserver
          image: k8s.gcr.io/echoserver:1.4
          ports:
            - containerPort: 8080
          securityContext:
            readOnlyRootFilesystem: true
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo-2
spec:
  securityContext:
    runAsUser: 10
    runAsNonRoot: false
  containers:
    - name: sec-ctx-demo-100
      image: gcr.io/google-samples/node-hello:1.0
      securityContext:
        runAsUser: 333
        runAsNonRoot: false
    - name: sec-ctx-demo-200
      image: gcr.io/google-samples/node-hedwfwllo:1.0
      securityContext:
        runAsUser: 340
        runAsNonRoot: false
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: containers-runs-as-root
spec:
  securityContext:
    runAsNonRoot: false
  containers:
    - name: sec-ctx-demo-100
      image: gcr.io/google-samples/node-hello:1.0
      securityContext:
        runAsUser: 13
        runAsNonRoot: false
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: securitydemo
  labels:
    app: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      securityContext:
        runAsUser: 1200
      containers:
        - name: frontend
          image: nginx
          ports:
            - containerPort: 80
          securityContext:
            readOnlyRootFilesystem: true
        - name: echoserver
          image: k8s.gcr.io/echoserver:1.4
          ports:
            - containerPort: 8080
          securityContext:
            readOnlyRootFilesystem: true
```
