# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/array-join.md

---
title: Prefer using Array `join`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using Array `join`
---

# Prefer using Array `join`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/array-join`

**Language:** Ruby

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The rule "Prefer using Array `join`" advises the use of the `join` method over the `*` operator when combining elements of an array into a string. This is because the `join` method is specifically designed for this purpose and its use makes the code more readable and self-explanatory.

The importance of this rule lies in code clarity and maintainability. When other developers read your code, the `join` method clearly communicates that you are combining elements of an array into a string. On the other hand, the `*` operator can be confusing because it is also used for multiplication and repetition operations.

To comply with this rule, always use the `join` method when your intention is to combine elements of an array into a string. For example, instead of writing `%w[foo bar baz] * ', '`, write `%w[foo bar baz].join(', ')`. This change makes the code more readable and less prone to misunderstandings.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
%w[foo bar baz] * ', '
# => 'foo, bar, baz'
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
%w[foo bar baz].join(', ')
# => 'foo, bar, baz'
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
