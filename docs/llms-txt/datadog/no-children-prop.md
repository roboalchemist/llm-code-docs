# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-children-prop.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-children-prop.md

---
title: Avoid passing children as props
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid passing children as props
---

# Avoid passing children as props

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-children-prop`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Children should be used as actual children not a JSX prop. This rule enforces the use of children as an element between the JSX element opening and closing tag.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
<div children='Children' />;

<MyComponent children={<AnotherComponent />} />;
<MyComponent children={['Child 1', 'Child 2']} />;

React.createElement("div", { children: 'Children' });
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
<div>Children</div>;
<MyComponent>Children</MyComponent>;
<MyComponent>
  <span>Child 1</span>
  <span>Child 2</span>
</MyComponent>;
React.createElement("div", {}, 'Children');
React.createElement("div", 'Child 1', 'Child 2');
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 