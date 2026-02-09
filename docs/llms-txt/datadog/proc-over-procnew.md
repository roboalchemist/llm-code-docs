# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/proc-over-procnew.md

---
title: Prefer proc over Proc.new
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer proc over Proc.new
---

# Prefer proc over Proc.new

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/proc-over-procnew`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer proc over Proc.new" is an important guideline in Ruby programming. It advises developers to use the `proc` method rather than `Proc.new` when creating a new Proc object. The `proc` method is more idiomatic to Ruby and is preferred because of its simplicity and readability.

The importance of this rule lies in maintaining consistency and clarity in your code. Using `proc` instead of `Proc.new` makes your code more concise and easier to read and understand. It also aligns with the Ruby community's best practices, which favor simplicity and readability.

To avoid violating this rule, always use `proc` when you need to create a new Proc object. For example, instead of writing `Proc.new { |n| puts n }`, you should write `proc { |n| puts n }`. This small change can significantly improve the readability of your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
p = Proc.new { |n| puts n }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
p = proc { |n| puts n }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 