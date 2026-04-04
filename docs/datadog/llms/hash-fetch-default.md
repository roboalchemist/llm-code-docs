# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/hash-fetch-default.md

---
title: Use fetch with default over custom check
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use fetch with default over custom check
---

# Use fetch with default over custom check

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/hash-fetch-default`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule emphasizes the importance of using the `fetch` method with a default value in Ruby, rather than a custom check. This is because the `fetch` method correctly handles 'falsey' values, such as `false` or `nil`, and will return them when they are the actual value associated with a key in a hash. This prevents unexpected results that may occur when using a custom check, as it may incorrectly evaluate a 'falsey' value as not present and return the default value instead.

The importance of this rule lies in the accuracy and predictability of your code. It ensures that you are correctly handling all potential values in a hash and not mistakenly returning a default value when the key is present but associated with a 'falsey' value. This can lead to bugs that are hard to track down and fix in your code.

To abide by this rule, always use the `fetch` method with a default value when checking if a key is present in a hash and you want to return a default value if it isn't. This method will correctly handle all values, including 'falsey' ones, and return the accurate result. For example, instead of using `hash[:key] || default_value`, use `hash.fetch(:key, default_value)`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
test = { foo: 'foo', is_bar: false }

# on a falsey value, you get unexpected results
test[:is_bar] || true # => true
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
test = { foo: 'foo', is_bar: false }

# fetch works on falsey values, so you get expected results
test.fetch(:is_bar, true) # => false
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
