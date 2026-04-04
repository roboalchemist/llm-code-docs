# Source: https://docs.datadoghq.com/security/default_rules/def-000-n2g.md

---
title: Azure group has administrative privileges over resources
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure group has administrative
  privileges over resources
---

# Azure group has administrative privileges over resources

## Description{% #description %}

This rule identifies when a group has administrative level permissions at the root (most permissive) scope.

## Rationale{% #rationale %}

Administrative Azure role assignments at the root scope have permissions on every Azure resource within a tenant, including all child management groups and subscriptions. This is the widest possible scope and is rarely needed. A role with these privileges could potentially, whether unknowingly or purposefully, cause security issues or data leaks. Roles with these levels of access may also be targeted by an adversary to compromise resources across the entire Azure tenant.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions and scope of a role assignment to the minimum necessary.
