# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/rbac_roles_with_attach_permission.md

---
title: RBAC roles with attach permission
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RBAC roles with attach permission
---

# RBAC roles with attach permission

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d45330fd-f58d-45fb-a682-6481477a0f84`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

### Description{% #description %}

Roles or ClusterRoles that permit attaching to containers via `kubectl attach` can be abused by attackers to read process output (stdout, stderr) and send input (stdin) to running processes. They can also allow a malicious user to attach to a privileged container, resulting in privilege escalation. For this reason, the `pods/attach` resource should not be included in production Role or ClusterRole rules. This rule flags Role or ClusterRole documents whose rules include the `pods/attach` resource (and related verb entries such as `create` or `*`). Findings support least-privilege enforcement by identifying and removing attach permissions from cluster roles.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: my-namespace
  name: allow-attach-neg
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: allow-attach-neg
  namespace: my-namespace
subjects:
- kind: User
  name: bob
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: allow-attach-neg
  apiGroup: ""
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: my-namespace
  name: allow-attach
rules:
- apiGroups: [""]
  resources: ["pods", "pods/attach"]
  verbs: ["get", "list", "create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: allow-attach
  namespace: my-namespace
subjects:
- kind: User
  name: bob
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: allow-attach
  apiGroup: ""
```
