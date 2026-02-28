# Source: https://docs.datadoghq.com/security/default_rules/def-000-za6.md

---
title: Ensure GKE node pools do not use default service accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure GKE node pools do not use
  default service accounts
---

# Ensure GKE node pools do not use default service accounts

## Description{% #description %}

The service account running the nodes in a cluster should have the principle of least privilege applied. Without a minimally privileged service account, the impact during a node comprise could be much worse.

## Remediation{% #remediation %}

Follow the documentation from Google Cloud's [Harden your cluster's security](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa) article to configure a non-default service account for your Cluster's nodes.
