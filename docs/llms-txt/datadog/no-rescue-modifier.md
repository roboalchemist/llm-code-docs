# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-rescue-modifier.md

---
title: Avoid using 'rescue' as a modifier
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using 'rescue' as a modifier
---

# Avoid using 'rescue' as a modifier

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-rescue-modifier`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule emphasizes the importance of not using 'rescue' as a modifier in your code. Using 'rescue' as a modifier can lead to confusion and potential bugs in the code. This is because it can catch exceptions you did not intend to catch and miss the ones you intended to catch. Hence, it's considered a bad practice.

The importance of this rule lies in ensuring the clarity and correctness of your error handling code. When 'rescue' is used as a modifier, it can catch `StandardError` and its subclasses by default. This can lead to unexpected behavior if you intended to catch a different exception.

Good coding practices to avoid this rule violation include explicitly stating the exception you are trying to catch, and using 'rescue' in a begin-end block instead of as a modifier. This makes your code easier to understand and less prone to bugs. For example, instead of writing `foo = a[x] rescue nil`, write:

```ruby
begin
  foo = a[x]
rescue IndexError
  foo = nil
end
```

This way, it's clear that you are trying to rescue `IndexError`, and not any other kind of error.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
foo = a[x] rescue nil

something rescue handle_error

# This is a common mistake: it doesn't capture SomeException.
# It captures StandardError and names the variable `SomeException`.
anything rescue SomeException
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
try
  foo = a[x]
rescue IndexError
  foo = nil
end

try
  something
rescue StandardError
  handle_error
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 