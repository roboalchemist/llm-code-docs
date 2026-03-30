# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-danger-with-children.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-danger-with-children.md

---
title: Avoid using children with dangerouslySetInnerHTML
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using children with dangerouslySetInnerHTML
---

# Avoid using children with dangerouslySetInnerHTML

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-danger-with-children`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

If both `children` and `dangerouslySetInnerHTML` are set, it's unclear which one should take precedence. React will throw a warning if both are set. This rule enforces the use of either `children` or `dangerouslySetInnerHTML` but not both.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
<div dangerouslySetInnerHTML={{ __html: "HTML" }}>{Children}</div>;
<Hello dangerouslySetInnerHTML={{ __html: "HTML" }}>Children</Hello>;
<Hello dangerouslySetInnerHTML={{ __html: "HTML" }}><Another /></Hello>;
React.createElement("div", { dangerouslySetInnerHTML: { __html: "HTML" } }, "Children");
React.createElement("Hello", { dangerouslySetInnerHTML: { __html: "HTML" } }, "Children");
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
<div dangerouslySetInnerHTML={{ __html: "HTML" }} />;
<Hello dangerouslySetInnerHTML={{ __html: "HTML" }} />;
<div>Children</div>;
<Hello>Children</Hello>;
React.createElement("div", { dangerouslySetInnerHTML: { __html: "HTML" } });
React.createElement("Hello", { dangerouslySetInnerHTML: { __html: "HTML" } });
React.createElement("div", {}, "Children");
React.createElement("Hello", {}, "Children");
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
