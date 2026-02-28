# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/rails-best-practices/enums.md

---
title: Prefer using hash syntax for enums
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using hash syntax for enums
---

# Prefer using hash syntax for enums

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `rails-best-practices/enums`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

When defining enums in Ruby, it is better to use the hash syntax rather than the array syntax. This is because the hash syntax is more explicit and less error-prone. With the hash syntax, the mapping between the enum keys and their underlying integer values is clearly defined.

This rule is important because when using the array syntax, the integer values are implicitly assigned based on the order of the keys in the array. This can lead to subtle bugs if the order of the keys in the array is changed. For example, if a new key is inserted in the middle of the array, the integer values of the keys that come after it will be shifted, which can cause existing data to be misinterpreted.

To avoid violating this rule, always use the hash syntax when defining enums in Ruby. Specify the integer value for each key explicitly. For example, instead of `enum status: [:pending, :completed]`, write `enum status: {pending: 0, completed: 1}`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class Transaction < ApplicationRecord
  enum type: %i[income expense]

  enum status: [:pending, :completed]
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class Transaction < ApplicationRecord
  enum type: {
    income: 0,
    expense: 1
  }

  enum status: {
    pending: 0,
    completed: 1
  }
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
