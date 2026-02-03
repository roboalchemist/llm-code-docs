# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/case-vs-if-elsif.md

---
title: Prefer case over if-elsif
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer case over if-elsif
---

# Prefer case over if-elsif

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/case-vs-if-elsif`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer case over if-elsif" is an important guideline for writing cleaner and more readable code in Ruby. The `case` statement is a multi-way branch statement, similar to `if-elsif-else`, but it is more concise and clear, especially when comparing a variable to multiple values. It improves the readability of your code and makes it easier to understand and maintain.

The importance of this rule lies in the fact that complex `if-elsif-else` chains can be difficult to read and understand. It can lead to confusion and increase the chances of introducing bugs in your code. On the other hand, using `case` makes your code more structured and logical, which is particularly helpful when dealing with multiple conditions.

To avoid violating this rule, you should use `case` instead of `if-elsif` whenever you are comparing a variable to multiple different values. In the `case` statement, you can specify multiple conditions in a more organized manner. If the conditions are not about the same variable or comparison, `if-elsif` might still be more appropriate.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
if status == :published
  do_something
elsif status == :draft || status == :pending_approval
  do_option_one
else
  do_option_two
end

if status == :published
  do_something
elsif status == :draft
  do_option_one
else
  do_option_two
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
case status
when :published
  do_something
when :draft, :pending_approval
  do_option_one
else
  do_option_two
end

if status == :published
  do_something
elsif status != :draft
  do_option_one
else
  do_option_two
end

if status1 == :published
  do_something
elsif status2 == :draft
  do_option_one
else
  do_option_two
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 