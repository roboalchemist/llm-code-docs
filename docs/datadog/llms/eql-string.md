# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/eql-string.md

---
title: Do not use eql? for strings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use eql? for strings
---

# Do not use eql? for strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/eql-string`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Do not use eql? for strings" is a standard practice in Ruby programming. The `eql?` method in Ruby checks if two objects are of the same type and have the same value. While this may seem useful, it can lead to unexpected behavior when comparing strings.

This rule is important because using `eql?` to compare strings can lead to confusing and hard-to-debug issues. For instance, `eql?` will return false when comparing a string to a symbol with the same characters, even though they might seem equivalent to a human reader.

To avoid violating this rule, it is recommended to use the `==` operator when comparing strings. The `==` operator in Ruby compares the values of two objects for equality, and is more intuitive for string comparisons. For example, instead of writing `'ruby'.eql? some_str`, you should write `'ruby' == some_str`. This will help to avoid potential confusion and make your code more readable and maintainable.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
'ruby'.eql? some_str
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
'ruby' == some_str
1.0.eql?
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
