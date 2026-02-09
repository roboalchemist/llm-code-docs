# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-duplicate-enum-values.md

---
title: Avoid duplicate enum member values
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid duplicate enum member values
---

# Avoid duplicate enum member values

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/no-duplicate-enum-values`

**Language:** TypeScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

An `enum` should not have duplicate values, which are usually not expected to be present.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
enum A {
    A = 1,
    B = 1,
}
enum B {
    A = 'A',
    B = 'A',
}
enum C {
  A = 'A',
  B = 'A',
  C = 1,
  D = 1,
}
enum E {
    A = 'A',
    B = 'A',
    C = 1,
    D = 1,
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
enum A {
  A,
  B,
}

enum B {
  A = 1,
  B,
}

enum C {
  A = 1,
  B = 2,
}

enum D {
  A = 'A',
  B = 'B',
}

enum E {
  A = 'A',
  B = 'B',
  C,
}

enum F {
  A = 'A',
  B = 'B',
  C = 2,
  D = 1 + 1,
}

enum G {
  A = 3,
  B = 2,
  C,
}

enum H {
  A = 'A',
  B = 'B',
  C = 2,
  D = foo(),
}

enum I {
  A = '',
  B = 0,
}

enum J {
  A = 0,
  B = -0,
  C = NaN,
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 