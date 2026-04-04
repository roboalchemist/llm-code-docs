# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/permissive_access_to_create_pods.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/permissive_access_to_create_pods.md

---
title: Permissive access to create Pods
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Permissive access to create Pods
---

# Permissive access to create Pods

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `592ad21d-ad9b-46c6-8d2d-fad09d62a942`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#privilege-escalation-prevention-and-bootstrapping)

### Description{% #description %}

The permission to create Pods in a cluster should be restricted because it can allow privilege escalation. This rule detects Role and ClusterRole rules where verbs include "create" for the "pods" resource, or where verbs or resources use wildcard values together with non-custom API groups (empty string or "*"). When triggered, the rule reports the document, resource, and rule location containing the unsafe verb/resource combination.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
- apiGroups: [""]

  resources: ["pods"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader2
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "watch", "create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader4
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs:
    - "get"
    - "watch"
```

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
  - apiGroups:
      - apiextensions.k8s.io
    resources:
      - "*"
    verbs:
      - create
      - delete
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
#this is a problematic code where the query should report a result(s)
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
  - apiGroups:
      - "*"
    resources:
      - "*"
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - apiextensions.k8s.io
    resources:
      - custom
    verbs:
      - create
      - delete
  - apiGroups:
      - "*"
    resources:
      - "*"
    verbs:
      - create
      - delete
      - get
      - list
      - patch
      - update
      - watch
```

```yaml
#this is a problematic code where the query should report a result(s)
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs:
    - "get"
    - "watch"
    - create
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: secret-reader2
rules:
- apiGroups: [""]
  resources: ["*"]
  verbs: ["get", "watch", "create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader3
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "*"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: secret-reader4
rules:
- apiGroups: [""]
  resources: ["*"]
  verbs: ["get", "watch", "*"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader5
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs:
    - "get"
    - "watch"
    - "c*e"
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader6
rules:
- apiGroups: [""]
  resources: ["p*ds"]
  verbs: ["get", "watch", "create"]
```
