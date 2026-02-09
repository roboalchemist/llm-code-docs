# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/ensure_administrative_boundaries_between_resources.md

---
title: Ensure administrative boundaries between resources
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Ensure administrative boundaries between
  resources
---

# Ensure administrative boundaries between resources

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e84eaf4d-2f45-47b2-abe8-e581b06deb66`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

### Description{% #description %}

As a best practice, ensure namespaces are used correctly to group and administer resources. Kubernetes authorization mechanisms, such as RBAC, can enforce policies that segregate or restrict user access to namespaces. This rule scans cluster manifests for resources that specify a namespace and aggregates the namespaces in use, reporting them for review. Review the reported namespaces to confirm they are required, appropriately configured, and governed by suitable access controls (for example, RoleBindings, NetworkPolicies, or admission controllers).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
  namespace: cosmic-namespace
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    securityContext:
      allowPrivilegeEscalation: false
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"

  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    securityContext:
      allowPrivilegeEscalation: false
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
---
apiVersion: v1
kind: Pod
metadata:
  name: frontend2
  namespace: cosmic-namespace
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    securityContext:
      allowPrivilegeEscalation: false
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"

  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    securityContext:
      allowPrivilegeEscalation: false
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```
