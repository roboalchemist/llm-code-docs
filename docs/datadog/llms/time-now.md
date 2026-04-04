# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/time-now.md

---
title: Prefer `Time.now` over `Time.new`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer `Time.now` over `Time.new`
---

# Prefer `Time.now` over `Time.new`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/time-now`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer `Time.now` over `Time.new`" is a best practice in Ruby programming. `Time.new` without arguments returns the current time but it's less descriptive than `Time.now`. Using `Time.now` helps to improve the readability of your code by explicitly stating that you are getting the current time.

This rule is important because clear and readable code is essential for maintenance and collaboration. When other developers read your code, they should be able to understand it easily. Using `Time.now` instead of `Time.new` for the current time makes your code more self-explanatory.

To avoid this violation, always use `Time.now` when you want to get the current time. Use `Time.new` only when you need to create a time object for a specific date and time. For example, `Time.new(2024, 2, 29, 12, 0, 0, "+00:00")` creates a time object for February 29, 2024, at noon UTC.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
current_time = Time.new
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
current_time = Time.now
rule_creation_time = Time.new(2024, 2, 29, 12, 0, 0, "+00:00")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
