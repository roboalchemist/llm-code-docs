# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/disjunctive-assign-in-const.md

---
title: Avoid unnecessary disjunctive assignments in constructor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unnecessary disjunctive assignments in constructor
---

# Avoid unnecessary disjunctive assignments in constructor

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/disjunctive-assign-in-const`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule pertains to the practice of avoiding unnecessary disjunctive (or conditional) assignments in class constructors in Ruby. A disjunctive assignment, denoted by `||=`, is a shorthand way of saying "if this variable is `nil` or `false`, assign it this value; otherwise, leave it as it is." While this can be a useful tool in some instances, using it in a class constructor can lead to confusing and unexpected behavior.

The main reason to avoid this practice is that it can lead to unexpected values for instance variables. In the non-compliant code example, if `@foo` somehow has a value before the constructor is called, that value will be preserved instead of being set to `42` as might be expected. This can make debugging more difficult and lead to subtle, hard-to-find bugs.

To avoid this issue, assign the value directly in the constructor, as shown in the compliant code example. This ensures that the instance variable will always have the expected value when the constructor is finished. It's a small change, but it can make your code much easier to understand and debug.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def initialize
  @foo ||= 42
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
def initialize
  @foo = 42
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
