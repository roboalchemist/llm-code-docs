# Source: https://docs.datadoghq.com/security/default_rules/def-000-k6h.md

---
title: >-
  Application with a critical vulnerability in a container with elevated
  privileges assigned to a privileged Kubernetes node
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Application with a critical
  vulnerability in a container with elevated privileges assigned to a privileged
  Kubernetes node
---

# Application with a critical vulnerability in a container with elevated privileges assigned to a privileged Kubernetes node

## Description{% #description %}

Unpatched vulnerabilities can increase the likelihood of exposing weaknesses, creating an entry point for attackers to gain unauthorized access to the pod or container. Granting excessive security capabilities to a pod or container can lead to unintended lateral movement to other containers, access to the underlying Kubernetes node, or access to cloud provider resources.

## Remediation{% #remediation %}

1. Review any associated vulnerability references or advisories.
1. Apply the appropriate patch based on remediation guidance. If no patch is available, apply compensating controls such as disabling or removing the vulnerable component.
1. Review your Kubernetes pod or container security context configurations to ensure they provide proper isolation boundaries between containers and host resources.
1. Apply possible mitigations, including the use of Kubernetes Pod Security Policies, SELinux, AppArmor, or Seccomp filters.
1. Review the assigned cloud provider roles and permissions on the assigned node to ensure they are scoped to the principle of least privilege.
