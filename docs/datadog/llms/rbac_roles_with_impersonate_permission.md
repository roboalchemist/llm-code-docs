# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/rbac_roles_with_impersonate_permission.md

---
title: RBAC roles with impersonate permission
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RBAC roles with impersonate permission
---

# RBAC roles with impersonate permission

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9f85c3f6-26fd-4007-938a-2e0cb0100980`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation)

### Description{% #description %}

Roles or ClusterRoles with the `impersonate` permission allow subjects to assume the rights of other users, groups, or service accounts. If an identity with such permissions is compromised, attackers can abuse this sudo-like capability to escalate privileges and act with the impersonated principals' access. Misuse of the `impersonate` permission can enable lateral movement, persistent access, and the bypass of intended permission boundaries. For these reasons, `impersonate` is considered a high-risk permission and is commonly subject to restriction and monitoring.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: impersonator-role-neg
  namespace: default
rules:
- apiGroups: [""]
  resources: ["users", "groups", "serviceaccounts"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: rbac-impersonate-binding
subjects:
- kind: ServiceAccount
  name: impersonator-sa-neg
  namespace: default
  apiGroup: ""
roleRef:
  kind: ClusterRole
  name: impersonator-role-neg
  apiGroup: ""
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: impersonator-role
  namespace: default
rules:
- apiGroups: [""]
  resources: ["users", "groups", "serviceaccounts"]
  verbs: ["impersonate"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: rbac-impersonate-binding
subjects:
- kind: ServiceAccount
  name: impersonator-sa
  namespace: default
  apiGroup: ""
roleRef:
  kind: ClusterRole
  name: impersonator-role
  apiGroup: ""
```
