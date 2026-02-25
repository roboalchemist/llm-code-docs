# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-unsafe-assignment.md

---
title: Avoid assigning a value with type any
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid assigning a value with type any
---

# Avoid assigning a value with type any

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/no-unsafe-assignment`

**Language:** TypeScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

The `any` type in TypeScript is dangerously broad, leading to unexpected behavior. Using `any` should be avoided.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
const x = 1 as any;
const x = 1 as any,
function foo(a = 1 as any) {}
class Foo { constructor(private a = 1 as any) {} }
class Foo { private a = 1 as any; }
const [x] = 1 as any;
const [x] = [] as any[];

// TS treats the assignment pattern weirdly in this case
[[[[x]]]] = [1 as any];
const x = [...(1 as any)];
const x = [...([] as any[])];

const x = { y: 1 as any };
const x = { y: { z: 1 as any } };
const x = { ...(1 as any) };
<Foo a={1 as any} />;
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
const x = 1;
const x: number = 1;
const x = 1, y = 1;
let x;
let x = 1, y;
function foo(a = 1) {}
class Foo { constructor(private a = 1) {} }
class Foo { private a = 1; }
const x: Set<string> = new Set();
const x: Set<string> = new Set<string>();
const [x] = [1];
const [x, y] = [1, 2] as number[];
const [x, ...y] = [1, 2, 3, 4, 5];
const [x, ...y] = [1];
const [{ ...x }] = [{ x: 1 }] as [{ x: any }];
function foo(x = 1) {}
function foo([x] = [1]) {}
function foo([x, ...y] = [1, 2, 3, 4, 5]) {}
function foo([x, ...y] = [1]) {}
// this is not checked, because there's no annotation to compare it with
const x = new Set<any>();
const x = { y: 1 };
const x = { y = 1 };
const x = { y(){} };
const x: { y: number } = { y: 1 };
const x = [...[1, 2, 3]];
const [{ [`x${1}`]: x }] = [{ [`x`]: 1 }] as [{ [`x`]: any }];
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
