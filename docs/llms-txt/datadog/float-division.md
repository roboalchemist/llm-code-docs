# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/float-division.md

---
title: Use fdiv on two integers float division
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use fdiv on two integers float division
---

# Use fdiv on two integers float division

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/float-division`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule requires the use of `fdiv` for division of two integers when the desired result is a float. This is important because in Ruby, the division of two integers results in an integer. The use of `fdiv` ensures the result is a float, which can be crucial when precision is required in the calculations.

Non-compliance to this rule can lead to inaccurate results due to integer division. For example, `5 / 2` would result in `2`, not `2.5` as one might expect. To avoid this, it is recommended to use the `fdiv` method which ensures a float result. For example, calling `5.fdiv(2)` would correctly return `2.5`.

Remember, it's important to understand the behavior of the language you're using and to use its methods appropriately to ensure the accuracy of your calculations. In Ruby, when dealing with division and expecting a float result, use `fdiv` to avoid potential precision loss.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
foo.to_f / bar.to_f
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
foo.to_f / bar
foo / bar.to_f
foo.fdiv(bar)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
