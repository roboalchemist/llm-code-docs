# Source: https://docs.datadoghq.com/security/default_rules/def-000-1oa.md

---
title: Google Cloud Kubernetes Engine cluster should not be publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Cloud Kubernetes Engine cluster
  should not be publicly accessible
---

# Google Cloud Kubernetes Engine cluster should not be publicly accessible
 
## Description{% #description %}

The control plane of a GKE cluster should not be open to the internet. Limiting internet access significantly reduces the attack surface.

## Remediation{% #remediation %}

Consider [allow-listing specific IP ranges in the cluster configuration](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).

Alternatively, consider [making the cluster private](https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) and accessing it from an internal network or [through Identity-aware Proxy (IaP)](https://cloud.google.com/iap/docs/enabling-kubernetes-howto).
