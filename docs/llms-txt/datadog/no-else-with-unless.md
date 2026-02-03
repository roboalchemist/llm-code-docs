# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-else-with-unless.md

---
title: Do not use unless with else
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use unless with else
---

# Do not use unless with else

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-else-with-unless`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule "Do not use unless with else" is a coding guideline that promotes clarity and readability in Ruby code. The `unless` keyword in Ruby is used as the inverse of `if`, meaning it executes the code block only if the condition is false. When an `else` statement is added to an `unless` statement, it can make the logic harder to follow and understand, especially for those new to the language or the codebase.

Why is this important? Readability and clarity are essential for maintaining a healthy codebase. Code is read more often than it is written, and it is crucial that it remains clear to all developers in a team. An `unless-else` construct can be confusing because it effectively double-negates the logic, making it harder to understand at a glance.

To avoid violating this rule, use an `if-else` construct instead. It conveys the same logic in a more straightforward manner. The `if-else` construct is also more common across different programming languages, making it easier for developers with different backgrounds to understand. For example, instead of writing `unless condition; else; end`, write `if !condition; else; end`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
unless success?
  puts 'failure'
else
  # foo
  puts 'success'
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
if success?
  puts 'failure'
else
  #foo
  puts 'success'
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 