# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-then.md

---
title: 'Do not use `then` for multi-line if/unless/when/in '
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use `then` for multi-line if/unless/when/in
---

# Do not use `then` for multi-line if/unless/when/in

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-then`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `then` keyword is not necessary in multi-line `if/unless/when/in` statements in Ruby. When used in multi-line statements, it can make the code harder to read and understand. This is because `then` is typically associated with single-line conditional statements in Ruby, and its use in multi-line statements can be confusing.

Maintaining readability and clarity in your code is crucial for effective collaboration and debugging. It becomes even more important in larger codebases, where complex logic can become difficult to follow if not written clearly.

To avoid this issue, omit the `then` keyword in your multi-line `if/unless/when/in` statements. For single-line `if/unless/when/in` statements, using `then` is acceptable and can help improve readability. This practice keeps your code clean and easy to understand, following the principles of good coding practices.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
if condition then
  do_something
end

case expression
when condition then
  do_something
end

case expression
in pattern then
  do_something
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
case value
when Array then new(*value)
# Some comment
end
```

```ruby
if condition
  do_something()
end

case expression
when condition
  do_something()
end

case expression
in pattern
  do_something()
end

if condition then do_something end

case type
when 'foo' then do_action(action_params)
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 