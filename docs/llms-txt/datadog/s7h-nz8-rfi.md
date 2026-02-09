# Source: https://docs.datadoghq.com/security/default_rules/s7h-nz8-rfi.md

---
title: Resources should be created in a non-default namespace in Kubernetes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Resources should be created in a
  non-default namespace in Kubernetes
---

# Resources should be created in a non-default namespace in Kubernetes
Classification:complianceFramework:cis-kubernetesControl:5.7.4 
## Description{% #description %}

Kubernetes provides a default namespace, where objects are placed if no namespace is specified for them. Placing objects in this namespace makes application of RBAC and other controls more difficult.

## Rationale{% #rationale %}

Resources in a Kubernetes cluster should be segregated by namespace, to allow for security controls to be applied at that level and to make it easier to manage resources.

## Audit{% #audit %}

Run this command to list objects in default namespace: `kubectl get all`

The only entries there should be system managed resources such as the Kubernetes service.

## Remediation{% #remediation %}

Ensure that namespaces are created to allow for appropriate segregation of Kubernetes resources and that all new resources are created in a specific namespace.

## Impact{% #impact %}

None

## Default value{% #default-value %}

Unless a namespace is specific on object creation, the default namespace will be used.

## References{% #references %}

None

## CIS controls{% #cis-controls %}

None
