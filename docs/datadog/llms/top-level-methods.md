# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/top-level-methods.md

---
title: Organize methods in modules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Organize methods in modules
---

# Organize methods in modules

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/top-level-methods`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule emphasizes the importance of organizing methods within modules or classes in Ruby. In Ruby, it's considered a best practice to wrap methods within classes or modules. This is because it helps in grouping related methods together, which in turn makes the code easier to understand, maintain, and reuse.

Not adhering to this rule can lead to a disorganized codebase, making it hard for other developers to understand and maintain the code. It can also lead to potential name clashes if a method is defined in the global scope.

To avoid violating this rule, always define your methods within a class or a module. For example, instead of writing `def some_method; end`, you should write `class SomeClass def some_method; end end`. This not only adheres to the rule but also improves the readability and maintainability of your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def some_method; end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class SomeClass
  def some_method; end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
