# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/rails-best-practices/read-attribute.md

---
title: Prefer using self over read attribute
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using self over read attribute
---

# Prefer using self over read attribute

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `rails-best-practices/read-attribute`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of `self` instead of `read_attribute` for reading attributes.

`read_attribute` is an older method in Rails, which can make your code harder to read and understand, especially for those who are not familiar with older Rails methods. Using `self` to access the model's attributes makes the code cleaner and easier to read.

To adhere to this rule, replace instances of `read_attribute(:attribute_name)` with `self[:attribute_name]`. This practice not only improves readability but also ensures your code is consistent with the latest Rails conventions.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class Product < ApplicationRecord
  def price
    read_attribute(:price) + 42
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class Product < ApplicationRecord
  def price
    self[:price] + 42
  end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
