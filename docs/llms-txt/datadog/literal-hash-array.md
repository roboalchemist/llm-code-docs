# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/literal-hash-array.md

---
title: Avoid array and hash constructor when empty
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid array and hash constructor when empty
---

# Avoid array and hash constructor when empty

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/literal-hash-array`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Avoid array and hash constructor when empty" is an important practice in Ruby for creating empty arrays and hashes. It dictates that developers should use literal constructors `[]` for arrays and `{}` for hashes rather than `Array.new` and `Hash.new` when the array or hash being created is empty.

This rule is important because it promotes code readability and simplicity. The literal constructors `[]` and `{}` are concise, straightforward, and are commonly used in the Ruby community. Using these instead of `Array.new` and `Hash.new` makes the code easier to read and understand.

To adhere to this rule, always use `[]` to initialize an empty array and `{}` to initialize an empty hash. However, it is acceptable to use `Array.new` and `Hash.new` when you are initializing an array or hash with default values, as demonstrated in the compliant code example.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
foo = Array.new
bar = Hash.new
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
foo = []
bar = {}
# Okay since they contain values
baz = Array.new(42) 
qux = Hash.new(99)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 