# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/sprintf.md

---
title: Prefer sprintf and form
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer sprintf and form
---

# Prefer sprintf and form

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/sprintf`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule enforces the use of `sprintf` and `format` over the `%` operator for string formatting in Ruby. This is important because `sprintf` and `format` are more readable and less error-prone than the `%` operator.

The `%` operator can lead to confusion and bugs, especially when the array to be interpolated contains more items than expected or when it's not clear what type of formatting is being applied.

To avoid this, always use `sprintf` or `format` for string formatting. These methods are more explicit about what formatting is being applied, making the code easier to understand and safer. For example, `sprintf('%d %d', 1, 42)` is preferred over `'%d %d' % [1, 42]`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
'%d %d' % [1, 42]
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
sprintf('%d %d', 1, 42)
sprintf('%<foo>d %<bar>d', foo: 1, bar: 42)

format('%d %d', 1, 42)
format('%<foo>d %<bar>d', foo: 1, bar: 42)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
