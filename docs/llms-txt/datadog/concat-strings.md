# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/concat-strings.md

---
title: Avoid slow string concatenation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid slow string concatenation
---

# Avoid slow string concatenation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/concat-strings`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule to avoid slow string concatenation in Ruby is essential for writing efficient and fast-performing code. String concatenation using the `+=` operator is slower because it creates a new string object every time it's used. This can lead to performance issues, especially in loops or large programs where numerous string concatenations might be happening.

Instead, the `<<` operator, also known as the append operator, should be used for string concatenation in Ruby. The `<<` operator modifies the original string, avoiding the creation of multiple unnecessary string objects. This results in faster execution time and lower memory usage, which is especially beneficial in larger applications or systems with limited resources.

Therefore, good coding practice in Ruby suggests using `<<` for string concatenation instead of `+=`. For instance, `output << "<p>#{text}</p>"` is more efficient than `output += "<p>#{text}</p>"`. Following this rule will help you write cleaner, faster, and more resource-efficient Ruby code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
output = ''
output += '<h1>Page title</h1>'
output += '<h3>Sub heading</h3>'

texts.each do |text|
  output += "<p>#{text}</p>"
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
output = ''
output << '<h1>Page title</h1>'
output << '<h3>Sub heading</h3>'

texts.each do |text|
  output << "<p>#{text}</p>"
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 