# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/tiller_deployment_is_accessible_from_within_the_cluster.md

---
title: Tiller Deployment accessible within cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Tiller Deployment accessible within cluster
---

# Tiller Deployment accessible within cluster

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e17fa86a-6222-4584-a914-56e8f6c87e06`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/containers/images/)

### Description{% #description %}

Tiller deployments must not allow access from within the cluster.Tiller containers must include the `--listen` argument and set it to a local address (for example `localhost` or `127.0.0.1`).Resources lacking `args` or whose `--listen` value is not a local address are flagged.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tiller-deploy
  labels:
    app: helm
    name: tiller
spec:
  selector:
    matchLabels:
      app: helm
      name: tiller
  template:
    metadata:
      labels:
        app: helm
        name: tiller
    spec:
      serviceAccountName: tiller
      containers:
        - name: tiller
          image: "tiller-image"
          args: ["--listen=127.0.0.1:44134"]
          ports:
          - containerPort: 44134
            name: tiller
            protocol: TCP
          - containerPort: 44135
            name: http
            protocol: TCP
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: helm
    name: tiller
  name: tiller-bad-args
spec:
  selector:
    matchLabels:
      name: tiller
  template:
    metadata:
      labels:
        app: helm
        name: tiller
    spec:
      containers:
        -
          args:
            - "--listen=10.7.2.8:44134"
          image: tiller-image
          name: tiller-v2
          ports:
            -
              containerPort: 44134
              name: tiller
              protocol: TCP
            -
              containerPort: 44135
              name: http
              protocol: TCP
      serviceAccountName: tiller
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: helm
    name: tiller
  name: tiller-deploy-no-args
spec:
  selector:
    matchLabels:
      name: tiller
  template:
    metadata:
      labels:
        app: helm
        name: tiller
    spec:
      containers:
        -
          name: tiller-v2
          image: tiller-image
      serviceAccountName: tiller
```
