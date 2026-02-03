# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/cluster_admin_role_binding_with_super_user_permissions.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/cluster_admin_role_binding_with_super_user_permissions.md

---
title: Cluster admin rolebinding with superuser permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cluster admin rolebinding with superuser
  permissions
---

# Cluster admin rolebinding with superuser permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `249328b8-5f0f-409f-b1dd-029f07882e11`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Low

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles)

### Description{% #description %}

Ensure that the `cluster-admin` role is used only where required (RBAC). This rule detects ClusterRoleBinding resources that bind to the `cluster-admin` role, which grants superuser permissions across the cluster. Such bindings increase risk and should be limited to adhere to the principle of least privilege.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: tiller-clusterrolebinding
subjects:
- kind: ServiceAccount
  name: tiller
  namespace: kube-system
roleRef:
  kind: ClusterRole
  name: view
  apiGroup: ""
# trigger validation
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: tiller-clusterrolebinding
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: ""
```
