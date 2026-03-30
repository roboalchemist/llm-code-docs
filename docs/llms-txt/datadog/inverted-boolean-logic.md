# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/inverted-boolean-logic.md

---
title: Inverted boolean logic is hard to read and should be avoided
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Inverted boolean logic is hard to read and should be avoided
---

# Inverted boolean logic is hard to read and should be avoided

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/inverted-boolean-logic`

**Language:** Apex

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule highlights the importance of avoiding inverted boolean logic, such as using negations with equality or relational expressions. Inverted boolean logic often makes code harder to read and understand because it requires extra mental effort to parse expressions like `!(foo == 42)` instead of the more straightforward `foo != 42`. Clear and direct boolean expressions improve code readability and maintainability.

To comply with this rule, prefer writing boolean expressions without negations around comparisons. For example, use `foo != 42` instead of `!(foo == 42)`, and `bar <= 51` instead of `!(bar > 51)`. Adopting this practice leads to cleaner, more intuitive code that aligns with common coding standards and best practices in Apex development.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
if (!(foo == 42)) {
}


Boolean b = !(bar > 51);
```

## Compliant Code Examples{% #compliant-code-examples %}

```
if (foo != 42) {
}


Boolean b = (bar <= 51);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
