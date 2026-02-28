# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/class-methods.md

---
title: Use self to define class methods
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use self to define class methods
---

# Use self to define class methods

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/class-methods`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Ruby, it is a good practice to use `self` to define class methods. This is because `self` inside a class or module definition refers to the class or module itself. Thus, when you define a method with `self`, you're actually defining a class method.

Using `self` is important for a couple of reasons. First, it makes your code more readable and easier to understand. When someone else reads your code, they can immediately understand that the method is a class method. Second, it prevents potential conflicts with instance methods that have the same name.

To avoid violations of this rule, always use `self` to define class methods. For example, instead of writing `def ClassName.method_name`, you should write `def self.method_name`. You can also use the `class << self` syntax to define multiple class methods at once. This syntax opens up the class's singleton class, which is where Ruby stores class methods. This can make your code cleaner and more organized, especially when you have many class methods.

For example:

```ruby
class MyClass
  class << self
    def first_method
      # code
    end

    def second_method
      # code
    end
  end
end
```

In this example, `first_method` and `second_method` are both class methods.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class TestClass
  def TestClass.some_method
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class TestClass
  def self.some_other_method
  end
end
```

```ruby
  class << self
    def first_method
    end

    def second_method_etc
    end
  end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
