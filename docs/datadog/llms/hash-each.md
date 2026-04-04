# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/hash-each.md

---
title: Prefer using hash each_key and each_value
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using hash each_key and each_value
---

# Prefer using hash each_key and each_value

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/hash-each`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer using hash each_key and each_value" recommends using the specific iterator methods `each_key` and `each_value` when iterating over the keys or values of a hash. It is considered a best practice in Ruby to use these methods instead of the more general `each` method followed by `keys` or `values`.

This rule is important because it helps to improve the readability and clarity of your code. When you use `each_key` or `each_value`, it's immediately clear that you're working with either the keys or the values of the hash. This makes your code easier to understand and maintain.

To follow this rule, you should replace any instances of `hash.keys.each` with `hash.each_key`, and `hash.values.each` with `hash.each_value`. This will make your code more idiomatic and easier to read, while still achieving the same functionality.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
# Updates the method
hash.keys.each { |k| p k }
hash.keys.each do |k| p k end

hash.values.each { |v| p v }
hash.values.each do |v| p v end

# Updates the method and parameters
hash.each { |k, _v| p k }
hash.each do |k, _v| p k end

hash.each { |_k, v| p v }
hash.each do |_k, v| p v end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
hash.each_key { |k| p k }
hash.each_value { |v| p v }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
