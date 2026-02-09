# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/string-interpolation.md

---
title: Avoid string concatenation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid string concatenation
---

# Avoid string concatenation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/string-interpolation`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Avoid string concatenation" is an important coding practice in Ruby for ensuring efficient and clean code. String concatenation in Ruby using the '+' operator creates a new string object, which can lead to excessive memory usage and slower performance when dealing with large strings or performing the operation multiple times.

Instead, Ruby provides alternatives that are more efficient. The string interpolation syntax `#{}` allows you to insert variables directly into strings without creating new string objects. This is not only more memory efficient, but also provides cleaner and more readable code.

Another alternative is the `format` method, which allows you to create a formatted string with placeholders for variables. This method is particularly useful when dealing with more complex strings, as it provides a clear and concise way to format your strings.

By following this rule, you can write more efficient and cleaner Ruby code, leading to better performance and readability.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
str1 = "Hello"
str2 = "world!"
result = str1 + " " + str2

foo = str1 + "bla"
foo = "bla" + str1
foo = "bla" + bar(baz)
foo = "bli" | str1
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
str1 = "Hello"
str2 = "world!"
resultA = "#{str1} <#{str2}>"
resultB = format('%s <%s>', str1, str2)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 