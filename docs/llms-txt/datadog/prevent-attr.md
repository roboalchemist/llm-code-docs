# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/prevent-attr.md

---
title: Avoid attr
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid attr
---

# Avoid attr

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/prevent-attr`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The `attr` method in Ruby is an older method that was commonly used before `attr_accessor`, `attr_reader`, and `attr_writer` were introduced. It is now considered best practice to use these newer methods instead of `attr` for better clarity and consistency in your code.

The `attr` method can lead to confusion because it behaves differently depending on the number and type of arguments passed to it. If it is passed one argument, it behaves like `attr_reader`, creating a getter method for an instance variable. If it is passed two arguments, with the second argument being `true`, it behaves like `attr_accessor`, creating both a getter and a setter method. This can lead to unexpected behavior if not used carefully.

To adhere to this rule and avoid confusion, always use `attr_accessor` to create both getter and setter methods, `attr_reader` to create only getter methods, and `attr_writer` to create only setter methods. This will make your code more readable and maintainable. Avoid using `attr` altogether. For example, instead of writing `attr :something, true`, write `attr_accessor :something`. Instead of `attr :one, :two, :three`, write `attr_reader :one, :two, :three`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class Something
    attr :something, true
    attr :one, :two, :three
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class Something
    attr_accessor :something
    attr_reader :one, :two, :three
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
