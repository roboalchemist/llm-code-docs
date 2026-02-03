# Source: https://docs.datadoghq.com/security/default_rules/def-00k-4s3.md

---
title: >-
  The Kubernetes API server should use a service account public key file for
  service accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes API server should use a
  service account public key file for service accounts
---

# The Kubernetes API server should use a service account public key file for service accounts
 
## Description{% #description %}

A service account public key file should be explicitiy set for service accounts on the API server. By default, if no `--service-account-key-file` argument is specified to the apiserver, it uses the private key from the TLS serving certificate to verify service account tokens. To ensure that the keys for service account tokens can be rotated as needed, a separate public/private key pair should be used for signing service account tokens.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--service-account-key-file` parameter to the public key file for service accounts: `--service-account-key-file=<filename>`
