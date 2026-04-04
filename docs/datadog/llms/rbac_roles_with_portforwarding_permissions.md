# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/rbac_roles_with_portforwarding_permissions.md

---
title: RBAC roles with port-forwarding permission
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RBAC roles with port-forwarding permission
---

# RBAC roles with port-forwarding permission

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `38fa11ef-dbcc-4da8-9680-7e1fd855b6fb`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

### Description{% #description %}

Roles or ClusterRoles that grant permissions to port-forward into pods can open socket-level communication channels to containers. If compromised, attackers may abuse this capability to establish direct connections that bypass network security controls. This can enable data exfiltration, remote command execution, or persistent access to containerized workloads. Limiting port-forward permissions to trusted principals and enforcing least-privilege reduces this risk.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: my-namespace
  name: allow-port-forward-neg
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: allow-port-forward-neg
  namespace: my-namespace
subjects:
- kind: User
  name: bob
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: allow-port-forward-neg
  apiGroup: ""
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: my-namespace
  name: allow-port-forward
rules:
- apiGroups: [""]
  resources: ["pods", "pods/portforward"]
  verbs: ["get", "list", "create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: allow-port-forward
  namespace: my-namespace
subjects:
- kind: User
  name: bob
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: allow-port-forward
  apiGroup: ""
```
