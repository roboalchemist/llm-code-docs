# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-begin-blocks.md

---
title: Avoid using BEGIN blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using BEGIN blocks
---

# Avoid using BEGIN blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-begin-blocks`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `BEGIN` blocks in Ruby are used to specify pieces of code that should be run before the program is run. These blocks are usually executed before any other code in the current file.

Although `BEGIN` blocks can be useful in certain situations, they can also lead to code that is harder to understand and maintain. This is because `BEGIN` blocks can create unexpected side effects, especially when they are used in larger codebases where they can be easily overlooked.

To avoid using `BEGIN` blocks, you can often move the code to the top of the file, or into a method or function that is explicitly called. This makes the code more explicit, easier to read, and less prone to unexpected side effects. If you need to perform setup steps before running your code, consider using a setup method or function instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
puts("Running")

BEGIN { puts("Beginning")}

my_str = begin
  a = "another "
  b = "block"
  a + b
end
puts(my_str)
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
puts("Beginning")

puts("Running")

my_str = begin
  a = "another "
  b = "block"
  a + b
end
puts(my_str)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
