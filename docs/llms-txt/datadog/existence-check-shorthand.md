# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/existence-check-shorthand.md

---
title: Use &&= to check if a variable may exist
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use &&= to check if a variable may exist
---

# Use &&= to check if a variable may exist

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/existence-check-shorthand`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The `&&=` operator in Ruby is a conditional assignment operator that checks if a variable is truthy (not `nil` or `false`). If the variable is truthy, it assigns the value on the right side of the operator to the variable. This rule emphasizes the importance of using this operator to avoid unnecessary checks and potential errors in your code.

It is important to use `&&=` operator to ensure your code is efficient and clean. Using this operator can help to avoid unnecessary conditional checks and keep your code concise. More importantly, it can prevent potential `nil` errors which are common in Ruby when trying to call a method on a `nil` object.

To follow this rule, use `&&=` operator when you need to check if a variable may exist and assign a value to it. For example, instead of doing `if foo; bar = foo.something; end`, you can do `bar &&= foo.something`. This will assign `foo.something` to `bar` only if `bar` is not `nil` or `false`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
if foo
     bar = foo.something
end

if foo
     bar = foo.something
else
     bar = foo.something_else
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
bar &&= foo.something

if foo
     bar = foo.something
else
     bar = foo.something_else
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
