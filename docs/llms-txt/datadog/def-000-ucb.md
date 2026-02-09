# Source: https://docs.datadoghq.com/security/default_rules/def-000-ucb.md

---
title: >-
  Publicly accessible application with a critical vulnerability running on a
  privileged Kubernetes node
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible application with a
  critical vulnerability running on a privileged Kubernetes node
---

# Publicly accessible application with a critical vulnerability running on a privileged Kubernetes node

## Description{% #description %}

Unpatched vulnerabilities in publicly accessible applications can increase the likelihood of exposing weaknesses, creating an entry point for attackers to gain unauthorized access to the pod or container. Granting excessive security capabilities to a pod or container allows unintended lateral movement to other containers or access to the underlying Kubernetes node. Assignment of the pod or container to a node with excessive permissions can increase the blast radius of potential unauthorized access to cloud resources.

## Remediation{% #remediation %}

1. Review any associated vulnerability references or advisories.
1. Apply the appropriate patch based on remediation guidance. If no patch is available, apply compensating controls such as disabling or removing the vulnerable component.
1. Review your Kubernetes pod or container security context configurations to ensure they provide proper isolation boundaries between containers and host resources.
1. Apply possible mitigations, including the use of Kubernetes Pod Security Policies, SELinux, AppArmor, or Seccomp filters.
1. Review the assigned cloud provider roles and permissions on the assigned node to ensure they are scoped to the principle of least privilege.
