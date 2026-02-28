# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-extend-struct-new.md

---
title: You should not inherit from Struct.new
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > You should not inherit from Struct.new
---

# You should not inherit from Struct.new

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-extend-struct-new`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule, "You should not inherit from `Struct.new`", is important because it can lead to unexpected behavior and bugs in your code. `Struct.new` creates a new Class, and if you inherit from it, you're creating a subclass of a dynamically generated Class. This can lead to confusing code and can make debugging difficult.

Instead of inheriting from `Struct.new`, you should assign the result of `Struct.new` to a constant. This will create a new Class with the provided attributes, and you can add methods to it just like any other Class. This approach is clearer and less prone to errors.

To avoid this, use `Struct.new` to create a new class and assign it to a constant. For example, `Foo = Struct.new(:foo, :bar)` creates a new Class with two attributes, `foo` and `bar`, and assigns it to the constant `Foo`. This is a far safer and more predictable way to use `Struct.new` in your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class Foo < Struct.new(:foo, :bar)
end

class Foo < Struct.new(:foo, :bar)
  def thing
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
Foo = Struct.new(:foo, :bar)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
