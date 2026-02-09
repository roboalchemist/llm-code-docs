# Source: https://docs.datadoghq.com/security/default_rules/def-000-dfy.md

---
title: >-
  Application with a critical vulnerability in a container with elevated
  privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Application with a critical
  vulnerability in a container with elevated privileges
---

# Application with a critical vulnerability in a container with elevated privileges

## Description{% #description %}

Unpatched vulnerabilities can increase the likelihood of exposing weaknesses, creating an entry point for attackers to gain unauthorized access to the pod or container. Granting excessive security context capabilities to a pod or container can lead to unintended lateral movement to other containers or to the underlying node resources.

## Remediation{% #remediation %}

1. Review any associated vulnerability references or advisories.
1. Apply the appropriate patch based on remediation guidance. If no patch is available, apply compensating controls such as disabling or removing the vulnerable component.
1. Review your Kubernetes pod or container security context configurations to ensure they provide proper isolation boundaries.
