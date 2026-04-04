# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/hash-literals.md

---
title: Use new syntax when keys are symbols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use new syntax when keys are symbols
---

# Use new syntax when keys are symbols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/hash-literals`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Use new syntax when keys are symbols" is a coding standard in modern Ruby development. It encourages the use of the new hash syntax, introduced in Ruby 1.9, where symbols are used as keys. The old hash rocket syntax (`:symbol => value`) is replaced with the more elegant and succinct `symbol: value` syntax.

This rule is important as it promotes a cleaner, more readable code. The new syntax is more concise and less cluttered, making it easier to understand the structure and purpose of the hash. This is particularly beneficial in large codebases or when hashes are nested or complex.

To adhere to this rule, always use the new syntax when defining hashes where keys are symbols. Instead of defining a hash with `:symbol => value`, use `symbol: value`. This approach will not only make your code more readable but also ensure consistency across your codebase.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
values = { :foo => 42, :bar => 99, :baz => 123 }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
values = { foo: 42, bar: 99, baz: 123 }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
