# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-end-blocks.md

---
title: Avoid using END blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using END blocks
---

# Avoid using END blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-end-blocks`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule of avoiding `END` blocks in Ruby is important due to the nature of how such blocks are executed. Unlike `at_exit` blocks, `END` blocks are run whenever the program exits, regardless of whether it's a normal termination or due to an unhandled exception. This can lead to unpredictable behavior and makes debugging more difficult.

The use of `END` blocks also makes your code less readable and harder to maintain. It's not immediately clear when or why these blocks are executed, and they can easily be overlooked when reading through the code. This can lead to unexpected side effects and bugs.

To adhere to this rule, use `at_exit` blocks instead of `END` blocks. This ensures that the block is only executed when the program exits normally, making your code more predictable and easier to debug. Also, consider structuring your code in a way that avoids the need for such blocks in the first place. This will make your code cleaner and easier to understand. For instance, instead of using `END` to perform cleanup tasks, you can use a `begin/rescue/ensure` block or make sure that resources are released as soon as they are no longer needed.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
END { puts("end") }
END {puts("end")}
END {
  puts("end")
}
END
{
  puts("end")
}
END {}

puts("begin")
my_str = begin
  a = "more "
  b = "things"
  a + b
end
puts(my_str)
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
at_exit { puts("end") }
at_exit {puts("end")}
at_exit {
  puts("end")
}
at_exit
{
  puts("end")
}
at_exit {}

puts("begin")
my_str = begin
  a = "more "
  b = "things"
  a + b
end
puts(my_str)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 