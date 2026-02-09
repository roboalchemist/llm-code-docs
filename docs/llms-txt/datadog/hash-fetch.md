# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/hash-fetch.md

---
title: Use fetch to check hash keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use fetch to check hash keys
---

# Use fetch to check hash keys

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/hash-fetch`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Use fetch to check hash keys" encourages the use of the `fetch` method over the direct hash access method `[]` for checking hash keys. This is because `fetch` raises an error when the key does not exist in the hash, making the code more robust and fail-safe by preventing any unexpected behavior due to missing hash keys.

The significance of this rule lies in its ability to make the code more predictable and error-resistant. When a hash key is accessed directly using `[]`, and the key does not exist, Ruby returns `nil` by default. This can lead to subtle bugs if the existence of the key is crucial for the subsequent code. Using `fetch`, on the other hand, will raise a `KeyError` if the key is not found, making it immediately clear that there's an issue with the code.

Adhering to this rule is straightforward. Instead of using direct hash access, use the `fetch` method whenever you need to access a hash key. For example, instead of `hash[:key]`, use `hash.fetch(:key)`. This way, if the key does not exist in the hash, your code will raise an error, allowing you to catch and handle the problem early on.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
test = { foo: 'foo', bar: 'bar', magic_num: 42 }
test[:foo] # => 'foo'
test[:qux] # => nil

def foo(opts)
  puts opts[:bar]
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
test = { foo: 'foo', bar: 'bar' }
test.fetch(:foo) # => 'foo'
test[:bar] = 42
test.fetch(:qux) # => KeyError
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 