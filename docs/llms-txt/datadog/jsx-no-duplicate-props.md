# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/jsx-no-duplicate-props.md

---
title: Avoid duplicate properties in JSX
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid duplicate properties in JSX
---

# Avoid duplicate properties in JSX

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/jsx-no-duplicate-props`

**Language:** JavaScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

Providing duplicate properties to JSX elements can produce unexpected results in your project.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
<Hello name="John" name="John" />;
<Hello name="John" name="John">foo</Hello>;
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
<Hello firstname="John" lastname="Doe" />;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
