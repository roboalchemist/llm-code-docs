# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/role_binding_to_default_service_account.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/k8s/role_binding_to_default_service_account.md

---
title: Role binding to default service account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Role binding to default service account
---

# Role binding to default service account

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1e749bc9-fde8-471c-af0c-8254efd2dee5`

**Cloud Provider:** Kubernetes

**Platform:** Kubernetes

**Severity:** Medium

**Category:** Insecure Defaults

#### Learn More{% #learn-more %}

- [Provider Reference](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

### Description{% #description %}

No RoleBinding or ClusterRoleBinding should bind to the default ServiceAccount. Binding roles to the default ServiceAccount grants those permissions to all pods that use that account in the namespace, increasing the risk of unintended privilege escalation. This undermines least-privilege principles and can expose workloads to unnecessary privileges.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: User
  name: jane
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: User
  name: jane
  apiGroup: rbac.authorization.k8s.io
- kind: ServiceAccount
  name: default
  namespace: kube-system
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```
