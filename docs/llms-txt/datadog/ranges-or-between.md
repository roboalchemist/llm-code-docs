# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/ranges-or-between.md

---
title: Prefer ranges/between over of complex comparisons
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer ranges/between over of complex comparisons
---

# Prefer ranges/between over of complex comparisons

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/ranges-or-between`

**Language:** Ruby

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The rule "Prefer ranges/between over complex comparisons" advises developers to use the range or `between?` method for comparisons instead of complex conditional statements. This practice increases the readability and clarity of your code. Complex comparisons using logical operators can be difficult to understand and prone to errors.

This rule is important because it promotes cleaner, more efficient, and easier-to-read code. When code is easier to read, it's easier to maintain, debug, and less likely to contain hidden bugs. Using the range or `between?` method is a more concise way to check if a value falls within a specific range.

To adhere to this rule, replace complex comparison statements with the range or `between?` method. For example, instead of writing `foo >= 42 && foo <= 99`, you can write `(42..99).include?(foo)` or `foo.between?(42, 99)`. These alternatives are more straightforward and visually cleaner, making your code easier to understand.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
acceptable_foo if foo >= 42 && foo <= 99
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
acceptable_foo if (42..99).include?(foo)
acceptable_foo if foo.between?(42, 99)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 