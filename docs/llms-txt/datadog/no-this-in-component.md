# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-this-in-component.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-this-in-component.md

---
title: Do not use this in functional components
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use this in functional components
---

# Do not use this in functional components

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-this-in-component`

**Language:** JavaScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

In JavaScript, particularly in the context of React, the `this` keyword is not necessary in functional components. Functional components are simpler constructs that are stateless and do not have access to the `this` keyword. Using `this` in a functional component is erroneous and leads to bugs in your code.

To adhere to this rule, always refer to props directly in functional components. Instead of using `this.props.foo`, use `props.foo`. This ensures that you are accessing the props object directly, rather than trying to access it through `this`, which is not available in functional components.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
function Test(props) {
    return (
        <div>{this.props.foo}</div>
    );
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
function Test(props) {
    return (
        <div>{props.foo}</div>
    );
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 