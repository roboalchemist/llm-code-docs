# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/invalid_image.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/invalid_image.md

---
title: Invalid image tag
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Invalid image tag
---

# Invalid image tag

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `583053b7-e632-46f0-b989-f81ff8045385`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Supply-Chain

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/concepts/containers/images/#updating-images)

### Description{% #description %}

The image tag must be provided and must not be empty or `latest`. Image digests (using `@`, e.g., `image@sha256:...`) are preferred and will satisfy this rule. Omitting a tag or using the `latest` tag is considered invalid.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-image-test-1
spec:
  containers:
    - name: uses-private-image
      image: nginx:1.21
      imagePullPolicy: Always
      command: [ "echo", "SUCCESS" ]
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-image-test-3
spec:
  containers:
    - name: uses-private-image-container
      image: nginx
      imagePullPolicy: Always
      command: [ "echo", "SUCCESS" ]
---
apiVersion: v1
kind: Pod
metadata:
  name: private-image-test-33
spec:
  containers:
    - name: uses-private-image-container
      image: nginx:latest
      imagePullPolicy: Always
      command: [ "echo", "SUCCESS" ]
```
