# Source: https://docs.datadoghq.com/security/default_rules/def-00k-rpz.md

---
title: The Kubernetes API server secure port should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes API server secure port
  should be enabled
---

# The Kubernetes API server secure port should be enabled

## Description{% #description %}

The secure port should not be disabled. The secure port is used to serve https with authentication and authorization. If you disable it, no https traffic is served and all traffic is served unencrypted.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node, and either remove the `--secure-port` parameter or set it to a different (non-zero) desired port. For example, `--secure-port=6443` which is also the default value.
