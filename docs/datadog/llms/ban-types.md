# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/ban-types.md

---
title: Avoid certain types
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid certain types
---

# Avoid certain types

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/ban-types`

**Language:** TypeScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Some types have several ways to be defined, and some others could be dangerous. This rule suggests a consistent use of types.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
// use lower-case primitives for consistency
const str: String = 'foo';
const bool: Boolean = true;
const num: Number = 1;
const symb: Symbol = Symbol('foo');
const bigInt: BigInt = 1n;

// use a proper function type
const func: Function = () => 1;

// use safer object types
const lowerObj: Object = {};
const capitalObj: Object = { a: 'string' };

const curly1: {} = 1;
const curly2: {} = { a: 'string' };
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
// use lower-case primitives for consistency
const str: string = 'foo';
const bool: boolean = true;
const num: number = 1;
const symb: symbol = Symbol('foo');
const bigInt: bigint = 1n;

// use a proper function type
const func: () => number = () => 1;

// use safer object types
const lowerObj: object = {};
const capitalObj: { a: string } = { a: 'string' };

const curly1: number = 1;
const curly2: Record<'a', string> = { a: 'string' };
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
