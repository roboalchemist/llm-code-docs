# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-extend-data-define.md

---
title: Do not extend Data.define
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not extend Data.define
---

# Do not extend Data.define

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-extend-data-define`

**Language:** Ruby

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The rule "Do not extend `Data.define`" is an important guideline in Ruby programming. `Data.define` is a method used to define a data type with specified fields, and it returns an anonymous class. Extending this anonymous class can lead to unpredictable behaviors and complications in your code, making it less maintainable and potentially introducing bugs.

It's important because extending `Data.define` can lead to a lack of clarity about the hierarchy and structure of your classes. In addition, this practice can make the code more difficult to read and understand for other developers, thereby reducing the code's maintainability.

Good coding practice dictates that you should avoid extending `Data.define`. Instead, you can assign the result of `Data.define` to a constant, and use this constant where needed in your code. For example, instead of writing `class MyClass < Data.define(:field1, :field2)`, you should write `MyClass = Data.define(:field1, :field2)`. This way, `MyClass` will be a clearly defined data type with the specified fields, and the code will be more readable and maintainable.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class MyClass < Data.define(:field1, :field2)
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
value = Data.define(:first_name, :last_name)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
