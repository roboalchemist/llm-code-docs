# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/rbac_roles_allow_privilege_escalation.md

---
title: RBAC roles allow privilege escalation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RBAC roles allow privilege escalation
---

# RBAC roles allow privilege escalation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8320826e-7a9c-4b0b-9535-578333193432`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#restrictions-on-role-binding-creation-or-update)

### Description{% #description %}

Roles or ClusterRoles that include `bind` or `escalate` permissions allow subjects to create new bindings with other roles. These permissions enable privilege escalation, because users with them can bind to roles that may exceed their own privileges and gain unauthorized elevated access. This rule flags Role and ClusterRole objects whose rules include `bind` or `escalate` for the `roles` or `clusterroles` resources.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: not-rbac-binder
rules:
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["clusterrolebindings"]
  verbs: ["create"]
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: rbac-binder
rules:
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["clusterroles"]
  verbs: ["bind"]
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["clusterrolebindings"]
  verbs: ["create"]
```
