# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-unaccessible-heading.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-unaccessible-heading.md

---
title: Headings must be accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Headings must be accessible
---

# Headings must be accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-unaccessible-heading`

**Language:** JavaScript

**Severity:** Warning

**Category:** Code Style

## Description{% #description %}

This rule ensures that all heading elements in your JavaScript code are accessible to all users, including those using assistive technologies like screen readers. This helps ensure that your web pages are inclusive and accessible to all users, regardless of their abilities or disabilities.

In the non-compliant code example, the heading element `<h1 aria-hidden>Foo</h1>` is marked with the `aria-hidden` attribute, which hides the element from assistive technologies. This is a violation of the rule because it makes the heading inaccessible to users who rely on these technologies.

To avoid these violations, ensure that all your heading elements are visible to assistive technologies and provide useful information. Don't use the `aria-hidden` attribute on them unless it's absolutely necessary.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
function Test() {
  return (
    <>
      <h1 aria-hidden>Foo</h1>
      <h1/>
    </>
  );
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
function Test() {
  return (
    <h1>Foo</h1>
  );
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
