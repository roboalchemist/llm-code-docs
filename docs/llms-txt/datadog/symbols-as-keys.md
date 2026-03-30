# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/symbols-as-keys.md

---
title: Use symbols instead of strings for hash keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use symbols instead of strings for hash keys
---

# Use symbols instead of strings for hash keys

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/symbols-as-keys`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Ruby, it is a best practice to use symbols instead of strings as hash keys. This rule emphasizes that it's more efficient and idiomatic to use symbols for this purpose. Symbols are immutable and unique, which makes them ideal for identifying things, whereas strings are mutable and can create multiple objects for the same sequence of characters.

The importance of this rule lies in the performance and memory usage of your Ruby application. Using symbols as hash keys reduces memory usage because they are stored in memory only once during a Ruby process. This can make a significant difference in the efficiency of your application, especially when dealing with large data sets.

To ensure you're following good coding practices, always use symbols for hash keys unless there's a specific reason to use a string. A simple refactoring from `values = { 'foo' => 42, 'bar' => 99, 'baz' => 123 }` to `values = { foo: 42, bar: 99, baz: 123 }` will make your code compliant with this rule. This not only improves your code's performance but also makes it more readable and consistent with Ruby's conventions.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
values = { 'foo' => 42, 'bar' => 99, 'baz' => 123 }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
values = { foo: 42, bar: 99, baz: 123 }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
