# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/array-coercion.md

---
title: ' Use `Array()` to ensure your variable is an array'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use `Array()` to ensure your variable is an array
---

# Use `Array()` to ensure your variable is an array

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/array-coercion`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Use `Array()` to ensure your variable is an array" is important for ensuring your code behaves as expected, regardless of the type of data it receives. It is common in Ruby to need to iterate through an array of items. However, if the variable is not an array, this can lead to unexpected behavior or errors.

The `Array()` method in Ruby is a Kernel method that converts its argument to an Array. If the argument is already an Array, it returns the argument. If the argument is nil, it returns an empty Array. This can be used to ensure that a variable is an array before trying to iterate over it, preventing potential errors or unexpected behavior.

By using `Array(foos)`, you can ensure that `foos` is an array before you try to iterate over it with `each`. This prevents the need to check if `foos` is an array with `foos.is_a?(Array)` and makes your code cleaner and easier to understand.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
foos = [foos] unless foos.is_a?(Array)
foos.each { |path| do_bar(path) }

# this would always create a new Array instance
[*foos].each { |foo| do_bar(foo) }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
Array(foos).each { |foo| do_bar(foo) }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
