# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-return-ensure.md

---
title: Do not return from an ensure block
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not return from an ensure block
---

# Do not return from an ensure block

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-return-ensure`

**Language:** Ruby

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The rule 'Do not return from an ensure block' in Ruby is essential as it helps to maintain the execution flow of the program. The ensure block is designed to always execute, regardless of whether an exception is raised. Its primary purpose is to house cleanup code that needs to run under all circumstances, such as closing files or network connections.

Returning from an ensure block can lead to unpredictable program behavior. It can prematurely exit a method or function, potentially bypassing important code and making it difficult to trace the program's flow. It may also cause exceptions not to be handled properly, leading to unanticipated crashes or bugs.

To avoid violating this rule, ensure that your cleanup code does not contain a return statement. If a method or function needs to return a value, place the return statement outside of the ensure block. If you need to handle exceptions, use a rescue block. This will allow you to manage exceptions and ensure that cleanup code is always executed, without disrupting the normal flow of the program.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def foo
  do_something_that_can_raise
ensure
  do_cleanup
  return self
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
def foo
  do_something_that_can_raise
  self
ensure
  critical_cleanup
end

def foo
  begin
    do_something_that_can_raise
  rescue StandardError => e
    # Handle exception
  end
  self
ensure
  critical_cleanup
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 