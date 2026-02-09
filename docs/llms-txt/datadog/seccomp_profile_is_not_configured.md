# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/seccomp_profile_is_not_configured.md

---
title: Seccomp profile is not configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Seccomp profile is not configured
---

# Seccomp profile is not configured

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f377b83e-bd07-4f48-a591-60c82b14a78b`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tutorials/security/seccomp/#create-pod-that-uses-the-container-runtime-default-seccomp-profile)

### Description{% #description %}

Containers should be configured with a secure seccomp profile to restrict potentially dangerous syscalls. The container or pod field securityContext.seccompProfile.type should be set to 'RuntimeDefault' or 'Localhost'; pod-level settings apply to containers when defined. If the deprecated annotation seccomp.security.alpha.kubernetes.io/defaultProfileName is used, it should be 'runtime/default'; if neither fields nor annotation are present, the seccomp profile is considered missing.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-test-1
  annotations:
    seccomp.security.alpha.kubernetes.io/defaultProfileName:  'runtime/default'
spec:
  containers:
  - name: foobar
    image: foo/bar:latest
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
        seccompProfile:
            type: RuntimeDefault
      containers:
        - name: frontend
          image: nginx
          ports:
            - containerPort: 80
          securityContext:
            allowPrivilegeEscalation: false
        - name: echoserver
          image: k8s.gcr.io/echoserver:1.4
          ports:
            - containerPort: 8080
          securityContext:
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
        runAsUser: 19000
      containers:
        - name: frontend
          image: nginx
          ports:
            - containerPort: 80
          securityContext:
            allowPrivilegeEscalation: false
            seccompProfile:
                type: RuntimeDefault
        - name: echoserver
          image: k8s.gcr.io/echoserver:1.4
          ports:
            - containerPort: 8080
          securityContext:
            allowPrivilegeEscalation: false
            seccompProfile:
                type: RuntimeDefault
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

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
            allowPrivilegeEscalation: false
        - name: echoserver
          image: k8s.gcr.io/echoserver:1.4
          ports:
            - containerPort: 8080
          securityContext:
            allowPrivilegeEscalation: false
            seccompProfile:
                type: RuntimeDefault
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
            allowPrivilegeEscalation: false
        - name: echoserver
          image: k8s.gcr.io/echoserver:1.4
          ports:
            - containerPort: 8080
          securityContext:
            allowPrivilegeEscalation: false
            seccompProfile:
                type: Unconfined
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
        seccompProfile:
            type: RuntimeDefault
      containers:
        - name: frontend
          image: nginx
          ports:
            - containerPort: 80
          securityContext:
            allowPrivilegeEscalation: false
        - name: echoserver
          image: k8s.gcr.io/echoserver:1.4
          ports:
            - containerPort: 8080
          securityContext:
            allowPrivilegeEscalation: false
            seccompProfile:
                type: Unconfined
```
