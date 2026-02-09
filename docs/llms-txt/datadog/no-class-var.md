# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-class-var.md

---
title: Avoid class variables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid class variables
---

# Avoid class variables

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-class-var`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule "Avoid class variables" refers to the practice of refraining from using class variables (variables starting with '@@') in Ruby. Class variables are shared between a class and all of its descendants, which can lead to unexpected behavior and bugs that are difficult to trace. This is because if a class variable is changed in a subclass, that change will also affect the superclass and all other subclasses.

This rule is crucial for maintaining clean, predictable, and easy-to-debug code. It also helps to prevent unintentional side effects that can occur when class variables are manipulated in different parts of a program.

To adhere to this rule, consider using class instance variables or constants instead. Class instance variables belong solely to the class they are defined in, and their value does not get shared with subclasses. Constants, on the other hand, are a good option when the value is not meant to change. For example, in the given non-compliant code, the class variable `@@class_var` could be replaced with a class instance variable `@class_var` or a constant `CLASS_VAR`, depending on the intended use.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class Parent
    @@class_var = 'parent'
    foo = bar

    def self.print_class_var
        puts @@class_var
    end
end

class Child < Parent
    @@class_var = 'child'
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 