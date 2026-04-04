# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/ban-ts-comment.md

---
title: Avoid @ts- comments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid @ts-<directive> comments
---

# Avoid @ts-<directive> comments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-code-style/ban-ts-comment`

**Language:** TypeScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Correct your types instead of disabling TypeScript.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
// @ts-expect-error
// @ts-ignore
// @ts-nocheck
// @ts-check
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
// just a comment containing @ts-expect-error somewhere
// just a comment containing @ts-ignore somewhere
// just a comment containing @ts-nocheck somewhere
// just a comment containing @ts-check somewhere
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
