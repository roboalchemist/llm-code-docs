# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/jsx-no-duplicate-key.md

---
title: Ensures unique key prop
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensures unique key prop
---

# Ensures unique key prop

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/jsx-no-duplicate-key`

**Language:** JavaScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

Duplicate JSX element keys can lead to unexpected behavior. Keys should always be unique.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
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

```jsx
[<Hello key="first" />, <Hello key="second">foo</Hello>, <Hello key="third" />];
data.map(x => { return <Hello key={`prefix-${x}`}>{x}</Hello>});
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 