# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/integer-type-checking.md

---
title: Enforce using Integer to check the type of an integer number
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce using Integer to check the type of an integer number
---

# Enforce using Integer to check the type of an integer number

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/integer-type-checking`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule enforces the use of the `Integer` class when performing type checking on integer numbers in Ruby. This is important because, in Ruby, integers can be either `Fixnum` or `Bignum` depending on their size. However, both `Fixnum` and `Bignum` are subclasses of `Integer`, making `Integer` the most appropriate class to use when checking if a number is an integer.

Using `Integer` for type checking increases the readability and maintainability of your code. It avoids the need to check for both `Fixnum` and `Bignum` separately, which can lead to redundant and cluttered code. Additionally, using `Integer` for type checking ensures that your code will continue to work correctly if Ruby changes its implementation of integer numbers in the future.

To abide by this rule and maintain good coding practices, always use `Integer` when checking if a number is an integer. Instead of writing `num.is_a?(Fixnum)` or `num.is_a?(Bignum)`, write `num.is_a?(Integer)`. This ensures your code is succinct, easily understandable, and robust against potential changes in Ruby's integer implementation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
timestamp.is_a?(Fixnum)
timestamp.is_a?(Bignum)
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
timestamp.is_a?(Integer)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
