# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/exception-class-message-separate.md

---
title: Separate the exception class and the message
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Separate the exception class and the message
---

# Separate the exception class and the message

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/exception-class-message-separate`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule requires that the exception class and the message be separated in the raise statement. This is important because it makes the code more readable and easier to understand. It also helps to avoid potential syntax errors or unexpected behavior.

When you combine the exception class and the message into a single object, it can be confusing to other developers who are trying to understand your code. It may not be immediately clear what type of exception is being raised, or what the associated message is.

To comply with this rule, separate the exception class and the message with a comma when you raise an exception. For example, instead of writing `raise SomeException.new('message')`, you should write `raise SomeException, 'message'`. This makes it clear that you are raising a `SomeException` and that the associated message is 'message'. It also makes your code more consistent with common Ruby coding conventions.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
raise SomeException.new('message')
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
raise SomeException, 'message'
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
