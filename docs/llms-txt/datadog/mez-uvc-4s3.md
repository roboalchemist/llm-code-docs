# Source: https://docs.datadoghq.com/security/default_rules/mez-uvc-4s3.md

---
title: The API server should explicitly set a service account public key file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The API server should explicitly set a
  service account public key file
---

# The API server should explicitly set a service account public key file
Classification:complianceFramework:cis-kubernetesControl:1.2.28 
## Description{% #description %}

Explicitly set a service account public key file for service accounts on the apiserver.

## Rationale{% #rationale %}

By default, if no âservice-account-key-file is specified to the apiserver, it uses the private key from the TLS serving certificate to verify service account tokens. To ensure that the keys for service account tokens could be rotated as needed, a separate public/private key pair should be used for signing service account tokens. Hence, the public key should be specified to the apiserver with âservice-account-key-file.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--service-account-key-file` argument exists and is set as appropriate.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--service-account-key-file` parameter to the public key file for service accounts: `--service-account-key-file=<filename>`

## Impact{% #impact %}

The corresponding private key must be provided to the controller manager. You would need to securely maintain the key file and rotate the keys based on your organization's key rotation policy.

## Default value{% #default-value %}

By default, `--service-account-key-file` argument is not set.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)
1. [https://github.com/kubernetes/kubernetes/issues/24167](https://github.com/kubernetes/kubernetes/issues/24167)

## CIS controls{% #cis-controls %}

Version 6 3 Secure Configurations for Hardware and Software on Mobile Devices, Laptops, Workstations, and Servers Version 7 5 Secure Configuration for Hardware and Software on Mobile Devices, Laptops, Workstations and Servers
