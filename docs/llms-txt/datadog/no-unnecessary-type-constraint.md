# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-unnecessary-type-constraint.md

---
title: Avoid unnecessary constraints on generic types
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unnecessary constraints on generic types
---

# Avoid unnecessary constraints on generic types

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/no-unnecessary-type-constraint`

**Language:** TypeScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

It is redundant to `extend` from `any` or `unknown`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
function data<T extends any>() {}
function data<T extends any, U>() {}
function data<T, U extends any>() {}
function data<T extends any, U extends T>() {}
const data = <T extends any>() => {};
const data = <T extends any>() => {};
const data = <T extends any>() => {};
const data = <T extends any,>() => {};
const data = <T extends any, >() => {};
const data = <T extends any ,>() => {};
const data = <T extends any , >() => {};
const data = <T extends any = unknown>() => {};
const data = <T extends any, U extends any>() => {};
function data<T extends unknown>() {}
const data = <T extends any>() => {};
const data = <T extends unknown>() => {};
class Data<T extends unknown> {}
const Data = class<T extends unknown> {};

class Data {
  member<T extends unknown>() {}
}

const Data = class {
  member<T extends unknown>() {}
};

interface Data<T extends unknown> {}
type Data<T extends unknown> = {};
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
function data() {}
function data<T>() {}
function data<T, U>() {}
function data<T extends number>() {}
function data<T extends number | string>() {}
function data<T extends any | number>() {}

type TODO = any;
function data<T extends TODO>() {}

const data = () => {};
const data = <T>() => {};
const data = <T, U>() => {};
const data = <T extends number>() => {};
const data = <T extends number | string>() => {};
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
