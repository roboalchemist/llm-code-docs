# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/jsx-key.md

---
title: Prevent missing key props in iterators/collection literals
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent missing key props in iterators/collection literals
---

# Prevent missing key props in iterators/collection literals

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/jsx-key`

**Language:** JavaScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

In JSX you need to specify a key prop for each item of a list because if it's missing it could lead to unexpected renders or stale UI. This rule checks for possible JSX lists and warns if the key prop is missing.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
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

```jsx
[<Hello key="first" test="foo" />, <Hello key="second" />, <Hello key="third" />];
data.map((x) => <Hello key={x.id}>{x}</Hello>);
Array.from([1, 2, 3], (x) => <Hello key={x.id}>{x}</Hello>);
<Hello key={id} {...{ id, caption }} />
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
