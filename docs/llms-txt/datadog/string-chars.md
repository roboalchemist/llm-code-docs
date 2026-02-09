# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/string-chars.md

---
title: Prefer string chars with empty string
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer string chars with empty string
---

# Prefer string chars with empty string

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/string-chars`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule is about preferring the use of the `chars` method over splitting a string with an empty string in Ruby. The `chars` method is a more idiomatic and efficient way to access the individual characters of a string in Ruby. Using `string.split('')` or `string.split(//)` to achieve this is less efficient and can lead to confusion, as the `split` method is typically used to divide a string into substrings based on a delimiter.

The importance of this rule lies in writing clear, efficient, and idiomatic Ruby code. When you use the `chars` method to access individual characters, your intent is clear to other developers who read your code. Additionally, the `chars` method is more efficient than `split('')` or `split(//)`, which can make a difference in performance when dealing with large strings.

To adhere to this rule and practice good coding, use the `chars` method whenever you need to access the individual characters of a string. For example, instead of `string.split('')`, use `string.chars`. If you need to split a string into substrings based on a delimiter, continue to use the `split` method with the appropriate delimiter, such as `string.split(' ')` to split on spaces. By doing so, your code will be more readable, efficient, and idiomatic.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
string.split(//)
string.split('')
string.split("")
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
string.chars
string.split("hello world")
string.split("hello world", " ")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 