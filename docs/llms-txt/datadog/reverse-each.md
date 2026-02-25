# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/reverse-each.md

---
title: Prefer using reverse_each
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using reverse_each
---

# Prefer using reverse_each

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/reverse-each`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer using `reverse_each`" is based on the principle of optimizing your Ruby code for better performance. In Ruby, there are two main methods for iterating over the elements of an array in reverse order: `reverse.each` and `reverse_each`. While the functionality of these two methods is the same, their performance characteristics are different.

The `reverse.each` method creates a new array that is the reverse of the original before performing the iteration. This can lead to unnecessary memory usage, especially for large arrays, and slow down the performance of your code.

On the other hand, the `reverse_each` method does not create a new array. Instead, it starts from the end of the original array and works its way to the beginning, saving memory and enhancing performance.

Therefore, to adhere to good coding practices and ensure optimal performance, it is recommended to use `reverse_each` instead of `reverse.each` when you need to iterate over the elements of an array in reverse order.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
array.reverse.each { }

["foo", "bar"].reverse.each { }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
array.reverse_each { }

["foo", "bar"].reverse_each { }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
