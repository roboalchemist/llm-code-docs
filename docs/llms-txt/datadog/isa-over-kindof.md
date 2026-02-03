# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/isa-over-kindof.md

---
title: Prefer is_a? over kind_of?
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer is_a? over kind_of?
---

# Prefer is_a? over kind_of?

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/isa-over-kindof`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer `is_a?` over `kind_of?`" suggests to use the method `is_a?` instead of `kind_of?` in your Ruby code. Both `is_a?` and `kind_of?` methods check if an object is an instance of a class or its subclasses. However, `is_a?` is generally preferred due to its clear and concise terminology.

This rule is important for maintaining consistency and readability in your code. Using `is_a?` makes your code more understandable to other developers because its function is immediately apparent from its name. On the other hand, `kind_of?` might lead to confusion as it's not as clear in its function.

To avoid this rule violation, always use the `is_a?` method when you want to check the class of an object. For example, instead of writing `something.kind_of?(Array)`, you should write `something.is_a?(Array)`. This will make your code easier to read and understand, leading to better maintainability and fewer bugs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
something.kind_of?(Array)
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
something.is_a?(Array)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 