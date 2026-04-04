# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/metadata_label_is_invalid.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/metadata_label_is_invalid.md

---
title: Invalid metadata label
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Invalid metadata label
---

# Invalid metadata label

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1123031a-f921-4c5b-bd86-ef354ecfd37a`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)

### Description{% #description %}

Metadata labels must be valid and conform to the pattern `^(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?$`. This requires label values to start and end with an alphanumeric character and may include dashes, underscores, or dots in the middle; labels that do not match this pattern are reported as `IncorrectValue` with the resource and label details.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: goproxy
  labels:
    app: goproxy
spec:
  containers:
  - name: goproxy
    image: k8s.gcr.io/goproxy:0.1
    ports:
    - containerPort: 8080
    readinessProbe:
      tcpSocket:
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 10
    livenessProbe:
      tcpSocket:
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 20
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: goproxy
  labels:
    app: g**dy.l+bel.
spec:
  containers:
  - name: goproxy
    image: k8s.gcr.io/goproxy:0.1
    ports:
    - containerPort: 8080
    livenessProbe:
      tcpSocket:
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 20
```
