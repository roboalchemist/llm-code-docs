# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/lambda-no-parameter.md

---
title: Omit parentheses if a lambda has no parameter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Omit parentheses if a lambda has no parameter
---

# Omit parentheses if a lambda has no parameter

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/lambda-no-parameter`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Ruby, lambda is a function object that is created with the `->` operator. The rule states that if a lambda function does not take any parameters, parentheses should be omitted. This is due to the Ruby style guide, which promotes cleaner and more readable code.

This rule is important because consistency in coding style makes the code easier to understand and maintain. Unnecessary parentheses can add clutter to the code and may lead to confusion. By omitting parentheses in lambdas with no parameters, the code becomes more streamlined and readable.

To adhere to this rule, write your lambda without parentheses if it doesn't require any parameters. For example, instead of writing `->() { something }`, you should write `-> { something }`. This makes it clear that the lambda takes no arguments, and helps maintain a consistent and clean coding style.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
l = ->() { something }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
l = -> { something }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 