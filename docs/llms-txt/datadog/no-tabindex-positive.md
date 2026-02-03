# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-tabindex-positive.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-tabindex-positive.md

---
title: Do not use positive values for a span's tabIndex attribute
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use positive values for a span's tabIndex attribute
---

# Do not use positive values for a span's tabIndex attribute

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-tabindex-positive`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule is to help ensure a logical and efficient tab order in web applications. The `tabIndex` attribute specifies the tab order of an element, with a positive value indicating that the element should be included in the tab order. However, using positive values can disrupt the natural tab order, leading to a confusing and potentially inaccessible user interface.

This rule is particularly important for ensuring accessibility and usability. Users who rely on keyboard navigation, such as those with motor disabilities or vision impairments, may struggle to navigate a page if the tab order is not logical and predictable.

To adhere to this rule, you should avoid using positive values for the `tabIndex` attribute. Instead, use a `tabIndex` of `0` to include an element in the tab order based on its position in the document flow, or a `tabIndex` of `-1` to exclude an element from the tab order.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
function Menu() {
    return (
        <div>
            <span tabIndex="5">item1</span>
            <span tabIndex={3}>item2</span>
        </div>
    );
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
function Menu() {
    return (
        <div>
            <span tabIndex="-1">item1</span>
            <span tabIndex={0}>item2</span>
        </div>
    );
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 