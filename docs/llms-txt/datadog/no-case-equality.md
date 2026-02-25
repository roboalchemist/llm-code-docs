# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-case-equality.md

---
title: Avoid explicit use of the case equality operator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid explicit use of the case equality operator
---

# Avoid explicit use of the case equality operator

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-case-equality`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The case equality operator `===` in Ruby is used to test equality within a `when` clause of a `case` statement. However, it's often considered a bad practice to use this operator explicitly outside of a `case` statement. This is because its behavior can be quite unpredictable and confusing, as it behaves differently for different classes.

The use of the `===` operator can lead to code that is harder to read and understand. It's also potentially prone to bugs, as it might not behave as expected with certain objects. Therefore, it's recommended to avoid the explicit use of the `===` operator.

Instead of using the `===` operator, it's better to use more explicit methods that clearly indicate what you're trying to achieve. For example, if you're trying to check if a string matches a regular expression, you can use the `match?` method. If you want to check if an object is an instance of a certain class, you can use the `is_a?` method. These methods are much more clear and straightforward, leading to better, more maintainable code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
/something/ === some_string
Array === something
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
some_string.match?(/something/)
something.is_a?(Array)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
