# Source: https://docs.datadoghq.com/security/default_rules/def-000-qoc.md

---
title: Azure Container registries should use private link
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Container registries should use
  private link
---

# Azure Container registries should use private link

## Description{% #description %}

This rule checks if Azure Container Registries are using Private Link connections. Using Private Link connections enhances security by ensuring that communication between resources is isolated and private.

## Remediation{% #remediation %}

To ensure Azure Container Registries use Private Link connections, see [Enable Private Link for Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/private-link-overview).
