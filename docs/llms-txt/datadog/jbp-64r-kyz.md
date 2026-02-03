# Source: https://docs.datadoghq.com/security/default_rules/jbp-64r-kyz.md

---
title: Each controller should use individual service account credentials
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Each controller should use individual
  service account credentials
---

# Each controller should use individual service account credentials
Classification:complianceFramework:cis-kubernetesControl:1.3.3 
## Description{% #description %}

Use individual service account credentials for each controller.

## Rationale{% #rationale %}

The controller manager creates a service account per controller in the kube-system namespace, generates a credential for it, and builds a dedicated API client with that service account credential for each controller loop to use. Setting the `--use-service-account-credentials` to true runs each control loop within the controller manager using a separate service account credential. When used in combination with RBAC, this ensures that the control loops run with the minimum permissions required to perform their intended tasks.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-controller-manager
```

Verify that the `--use-service-account-credentials` argument is set to true.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node to set the below parameter:

```
--use-service-account-credentials=true
```

## Impact{% #impact %}

Whatever authorizer is configured for the cluster, it must grant sufficient permissions to the service accounts to perform their intended tasks. When using the RBAC authorizer, those roles are created and bound to the appropriate service accounts in the kube-system namespace automatically with default roles and rolebindings that are auto-reconciled on startup. If using other authorization methods (ABAC, Webhook, etc.), the cluster deployer is responsible for granting appropriate permissions to the service accounts (the required permissions can be seen by inspecting the `controller-roles.yaml` and `controller-role-bindings.yaml` files for the RBAC roles.

## Default value{% #default-value %}

By default, `--use-service-account-credentials` is set to false.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-controller-manager/](https://kubernetes.io/docs/admin/kube-controller-manager/)
1. [https://kubernetes.io/docs/admin/service-accounts-admin/](https://kubernetes.io/docs/admin/service-accounts-admin/)
1. [https://github.com/kubernetes/kubernetes/blob/release-1.6/plugin/pkg/auth/authorizer/rbac/bootstrappolicy/testdata/controller-roles.yaml](https://github.com/kubernetes/kubernetes/blob/release-1.6/plugin/pkg/auth/authorizer/rbac/bootstrappolicy/testdata/controller-roles.yaml)
1. [https://github.com/kubernetes/kubernetes/blob/release-1.6/plugin/pkg/auth/authorizer/rbac/bootstrappolicy/testdata/controller-role-bindings.yaml](https://github.com/kubernetes/kubernetes/blob/release-1.6/plugin/pkg/auth/authorizer/rbac/bootstrappolicy/testdata/controller-role-bindings.yaml)
1. [https://kubernetes.io/docs/admin/authorization/rbac/#controller-roles](https://kubernetes.io/docs/admin/authorization/rbac/#controller-roles)

## CIS controls{% #cis-controls %}

Version 6.14 Controlled Access Based on the Need to Know

Version 7.4 Controlled Use of Administrative Privileges
