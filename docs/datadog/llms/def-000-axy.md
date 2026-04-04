# Source: https://docs.datadoghq.com/security/default_rules/def-000-axy.md

---
title: The GKE cluster should be encrypted using customer-managed keys in KMS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The GKE cluster should be encrypted
  using customer-managed keys in KMS
---

# The GKE cluster should be encrypted using customer-managed keys in KMS

## Description{% #description %}

Kubernetes secrets, stored in etcd, at the application layer should be encrypted using a customer-managed key in Cloud KMS. Encrypting the application layer this way ensures that sensitive data is safeguarded properly if etcd becomes compromised by an attacker.

## Remediation{% #remediation %}

Follow the steps in Google Cloud's [Enable application-layer secrets encryption documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets#enabling).
