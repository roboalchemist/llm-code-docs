# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/statefulset_without_pod_disruption_budget.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/statefulset_without_pod_disruption_budget.md

---
title: StatefulSet without PodDisruptionBudget
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > StatefulSet without PodDisruptionBudget
---

# StatefulSet without PodDisruptionBudget

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1db3a5a5-bf75-44e5-9e44-c56cfc8b1ac5`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Availability

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)

### Description{% #description %}

StatefulSets with more than one replica should have a PodDisruptionBudget that targets the StatefulSet's pod selector (`spec.selector.matchLabels`) to ensure high availability.This prevents simultaneous voluntary evictions from reducing the number of available replicas and helps maintain service continuity.The rule flags StatefulSets where no PodDisruptionBudget matches the StatefulSet's selector.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: nginx-pdb
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      app: nginx33
      run: test
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx123
      run: test
  serviceName: "nginx"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: k8s.gcr.io/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: nginx-pdb
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      app: xpto
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  requiredDropCapabilities:
    - ALL
  selector:
    matchLabels:
      app: nginx
  serviceName: "nginx"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: k8s.gcr.io/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
```
