# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-suppress-exceptions.md

---
title: Do not suppress exceptions without a comment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not suppress exceptions without a comment
---

# Do not suppress exceptions without a comment

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-suppress-exceptions`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Do not suppress exceptions without a comment" is a guideline that helps in maintaining the readability, debuggability, and maintainability of your code. When an exception is silently suppressed, it can lead to confusion for other developers who later maintain the code, as it may not be clear why the exception is being ignored. This can also hide potential issues in your code which might lead to bugs that are difficult to diagnose.

This rule is important because exceptions are generally a sign of an unexpected condition or error in your code. Ignoring them without any explanation can lead to hidden bugs and make your code harder to understand and maintain. It can also lead to incorrect behavior of your application, as the exception may be signaling a condition that needs to be handled.

To avoid violating this rule, always handle exceptions in your rescue block, or if you are intentionally suppressing an exception, clearly document the reason with a comment. This way, other developers will understand why the exception is being ignored. For example, you can handle the exception by logging it or by executing some fallback code. If you are suppressing the exception because it's expected and safe to ignore, explain why this is the case in a comment. For example: `rescue SomeError # We expect this error and it's safe to ignore because...`. This will make your code easier to understand and maintain.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
begin
  do_something
rescue SomeError
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
begin
  do_something
rescue SomeError
  handle_exception
end

begin
  do_something
rescue SomeError
  # Why we do nothing
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 