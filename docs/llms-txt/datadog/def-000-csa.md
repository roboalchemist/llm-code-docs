# Source: https://docs.datadoghq.com/security/default_rules/def-000-csa.md

---
title: EKS Cluster secrets encryption should be enabled and use KMS CMKs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EKS Cluster secrets encryption should
  be enabled and use KMS CMKs
---

# EKS Cluster secrets encryption should be enabled and use KMS CMKs

## Description{% #description %}

EKS clusters should use AWS KMS customer-managed keys (CMKs) for envelope encryption of Kubernetes secrets. This allows you to encrypt your secrets with a unique data key, which can be automatically rotated on a recurring schedule.

## Remediation{% #remediation %}

For guidance on configuring EKS cluster secrets encryption, refer to the [Encrypt Kubernetes secrets with KMS on existing clusters](https://docs.aws.amazon.com/eks/latest/userguide/enable-kms.html) section of the Amazon EKS User Guide.
