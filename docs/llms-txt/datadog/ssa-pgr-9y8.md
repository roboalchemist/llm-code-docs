# Source: https://docs.datadoghq.com/security/default_rules/ssa-pgr-9y8.md

---
title: Service accounts on the controller manager should have a private key file set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Service accounts on the controller
  manager should have a private key file set
---

# Service accounts on the controller manager should have a private key file set
Classification:complianceFramework:cis-kubernetesControl:1.3.4 
## Description{% #description %}

Explicitly set a service account private key file for service accounts on the controller manager.

## Rationale{% #rationale %}

To ensure that keys for service account tokens can be rotated as needed, a separate public/private key pair should be used for signing service account tokens. The private key should be specified to the controller manager with `--service-account-private-key-file` as appropriate.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-controller-manager
```

Verify that the `--service-account-private-key-file` argument is set as appropriate.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node and set the `--service-account-private-key-file parameter` to the private key file for service accounts:

```
--service-account-private-key-file=<filename>
```

## Impact{% #impact %}

You would need to securely maintain the key file and rotate the keys based on your organization's key rotation policy.

## Default value{% #default-value %}

By default, `--service-account-private-key-file` it not set.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-controller-manager/](https://kubernetes.io/docs/admin/kube-controller-manager/)

## CIS controls{% #cis-controls %}

Version 6.14 Controlled Access Based on the Need to Know

Version 7.4 Controlled Use of Administrative Privileges
