# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-empty-interface.md

---
title: Avoid the declaration of empty interfaces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid the declaration of empty interfaces
---

# Avoid the declaration of empty interfaces

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-code-style/no-empty-interface`

**Language:** TypeScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Do not use empty interfaces.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
interface Foo {}
interface Foo extends {}
interface Bar extends Foo {}
interface Foo extends Array<number> {}
interface Foo extends Array<number | {}> {}
interface Foo extends Array<Bar> {}
interface Foo extends R {}
interface Foo<T> extends Bar<T> {}
declare module FooBar { type Baz = typeof baz; export interface Bar extends Baz {} }
interface Foo {

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
interface Foo { name: string; }
interface Foo { name: string; }
interface Bar { age: number; }

// valid because extending multiple interfaces can be used instead of a union type
interface Baz extends Foo, Bar {}
interface Foo { name: string; }
interface Foo { props: string; }
class Bar {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
