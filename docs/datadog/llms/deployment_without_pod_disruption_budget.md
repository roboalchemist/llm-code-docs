# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/deployment_without_pod_disruption_budget.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/deployment_without_pod_disruption_budget.md

---
title: Deployment without PodDisruptionBudget
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Deployment without PodDisruptionBudget
---

# Deployment without PodDisruptionBudget

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b23e9b98-0cb6-4fc9-b257-1f3270442678`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Availability

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)

### Description{% #description %}

Deployments with more than one replica should be targeted by a PodDisruptionBudget to ensure high availability during voluntary disruptions. This rule flags Deployment resources that have replicas > 1 but are not selected by any PodDisruptionBudget. A PodDisruptionBudget helps maintain the desired number of available pods during node drains or other disruptions.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: nginx-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: nginx32
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx32
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: nginx-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: xpto
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```
