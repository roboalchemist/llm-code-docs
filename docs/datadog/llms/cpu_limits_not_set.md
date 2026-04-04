# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/cpu_limits_not_set.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/cpu_limits_not_set.md

---
title: CPU limits not set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CPU limits not set
---

# CPU limits not set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4ac0e2b7-d2d2-4af7-8799-e8de6721ccda`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Resource Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

### Description{% #description %}

CPU limits should be set to ensure fair resource allocation and to prevent containers from consuming excessive CPU. Each container and initContainer should include a `resources.limits.cpu` value. This rule verifies that `resources`, `resources.limits`, and `resources.limits.cpu` are defined for each container.

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
      limits:
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
        limits:
          memory: "64Mi"
    - name: log-aggregator
      image: images.my-company.example/log-aggregator:v6
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
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
            limits:
              memory: "64Mi"
        - name: log-aggregator
          image: images.my-company.example/log-aggregator:v6
          resources:
            requests:
              memory: "64Mi"
              cpu: "250m"
```
