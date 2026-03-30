# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/predicate-methods.md

---
title: 'Use predicate methods over explicit comparisons with `==` '
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use predicate methods over explicit comparisons with `==`
---

# Use predicate methods over explicit comparisons with `==`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/predicate-methods`

**Language:** Ruby

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The rule 'Use predicate methods over explicit comparisons with `==`' encourages the use of predicate methods in Ruby for cleaner, more idiomatic code. Predicate methods are methods that return a boolean value, and in Ruby, they are typically identified by the question mark at the end of the method name. These methods provide a more expressive and concise way to perform certain checks, such as checking if a number is even, odd, or nil.

This rule is important because it improves the readability and maintainability of the code. It reduces verbosity and makes the intention of the code clearer to other developers. Explicitly comparing values using `==` can sometimes lead to confusion or errors, especially with `nil` checks.

To avoid violations of this rule, use the built-in predicate methods provided by Ruby whenever possible. For instance, instead of checking if a number is even with `num % 2 == 0`, use the `.even?` method like so: `num.even?`. Similarly, instead of checking if a variable is `nil` with `var == nil`, use the `.nil?` method: `var.nil?`. By following these practices, you can write cleaner and more idiomatic Ruby code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
if foo % 2 == 0
end

if bar % 2 == 1
end

if baz == nil
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
if foo.even?
end

if bar.odd?
end

if baz.nil?
end

if qux.zero?
end

if quux == 0
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
