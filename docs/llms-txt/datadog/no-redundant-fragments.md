# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-redundant-fragments.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-redundant-fragments.md

---
title: Fragments should not be used when there is 1 child
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Fragments should not be used when there is 1 child
---

# Fragments should not be used when there is 1 child

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-redundant-fragments`

**Language:** JavaScript

**Severity:** Warning

**Category:** Code Style

## Description{% #description %}

This rule emphasizes that React Fragments should not be used when there is only one child within the component. React Fragments are a useful feature for grouping a list of children without adding extra nodes to the DOM. However, when there is only a single child, the use of Fragments is unnecessary and can lead to cluttered and confusing code.

To avoid violating this rule, remove the Fragment (`<>...</>`) when you have only one child in your component. Instead of wrapping a single child with a Fragment, you can return the child directly.

**Note:** Remove redundant fragments only when the JSX remains syntactically valid. In some cases, such as conditional return statements or components that render multiple adjacent elements, an enclosing element (for example, a Fragment or div) is required for proper parsing. If removing the fragment results in a parsing error such as `Parsing error: ',' expected`, keep the fragment or replace it with another valid wrapper.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
export default function Menu() {
  return (
    <>
      <MenuText />
    </>
  );
}

function MenuText() {
  return (
    <h1>
    <>Menu</>
    </h1>
  );
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
export default function Menu() {
  return <MenuText />;
}

function MenuText() {
  return <h1>Menu</h1>;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
