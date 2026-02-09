# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/lambda-parameters.md

---
title: Ensure lambdas have parenthesis around parameters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure lambdas have parenthesis around parameters
---

# Ensure lambdas have parenthesis around parameters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/lambda-parameters`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule ensures that lambdas in your Ruby code have parenthesis around their parameters. Lambdas are anonymous functions that are objects, allowing them to be stored in variables and passed around. The syntax for defining a lambda in Ruby is `->(parameters) { body }`. When the parenthesis around parameters are omitted, it might lead to unexpected behavior and bugs, especially when dealing with multiple parameters.

The importance of this rule lies in its ability to prevent potential confusion and errors that could occur from misinterpretation of the code. It enhances the readability and maintainability of your code. This is especially significant in large codebases where clarity is crucial for efficient collaboration and debugging.

To adhere to this rule, always include parenthesis around the parameters when defining a lambda. For example, instead of writing `l = ->x, y { something(x, y) }`, write it as `l = ->(x, y) { something(x, y) }`. This practice will make your code safer and easier to understand, ultimately leading to better software quality.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
l = ->x, y { something(x, y) }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
l = ->(x, y) { something(x, y) }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 