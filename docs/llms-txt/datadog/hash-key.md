# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/hash-key.md

---
title: Prefer using hash key and value
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using hash key and value
---

# Prefer using hash key and value

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/hash-key`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer using hash key and value" encourages the use of the `key?` and `value?` methods when working with Ruby hashes, as opposed to the older `has_key?` and `has_value?` methods. These older methods are considered deprecated and may not be supported in future versions of Ruby.

This rule is important because it promotes the use of more modern, clean, and efficient Ruby syntax. By using `key?` and `value?`, your code will be more readable and maintainable, and you'll avoid potential issues with deprecated methods in future Ruby versions.

To adhere to this rule, replace any instances of `has_key?` with `key?` and `has_value?` with `value?` in your Ruby code. For example, instead of `hash.has_key?(:test)`, you should use `hash.key?(:test)`. Similarly, replace `hash.has_value?(value)` with `hash.value?(value)`. By following these practices, your Ruby code will be more modern, efficient, and future-proof.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
hash.has_key?(:test)
hash.has_value?(value)
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
hash.key?(:test)
hash.value?(value)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 