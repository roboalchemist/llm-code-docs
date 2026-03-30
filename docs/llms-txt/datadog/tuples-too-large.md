# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/tuples-too-large.md

---
title: Tuples should not be too large
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Tuples should not be too large
---

# Tuples should not be too large

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/tuples-too-large`

**Language:** Swift

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Tuples should not be too large. This is because tuples are designed to be simple, quick ways to group related values. They are not meant to serve as data structures or record types, which are better suited to handle larger amounts of data.

To avoid the violation of this rule, you should consider using a struct or a class when you find yourself needing a tuple with more than two or three items. For example, instead of `func myfunction() -> (Int, Int, Int, String) {}`, you could define a struct like this: `struct MyFunctionResult { let a: Int; let b: Int; let c: Int; let d: String }`, and then have `myfunction()` return a `MyFunctionResult`. This makes your code more readable and easier to maintain.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
func myfunction() -> (Int, Int, Int, String) {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
