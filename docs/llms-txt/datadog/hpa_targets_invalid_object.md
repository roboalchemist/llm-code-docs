# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/hpa_targets_invalid_object.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/hpa_targets_invalid_object.md

---
title: HPA targets invalid object
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > HPA targets invalid object
---

# HPA targets invalid object

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2f652c42-619d-4361-b361-9f599688f8ca`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Availability

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)

### Description{% #description %}

The `HorizontalPodAutoscaler` must target a valid object. This rule verifies each entry in `spec.metrics` with `type: "Object"` includes the required fields: `object.metric`, `object.target`, and `object.describedObject` with `name`, `apiVersion`, and `kind`. If any of these fields are missing, the metric is considered invalid.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Object
    object:
      metric:
        name: requests-per-second
      describedObject:
        apiVersion: networking.k8s.io/v1beta1
        kind: Ingress
        name: main-route
      target:
        type: Value
        value: 10k
```

```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: matching-svc
  namespace: default
spec:
  metrics:
    - resource:
        name: cpu
        target:
          averageUtilization: 50
          type: Utilization
      type: Resource
  minReplicas: 1
  maxReplicas: 5
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: matching-svc
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Object
    object:
      metric:
        name: requests-per-second
      target:
        type: Value
        value: 10k
      describedObject:
        apiVersion: networking.k8s.io/v1beta1
        kind: Ingress
```
