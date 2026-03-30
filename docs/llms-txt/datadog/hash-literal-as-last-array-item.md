# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/hash-literal-as-last-array-item.md

---
title: Wrap hash literal in braces if last in array
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Wrap hash literal in braces if last in array
---

# Wrap hash literal in braces if last in array

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/hash-literal-as-last-array-item`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Ruby, hash literals can sometimes be ambiguous, especially when they are the last element in an array without being explicitly wrapped in braces. This rule enforces the use of braces around hash literals when they are the last element in an array.

The importance of this rule lies in maintaining the clarity and readability of your code. It can be confusing for others (or even for yourself at a later date) to understand the intention of your code when a hash literal is not clearly defined within an array. Furthermore, not wrapping a hash literal in braces may lead to unexpected behavior, as Ruby might not interpret it as you intended.

To adhere to this rule and ensure good coding practices, always wrap hash literals in braces `{}` when they are the last element in an array. For example, instead of writing `[1, 42, foo: 99, bar: 96]`, you should write `[1, 42, { foo: 99, bar: 96 }]`. This makes it clear that the last element is a hash, improving the readability and predictability of your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
[1, 42, foo: 99, bar: 96]
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
[1, 42, { foo: 99, bar: 96 }]
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
