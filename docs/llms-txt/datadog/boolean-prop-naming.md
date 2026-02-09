# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/boolean-prop-naming.md

---
title: Consistent naming for boolean props
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Consistent naming for boolean props
---

# Consistent naming for boolean props

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/boolean-prop-naming`

**Language:** TypeScript

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Enforces a consistent naming pattern for boolean props to ensure that the variable is prefixed with either `is` or `has` (or the uppercase equivalent).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
type Props = {
  enabled: boolean;
  __enabled: boolean;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
type Props = {
  isEnabled: boolean;
  hasFoo: boolean;
  __hasFoo: boolean;
  IS_ENABLED: boolean;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 