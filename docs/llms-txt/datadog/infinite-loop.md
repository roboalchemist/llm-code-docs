# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/infinite-loop.md

---
title: Use Kernel#loop instead of while/until
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use Kernel#loop instead of while/until
---

# Use Kernel#loop instead of while/until

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/infinite-loop`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The Ruby static analysis rule "Use Kernel#loop instead of while/until" focuses on promoting the use of `Kernel#loop` for infinite loops rather than `while true` or `until false`. This is because `Kernel#loop` is more idiomatic to Ruby, and it communicates the intent of an infinite loop more clearly. This rule helps to maintain readability, which is crucial in large codebases where understanding the flow and function of the code is important.

The `while true` or `until false` expressions can be misleading as they suggest a condition that might change, even though they are used to create infinite loops. Using `Kernel#loop` eliminates this ambiguity, making the code easier to understand.

To adhere to this rule, replace any `while true` or `until false` loops with `Kernel#loop`. The body of the loop remains the same. This small change can significantly improve the clarity of the code, making it more understandable for other developers who might work on the same codebase.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
while true
  do_something
end

until false
  do_something
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
loop do
  do_something
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
