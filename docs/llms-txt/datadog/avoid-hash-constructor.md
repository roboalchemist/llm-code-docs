# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/avoid-hash-constructor.md

---
title: Use hash literal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use hash literal
---

# Use hash literal

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/avoid-hash-constructor`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The "Use hash literal" rule in Ruby encourages the use of hash literals, `{a => b, c => d}`, instead of the `Hash[]` method for creating hashes. This rule is crucial because hash literals are more readable, straightforward, and faster in performance compared to the `Hash[]` method.

The `Hash[]` method might be less clear to some developers, especially those new to Ruby, because it's not immediately obvious that a hash is being created. Moreover, the `Hash[]` method is slower because it involves method call overhead, which can impact the performance of your application if used extensively.

To adhere to this rule, always use hash literals when creating a new hash. For example, instead of using `Hash[a, b, c, d]`, use `{a => b, c => d}`. Similarly, if you need to convert an array to a hash, instead of using `Hash[ary]`, use `ary.to_h`. This will enhance readability and performance of your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
Hash[ary]
Hash[a, b, c, d]
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
ary.to_h
{a => b, c => d}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 