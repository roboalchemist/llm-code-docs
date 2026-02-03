# Source: https://docs.datadoghq.com/security/default_rules/qet-z9y-rwq.md

---
title: Containers should not be allowed to share the host network namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Containers should not be allowed to
  share the host network namespace
---

# Containers should not be allowed to share the host network namespace
Classification:complianceFramework:cis-kubernetesControl:5.2.4 
## Description{% #description %}

Do not generally permit containers to be run with the hostNetwork flag set to true.

## Rationale{% #rationale %}

A container running in the host's network namespace could access the local loopback device, and could access network traffic to and from other pods. There should be at least one PodSecurityPolicy (PSP) defined which does not permit containers to share the host network namespace. If you have need to run containers which require hostNetwork, this should be defined in a separate PSP and you should carefully check RBAC controls to ensure that only limited service accounts and users are given permission to access that PSP.

## Audit{% #audit %}

Get the set of PSPs with the following command: `kubectl get psp`

For each PSP, check whether privileged is enabled: `kubectl get psp <name> -o=jsonpath='{.spec.hostNetwork}'`

Verify that there is at least one PSP which does not return true.

## Remediation{% #remediation %}

Create a PSP as described in the Kubernetes documentation, ensuring that the `.spec.hostNetwork` field is omitted or set to false.

## Impact{% #impact %}

Pods defined with spec.hostNetwork: true will not be permitted unless they are run under a specific PSP.

## Default value{% #default-value %}

By default, PodSecurityPolicies are not defined.

## References{% #references %}

1. [https://kubernetes.io/docs/concepts/policy/pod-security-policy](https://kubernetes.io/docs/concepts/policy/pod-security-policy)

## CIS controls{% #cis-controls %}

Version 6.5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
