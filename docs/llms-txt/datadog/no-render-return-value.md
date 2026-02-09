# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-render-return-value.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-render-return-value.md

---
title: Avoid usage of the return value of ReactDOM.render
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid usage of the return value of ReactDOM.render
---

# Avoid usage of the return value of ReactDOM.render

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-render-return-value`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Using the return value of the render method is a legacy feature. If you have a valid reason to reference the root React instance, you should assign a callback ref to the root component.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
const inst = ReactDOM.render(<App />, document.body);
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
ReactDOM.render(<App ref={doSomethingWithInst} />, document.body);

ReactDOM.render(<App />, document.body, doSomethingWithInst);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 