# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/tiller_service_is_not_deleted.md

---
title: Tiller Service present
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Tiller Service present
---

# Tiller Service present

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8b862ca9-0fbd-4959-ad72-b6609bdaa22d`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/services-networking/service)

### Description{% #description %}

Tiller services should be removed because Helm v2 is deprecated and no longer supported. This rule flags resources that reference 'tiller' in their metadata.name, in values of metadata.labels, or in values under spec.selector. These references should be removed or replaced to ensure compatibility with Helm v3.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: some-service
  labels:
    name: some-label
spec:
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: tiller-deploy
  labels:
    app: helm
    name: tiller
spec:
  type: ClusterIP
  selector:
    app: helm
    name: tiller
  ports:
  - name: tiller
    port: 44134
    protocol: TCP
    targetPort: tiller
```
