# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/condition-safe-alignment.md

---
title: Wrap assignment in condition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Wrap assignment in condition
---

# Wrap assignment in condition

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/condition-safe-alignment`

**Language:** Ruby

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The rule "Wrap assignment in condition" is designed to avoid a common programming bug where a single equals sign (`=`) is used in a conditional statement instead of a double equals sign (`==`). This can lead to unexpected behavior because the single equals sign is used for assignment in Ruby, not for comparison.

This is important because using assignment in a conditional statement can lead to code that is hard to read and understand. It can also lead to bugs if the assignment is unintentional. The assignment will always return a truthy value unless the assigned value is `nil` or `false`, which may not be the expected behavior.

To avoid violating this rule, always use double equals (`==`) for comparison in conditional statements. If you need to assign a value and use it in the condition, you should do the assignment outside of the conditional statement. If you must do the assignment inside the condition, wrap the assignment in parentheses to make it clear that the assignment is intentional. This improves code readability and helps prevent bugs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
if v = array.grep(/foo/)
  do_something(v)
  # some code
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
if (v = array.grep(/foo/))
  do_something(v)
  # some code
end

v = array.grep(/foo/)
if v
  do_something(v)
  # some code
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
