# Source: https://docs.datadoghq.com/security/default_rules/def-000-rzw.md

---
title: Cluster should have Private Endpoint enabled and public access disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cluster should have Private Endpoint
  enabled and public access disabled
---

# Cluster should have Private Endpoint enabled and public access disabled

## Description{% #description %}

A cluster should have private endpoint enabled and public access disabled. These settings will ensure the cluster is properly isolated from public access.

## Remediation{% #remediation %}

**Note**: A cluster created without private endpoint cannot be modified to enable private endpoint. A new cluster must be created.

Follow the [Customize Network Isolation](https://cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#gcloud) guide from Google Cloud to enable private endpoint and disable public access to your cluster.

## References{% #references %}
