# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/double-colon-method-calls.md

---
title: Use double colons only to reference constants
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use double colons only to reference constants
---

# Use double colons only to reference constants

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/double-colon-method-calls`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Ruby, double colons `::` are used as a namespace resolution operator that allows you to reference constants, including classes and modules, from within different scopes. This rule emphasizes that you should only use double colons to reference these constants.

Using double colons for methods or variables can lead to confusion and unexpected behavior because it deviates from the standard Ruby syntax. It's important to use the correct operators for clarity and to maintain consistency in your code.

To avoid violating this rule, always use a dot `.` when you want to call a method on an object or class. If you want to reference a constant, use double colons `::`. By following these guidelines, your code will be more readable and easier to understand.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
SomeClass::some_method
some_object::some_method
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
SomeClass.some_method
some_object.some_method
SomeModule::SomeClass::SOMETHING
SomeModule::SomeClass()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 