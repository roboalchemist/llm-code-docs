# Source: https://docs.datadoghq.com/security/default_rules/acr-cv5-wp5.md

---
title: Containers should not be run with the hostPID flag set to true
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Containers should not be run with the
  hostPID flag set to true
---

# Containers should not be run with the hostPID flag set to true
Classification:complianceFramework:cis-kubernetesControl:5.2.2
## Description{% #description %}

Do not generally permit containers to be run with the hostPID flag set to true.

## Rationale{% #rationale %}

A container running in the host's PID namespace can inspect processes running outside the container. If the container also has access to ptrace capabilities this can be used to escalate privileges outside of the container. There should be at least one PodSecurityPolicy (PSP) defined which does not permit containers to share the host PID namespace. If you need to run containers which require hostPID, this should be defined in a separate PSP and you should carefully check RBAC controls to ensure that only limited service accounts and users are given permission to access that PSP.

## Audit{% #audit %}

Get the set of PSPs with the following command: `kubectl get psp`

For each PSP, check whether privileged is enabled: `kubectl get psp <name> -o=jsonpath='{.spec.hostPID}'`

Verify that there is at least one PSP which does not return true.

## Remediation{% #remediation %}

Create a PSP as described in the Kubernetes documentation, ensuring that the `.spec.hostPID` field is omitted or set to false.

## Impact{% #impact %}

Pods defined with spec.hostPID: true will not be permitted unless they are run under a specific PSP.

## Default value{% #default-value %}

By default, PodSecurityPolicies are not defined.

## References{% #references %}

1. [https://kubernetes.io/docs/concepts/policy/pod-security-policy](https://kubernetes.io/docs/concepts/policy/pod-security-policy)

## CIS controls{% #cis-controls %}

Version 6.5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
