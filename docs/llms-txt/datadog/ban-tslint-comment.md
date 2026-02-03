# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/ban-tslint-comment.md

---
title: Avoid using TSLint comments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using TSLint comments
---

# Avoid using TSLint comments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-code-style/ban-tslint-comment`

**Language:** TypeScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Do not disable TypeScript checks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
/* tslint:disable */
/* tslint:enable */
/* tslint:disable:rule1 rule2 rule3... */
/* tslint:enable:rule1 rule2 rule3... */
// tslint:disable-next-line
someCode(); // tslint:disable-line
// tslint:disable-next-line:rule1 rule2 rule3...
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
// This is a comment that just happens to mention tslint
/* This is a multiline comment that just happens to mention tslint */
someCode(); // This is a comment that just happens to mention tslint
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 