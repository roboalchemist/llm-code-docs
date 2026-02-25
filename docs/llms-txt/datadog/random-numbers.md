# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/random-numbers.md

---
title: Prefer using ranges for random numbers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using ranges for random numbers
---

# Prefer using ranges for random numbers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/random-numbers`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Ruby, it's considered a better practice to use ranges when generating random numbers. This rule is important because it promotes the use of more idiomatic Ruby code and enhances readability. Using a range to generate a random number clearly shows the minimum and maximum values, which makes the code easier to understand.

Non-compliant code, such as `rand(42) + 1`, is less clear because it's not immediately obvious what the range of possible values is. This can lead to confusion and potential bugs in the code.

To follow this rule, use a range when generating random numbers. For example, `rand(1..42)` is a much clearer way of generating a random number between 1 and 42. This makes it obvious to anyone reading the code what the range of possible values is, thus improving the readability and maintainability of your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
rand(42) + 1
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
rand(1..42)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
