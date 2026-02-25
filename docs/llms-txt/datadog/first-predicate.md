# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/first-predicate.md

---
title: Use first rather than filter and first
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use first rather than filter and first
---

# Use first rather than filter and first

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/first-predicate`

**Language:** Swift

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of the `first(where:)` method instead of chaining `filter` followed by `first` when searching for the first element that matches a condition. Using `first(where:)` is more efficient because it stops iterating as soon as it finds the first matching element, whereas `filter` evaluates the entire collection before extracting the first element.

To comply with this rule, replace code like `bar.filter { $0.containsString("baz") }.first` with `bar.first(where: { $0.containsString("baz") })`. This not only optimizes the code but also enhances readability and maintainability.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
let foo = bar.filter { $0.containsString("baz") }.first
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
let foo = bar.first(where: { $0.containsString("baz") })
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
