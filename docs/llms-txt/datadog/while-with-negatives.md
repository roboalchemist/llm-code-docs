# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/while-with-negatives.md

---
title: Prefer until over while for negative conditions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer until over while for negative conditions
---

# Prefer until over while for negative conditions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/while-with-negatives`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer until over while for negative conditions" suggests that, when writing loops in Ruby, we should use `until` instead of `while` for negative conditions. This is because `until` is more readable and intuitive when dealing with negative conditions. It allows the code to be more easily understood by other developers, which is crucial for maintaining clean and efficient code.

The importance of this rule lies in the readability and maintainability of the code. Using `until` for negative conditions makes the code more straightforward and self-explanatory. It reduces the cognitive load required to understand the code, making it easier for other developers to maintain and modify the code in the future.

To follow this rule, you need to replace `while` with `until` when dealing with negative conditions. For example, instead of writing `perform_work while !is_weekend`, you should write `perform_work until is_weekend`. This change improves the readability of the code without affecting its functionality.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
perform_work while !is_weekend
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
perform_work until is_weekend
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
