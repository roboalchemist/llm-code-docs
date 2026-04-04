# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/shared_service_account.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/shared_service_account.md

---
title: Shared service account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Shared service account
---

# Shared service account

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c1032cf7-3628-44e2-bd53-38c17cf31b6b`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

### Description{% #description %}

A service account token is shared between workloads. The rule detects multiple workload manifests that reference the same `serviceAccountName` in their spec. Sharing a service account increases the blast radius and can violate least-privilege principles by causing credentials and permissions to be shared across workloads.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod1
spec:
  serviceAccountName : service1
  containers:
  - name: mycontainer
    image: redis
---
apiVersion: v1
kind: Pod
metadata:
  name: pod2
spec:
  serviceAccountName : service2
  containers:
  - name: envars-test-container
    image: nginx
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod1
spec:
  serviceAccountName : service1
  containers:
  - name: mycontainer
    image: redis
---
apiVersion: v1
kind: Pod
metadata:
  name: pod2
spec:
  serviceAccountName : service1
  containers:
  - name: envars-test-container
    image: nginx
```
