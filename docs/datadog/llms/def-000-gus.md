# Source: https://docs.datadoghq.com/security/default_rules/def-000-gus.md

---
title: >-
  Publicly accessible application in a container with elevated privileges
  assigned to a privileged Kubernetes node
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible application in a
  container with elevated privileges assigned to a privileged Kubernetes node
---

# Publicly accessible application in a container with elevated privileges assigned to a privileged Kubernetes node

## Description{% #description %}

Granting excessive security capabilities to a pod or container can lead to unintended lateral movement to other containers, access to the underlying Kubernetes node, or access to cloud provider resources. Assignment of the pod or container to a node with privileged roles or permissions increases the blast radius of unauthorized access to cloud resources.

## Remediation{% #remediation %}

1. Review your Kubernetes pod or container security context configurations to ensure they provide proper isolation boundaries between containers and host resources.
1. Apply possible mitigations, including the use of Kubernetes Pod Security Policies, SELinux, AppArmor, or Seccomp filters.
1. Review the assigned cloud provider roles and permissions on the assigned node to ensure they are scoped to the principle of least privilege.
