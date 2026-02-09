# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/tsx-no-duplicate-key.md

---
title: Key props must be unique in JSX elements.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Key props must be unique in JSX elements.
---

# Key props must be unique in JSX elements.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `tsx-react/tsx-no-duplicate-key`

**Language:** TypeScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

This rule identifies issues where JSX elements are assigned duplicate `key` properties. In React and similar JSX-based frameworks, the `key` prop is essential for efficiently identifying and managing list items during updates. Using identical keys for multiple elements can lead to unpredictable UI behavior, rendering glitches, and performance degradation. This includes cases where elements in a static array literal have the same key, or when elements generated in dynamic loops (like `map` or `Array.from`) are assigned a constant `key` value, resulting in all generated items having the identical key.

## How to Remidate{% #how-to-remidate %}

To remediate this, ensure that every JSX element within a list or iteration block has a `key` prop whose value is unique among its immediate siblings. For static lists, each element should have a distinct, hardcoded key. When rendering dynamic lists (e.g., using `map`), use a stable and unique identifier from the data item itself (e.g., `item.id` or `item.uuid`). Avoid using static or constant values as keys within loops, as this defeats the purpose of keys. While array indices (`index`) can be used as a last resort, they are only appropriate if the list's items are truly static and their order will never change, as reordering or filtering can lead to unexpected behavior.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
[<Hello key="one" />, <Hello key="one">foo</Hello>, <Hello key="one" />];
[<Hello key={"foo"} />, <Hello key={`foo`}>foo</Hello>];
[<Hello key={a} />, <Hello key={a} />];
data.map(x => <Hello key="a" />);
data.map(x => <Hello key={1}>{x}</Hello>);
data.map(x => <Hello key={"1" + "2"}>{x}</Hello>);
data.map(x => { return <Hello key={true}>{x}</Hello>});
data.map(function(x) { return <Hello key={[]}>{x}</Hello>});
Array.from([1, 2, 3], (x) => <Hello key={{}}>{x}</Hello>);
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
[<Hello key="first" />, <Hello key="second">foo</Hello>, <Hello key="thrid" />];
data.map(x => { return <Hello key={`prefix-${x}`}>{x}</Hello>});
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 