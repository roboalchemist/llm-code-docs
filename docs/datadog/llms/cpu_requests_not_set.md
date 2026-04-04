# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/cpu_requests_not_set.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/cpu_requests_not_set.md

---
title: CPU requests not set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CPU requests not set
---

# CPU requests not set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ca469dd4-c736-448f-8ac1-30a642705e0a`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Resource Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#)

### Description{% #description %}

CPU requests should be set to ensure the total resource requests of scheduled containers are less than the node's capacity. This rule checks both `initContainers` and `containers` for the presence of a `resources` field, a `resources.requests` map, and a `cpu` entry within `requests`. It reports a MissingAttribute issue when any container is missing `resources`, missing `requests`, or missing CPU requests to help enforce proper schedulability and capacity planning.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
    - name: app
      image: images.my-company.example/app:v4
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
    - name: log-aggregator
      image: images.my-company.example/log-aggregator:v6
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
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
        - name: app
          image: images.my-company.example/app:v4
          resources:
            requests:
              memory: "64Mi"
              cpu: "250m"
            limits:
              memory: "128Mi"
              cpu: "500m"
        - name: log-aggregator
          image: images.my-company.example/log-aggregator:v6
          resources:
            requests:
              memory: "64Mi"
              cpu: "250m"
            limits:
              memory: "128Mi"
              cpu: "500m"
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
    - name: app
      image: images.my-company.example/app:v4
      resources:
        requests:
          memory: "64Mi"
        limits:
          memory: "128Mi"
          cpu: "500m"
    - name: log-aggregator
      image: images.my-company.example/log-aggregator:v6
      resources:
        limits:
          memory: "128Mi"
          cpu: "500m"
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
        - name: app
          image: images.my-company.example/app:v4
          resources:
            requests:
              memory: "64Mi"
            limits:
              memory: "128Mi"
              cpu: "500m"
        - name: log-aggregator
          image: images.my-company.example/log-aggregator:v6
          resources:
            limits:
              memory: "128Mi"
              cpu: "500m"
```
