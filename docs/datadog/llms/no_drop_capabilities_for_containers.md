# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/no_drop_capabilities_for_containers.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/no_drop_capabilities_for_containers.md

---
title: Containers missing drop capabilities
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Containers missing drop capabilities
---

# Containers missing drop capabilities

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `268ca686-7fb7-4ae9-b129-955a2a89064e`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

### Description{% #description %}

Containers and initContainers should configure drop capabilities in their `securityContext`. The rule requires that each container defines `securityContext.capabilities` with a `drop` attribute; missing `securityContext`, `capabilities`, or `drop` is reported. This enforces least-privilege by removing unnecessary Linux capabilities.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: extensions/v1beta1
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
      - name: payment
        image: nginx
        securityContext:
          capabilities:
            drop:
              - all
            add:
              - NET_BIND_SERVICE
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: extensions/v1beta1
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
      - name: payment
        image: nginx
        securityContext:
          capabilities:
            add:
              - NET_BIND_SERVICE
      - name: payment2
        image: nginx
        securityContext:
          allowPrivilegeEscalation: false
      - name: payment3
        image: nginx
```
