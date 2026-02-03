# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-nested-method.md

---
title: Prevent nested method
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent nested method
---

# Prevent nested method

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-nested-method`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The Ruby static analysis rule "Prevent nested method" discourages defining a method within another method. This practice is generally discouraged in Ruby because the inner method is not actually defined within the scope of the outer method as one might expect, but rather in the same scope as the outer method. This can lead to unexpected behavior and make code more difficult to understand and maintain.

This rule is important because it promotes good coding practices and helps to prevent potential bugs. Nested methods can lead to confusing code and unintended side effects, making your code more difficult to debug and maintain. Furthermore, nested methods are not a common practice in Ruby and can be surprising to other developers who read your code.

To avoid violating this rule, define all methods at the same level of scope. Instead of defining a method within another method, define each method separately and call them as needed. If you find that you are frequently defining methods within other methods, it may be a sign that your code could be structured more effectively, for example by using classes or modules.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def foo(x)
  def bar(y)
  end

  bar(x)
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
def bar(y)
end

def foo(x)
  bar(x)
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 