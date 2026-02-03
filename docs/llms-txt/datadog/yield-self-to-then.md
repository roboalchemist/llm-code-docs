# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/yield-self-to-then.md

---
title: Prefer using then over yield_self
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using then over yield_self
---

# Prefer using then over yield_self

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/yield-self-to-then`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer using `then` over `yield_self`" is a coding practice in Ruby that helps improve code readability and simplicity. In Ruby, both `yield_self` and `then` are used to yield the receiver to a block and return the result. However, as of Ruby 2.6, `then` is the preferred method due to its simplicity and clearer syntax.

The importance of this rule lies in the maintenance and readability of the code. `then` is more intuitive and easier to understand for developers, especially those who are new to Ruby. This can lead to fewer misunderstandings and bugs in the code, and make it easier for developers to read and maintain the code in the future.

To follow this rule, replace any instances of `yield_self` with `then`. For example, instead of writing `foo.yield_self { |x| x.do_something }`, you should write `foo.then { |x| x.do_something }`. Similarly, `"FOO".yield_self { |x| x.downcase }` should be replaced with `"FOO".then { |x| x.downcase }`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
foo.yield_self { |x| x.do_something }
"FOO".yield_self { |x| x.downcase }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
foo.then { |x| x.do_something }
"FOO".then { |x| x.downcase }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 