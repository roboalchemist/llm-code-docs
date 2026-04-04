# Source: https://docs.datadoghq.com/security/default_rules/def-000-e1g.md

---
title: Public endpoint lacks assigned owner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Public endpoint lacks assigned owner
---

# Public endpoint lacks assigned owner

## Description{% #description %}

This public endpoint has no assigned team. This can lead to maintenance issues and increase the likelihood of undetected vulnerabilities. The lack of ownership and monitoring could significantly impede incident response effectiveness when an attack occurs.

## Rationale{% #rationale %}

This finding works by identifying an API that:

- is processing traffic from the internet
- has no team assigned

## Remediation{% #remediation %}

Assign a team to the endpoint on the [Service Catalog API](https://app.datadoghq.com/software?selectedComponent=endpoint) page.
