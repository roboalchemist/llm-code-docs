# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/tsx-key.md

---
title: Enforce key prop for JSX elements in lists or iterators
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce key prop for JSX elements in lists or iterators
---

# Enforce key prop for JSX elements in lists or iterators

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `tsx-react/tsx-key`

**Language:** TypeScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

In React, each JSX element rendered within a list or an iterator (such as `Array.prototype.map()`) requires a unique and stable `key` prop. This `key` helps React efficiently identify which items have changed, are added, or are removed during updates. Failing to provide a `key` can lead to performance issues, unexpected rendering behavior, incorrect component state, and stale UI, especially when list items are reordered, filtered, or added/removed.

## How to Remediate{% #how-to-remediate %}

To fix this, provide a unique and stable `key` prop to each top-level JSX element returned within a list or iterator. Ideally, the `key` should be a unique identifier from your data (e.g., `item.id`). Avoid using array indices as `key`s if the list items can change order, be filtered, or be added/removed, as this can negate the benefits of keys. Note that React Fragment shorthand (`<>...</>`) does not support the `key` prop; for keyed fragments, use `React.Fragment` explicitly (e.g., `<React.Fragment key={item.id}>...</React.Fragment>`).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
[<></>];
[<Hello a="foo" />, <Hello>foo</Hello>, <Hello />];
[<Hello />, <Hello a="">foo</Hello>, <Hello />];
data.map(x => <Hello a="" />);
data.map(x => <Hello>{x}</Hello>);
data.map(x => <Hello a="">{x}</Hello>);
data.map(x => { return <Hello>{x}</Hello>});
data.map(x => { return <Hello a="">{x}</Hello>});
data.map(function(x) { return <Hello>{x}</Hello>});
data.map(function(x) { return <Hello>{x}</Hello>});
Array.from([1, 2, 3], (x) => <Hello>{x}</Hello>);
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
[<Hello key="first" test="foo" />, <Hello key="second" />, <Hello key="third" />];
data.map((x) => <Hello key={x.id}>{x}</Hello>);
Array.from([1, 2, 3], (x) => <Hello key={x.id}>{x}</Hello>);
<Hello key={id} {...{ id, caption }} />
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
