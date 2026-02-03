# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/rails-best-practices/write-attribute.md

---
title: Prefer using self over write attribute
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using self over write attribute
---

# Prefer using self over write attribute

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `rails-best-practices/write-attribute`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule promotes the use of `self` over the ActiveRecord method `write_attribute`. This rule is important because using `self` to assign attributes is more idiomatic in Ruby and leads to cleaner, more readable code.

The `write_attribute` method in Rails is not recommended for regular use. It bypasses the normal attribute assignment process, skipping validations and callbacks. This can result in unexpected behavior and difficult-to-debug errors.

To avoid violating this rule, simply use `self[:attribute] = value` instead of `write_attribute(:attribute, value)`. For example, you can replace `write_attribute(:price, 42)` with `self[:price] = 42`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class Product < ApplicationRecord
  def price
    write_attribute(:price, 42)
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class Product < ApplicationRecord
  def price
    self(:price, 42)
  end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 