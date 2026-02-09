# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-rescue-exception.md

---
title: Do not rescue the Exception class
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not rescue the Exception class
---

# Do not rescue the Exception class

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-rescue-exception`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Do not rescue the Exception class" is a crucial practice in Ruby programming for handling exceptions. The Exception class is the root of Ruby's exception hierarchy, so when you rescue Exception, you're potentially catching and handling severe system errors that Ruby itself is trying to bubble up. These could be fundamental issues like memory overflows and syntax errors, which could cause the program to behave unexpectedly or even crash.

Rescuing the Exception class can lead to major problems in debugging since it can hide the true nature of the error and its source. It makes it harder to pinpoint where and why the error occurred. This can lead to significant delays in identifying and resolving coding issues.

Instead of rescuing the Exception class, it is better to rescue more specific error classes or use `StandardError` which is the superclass for most error types. For instance, if you're expecting possible nil values, use `rescue NoMethodError`. This allows Ruby to handle severe system errors appropriately and ensures that you're only rescuing the errors you expect. This practice makes your code safer, more predictable, and easier to maintain and debug.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
begin
  # The exit will be rescued, so the program won't exit.
  exit
rescue Exception
  # You are here!
end

begin
  # The exit will be rescued, so the program won't exit.
  exit
rescue Exception => e
  # You are still here!
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
begin
  exit
rescue StandardError
  # Not reached
end

begin
  exit
rescue StandardError => e
  # Not reached either
end

begin
  exit
rescue => e
  # Equivalent to the above.
  # Does not rescue Exception, but StandardError.
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 