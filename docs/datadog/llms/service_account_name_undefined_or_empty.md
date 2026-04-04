# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/service_account_name_undefined_or_empty.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/service_account_name_undefined_or_empty.md

---
title: Service account name undefined or empty
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Service account name undefined or empty
---

# Service account name undefined or empty

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `591ade62-d6b0-4580-b1ae-209f80ba1cd9`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Insecure Defaults

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

### Description{% #description %}

A Kubernetes Pod should have a service account defined to restrict Kubernetes API access. The `serviceAccountName` attribute should be present in the Pod spec and not be empty. Pods missing this attribute or having an empty value are reported by the rule.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    volumeMounts:
    - mountPath: /var/run/secrets/tokens
      name: vault-token
  serviceAccountName: build-robot
  volumes:
  - name: vault-token
    projected:
      sources:
      - serviceAccountToken:
          path: vault-token
          expirationSeconds: 7200
          audience: vault
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
#this is a problematic code where the query should report a result(s)
apiVersion: v1
kind: Pod
metadata:
  name: nginx.container
spec:
  containers:
  - image: nginx
    name: nginx
    volumeMounts:
    - mountPath: /var/run/secrets/tokens
      name: vault-token
  volumes:
  - name: vault-token
    projected:
      sources:
      - serviceAccountToken:
          path: vault-token
          expirationSeconds: 7200
          audience: vault

---

apiVersion: v1
kind: Pod
metadata:
  name: nginx2.container.group
spec:
  containers:
  - image: nginx2
    name: nginx2
    volumeMounts:
    - mountPath: /var/run/secrets/tokens
      name: vault-token
  serviceAccountName:
  volumes:
  - name: vault-token
    projected:
      sources:
      - serviceAccountToken:
          path: vault-token
          expirationSeconds: 7200
          audience: vault

---

apiVersion: v1
kind: Pod
metadata:
  name: nginx3
spec:
  containers:
  - image: nginx3
    name: nginx3
    volumeMounts:
    - mountPath: /var/run/secrets/tokens
      name: vault-token
  serviceAccountName: ""
  volumes:
  - name: vault-token
    projected:
      sources:
      - serviceAccountToken:
          path: vault-token
          expirationSeconds: 7200
          audience: vault
```
