# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-extra-non-null-assertion.md

---
title: Avoid extra non-null assertions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid extra non-null assertions
---

# Avoid extra non-null assertions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/no-extra-non-null-assertion`

**Language:** TypeScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

The non `null` or `undefined` assertion operation should not be used twice in a single expression.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
const bar = foo!!.bar;
function foo(bar: number | undefined) { const bar: number = bar!!; }
function foo(bar?: { n: number }) { return bar!?.n; }
function foo(bar?: { n: number }) { return bar!?.(); }

// parentheses
const foo: { bar: number } | null = null; const bar = (foo!)!.bar;
function foo(bar?: { n: number }) { return (bar!)?.n; }
function foo(bar?: { n: number }) { return (bar)!?.n; }
function foo(bar?: { n: number }) { return (bar!)?.(); }
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
const bar = foo!.bar;

function foo(bar: number | undefined) {
  const bar: number = bar!;
}

function foo(bar?: { n: number }) {
  return bar?.n;
}

// https://github.com/typescript-eslint/typescript-eslint/issues/2166
checksCounter?.textContent!.trim();

// https://github.com/typescript-eslint/typescript-eslint/issues/2732
function foo(key: string | null) {
  const obj = {};
  return obj?.[key!];
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
