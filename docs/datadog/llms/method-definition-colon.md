# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/method-definition-colon.md

---
title: 'Do not use :: to define class methods'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use :: to define class methods
---

# Do not use :: to define class methods

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/method-definition-colon`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule refers to the naming convention of class methods in Ruby. It emphasizes not using the string '::' to define class methods. This is because it's not a valid method name in Ruby and will result in a syntax error.

Using standard naming conventions is crucial for code readability and maintainability. It's important to name methods in a clear and descriptive way, following the standards of the Ruby community. Using a string like '::' as a method name is not meaningful, descriptive, or standard.

To avoid this rule violation, always define class methods by using the 'self' keyword followed by a meaningful method name. For instance, `def self.my_method` is a standard way to define a class method in Ruby. This approach not only makes the code more readable but also helps other developers understand the purpose of the method easily.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class TestClass
  def self::my_method
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class TestClass
  def self.my_method
  end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
