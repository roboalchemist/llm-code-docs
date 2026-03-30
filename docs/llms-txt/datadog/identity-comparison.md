# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/identity-comparison.md

---
title: Prefer equal? over == when comparing object_id
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer equal? over == when comparing object_id
---

# Prefer equal? over == when comparing object_id

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/identity-comparison`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Ruby, the rule "Prefer `equal?` over `==` when comparing `object_id`" is important to remember because of how these two comparison methods function. The `equal?` method checks if the two compared references point to the exact same object, while the `==` method checks if the values of the two objects are the same.

This rule is crucial because when you are comparing `object_id`, you are actually interested in whether the two objects are the same object, not whether their values are equal. Using `==` can lead to unexpected results if two different objects have the same `object_id`.

To adhere to this rule and maintain good coding practices, always use `equal?` when comparing `object_id`. This ensures that you are accurately checking if the two objects are the same. For instance, instead of writing `foo.object_id == bar.object_id`, you should write `foo.equal?(bar)`. This way, you are properly checking for object identity, not object equality.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
foo.object_id == bar.object_id
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
foo.equal?(bar)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
