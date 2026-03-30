# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/increment-decrement-single-stmt.md

---
title: Increment or decrement are single statement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Increment or decrement are single statement
---

# Increment or decrement are single statement

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/increment-decrement-single-stmt`

**Language:** Swift

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Increments (`++`) or decrements (`--`) should be single statements. This rule is important because it helps to avoid confusion and potential errors in your code. When increments or decrements are combined with other operations, it can be difficult to understand the order in which the operations are performed. This can lead to unexpected results and bugs in your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
foo = ++bar - baz--
foo = bar++

foo(bar++)
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
++foo
bar++
--foo
func factorial(_ n: Int) -> Int {
    guard n >= 0 else {
        foo++
    }
    --bar
    return n == 0 ? 1 : n * factorial(n - 1)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
