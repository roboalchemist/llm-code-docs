# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-datetime.md

---
title: Avoid `DateTime` unless for historical purposes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid `DateTime` unless for historical purposes
---

# Avoid `DateTime` unless for historical purposes

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-datetime`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `DateTime` class in Ruby is known for its complexity and potential for confusion. It is based on the Julian Day Number system, which is primarily used for astronomical and historical calculations. While it does offer precision to the nanosecond, this level of detail is rarely necessary in most application development.

Using `DateTime` for common date and time manipulation can lead to unexpected behavior, especially when dealing with time zones. This is due to `DateTime`'s handling of time offsets as fractions of a day, which can result in rounding errors. It also lacks support for daylight saving time adjustments.

Instead, it's recommended to use the `Time` and `Date` classes for most common date and time operations. `Time` handles time zones better and `Date` is simpler for date-only operations. `DateTime` should be reserved for historical date and time calculations, where the Julian Day Number system is necessary. For example, `DateTime.iso8601('1867-07-01', Date::ITALY)` would be appropriate for representing the date of Canada's confederation in the Italian calendar.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
DateTime.now
DateTime.iso8601('2018-02-04')
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
Time.now
Date.iso8601('2018-02-04')
DateTime.iso8601('1867-07-01', Date::CANADA)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
