# Source: https://docs.datadoghq.com/security/default_rules/def-00k-b7g.md

---
title: >-
  The Kubernetes API server should validate that the service account token
  exists in etcd
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes API server should
  validate that the service account token exists in etcd
---

# The Kubernetes API server should validate that the service account token exists in etcd

## Description{% #description %}

Service accounts should be validated before validating the token. If `--service-account-lookup` is not enabled, the API server only verifies that the authentication token is valid, and does not validate that the service account token mentioned in the request is actually present in etcd. This enables you to use a service account token even after the corresponding service account is deleted.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the below parameter. `--service-account-lookup=true`

**NOTE**: Alternatively, you can delete the `--service-account-lookup` parameter from this file so that the default takes effect.
