# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/rbac_roles_with_read_secrets_permissions.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/rbac_roles_with_read_secrets_permissions.md

---
title: RBAC roles with read secrets permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RBAC roles with read secrets permissions
---

# RBAC roles with read secrets permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b7bca5c4-1dab-4c2c-8cbe-3050b9d59b14`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

### Description{% #description %}

Roles and ClusterRoles with `get`, `watch`, or `list` permissions on Kubernetes Secrets are dangerous and should be avoided. These permissions allow read access to Secrets objects across the scope of the Role or ClusterRole. In case of compromise, attackers could abuse these roles to access sensitive data such as passwords, tokens, and keys, increasing the blast radius. This policy flags Role and ClusterRole rules that grant the `get`, `watch`, or `list` verbs on the `secrets` resource.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: role-pod-and-logs-reader
rules:
- apiGroups: [""]
  resources: ["pods", "pods/logs"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-role-pod-and-pod-logs-reader
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list"]
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: role-secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-role-secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "watch", "list"]
```
