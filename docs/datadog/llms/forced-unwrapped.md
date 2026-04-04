# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/forced-unwrapped.md

---
title: Optionals should not be force-unwrapped
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Optionals should not be force-unwrapped
---

# Optionals should not be force-unwrapped

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/forced-unwrapped`

**Language:** Swift

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Declaring a variable as optional clearly signals that it may not hold a valid value and could be `nil`. Force-unwrapping bypasses that safety and will cause a runtime crash if the value is actually `nil`. Even if you check for `nil` first, relying on force-unwrapping is still discouraged because it undermines the intent of optionals. A safer and more maintainable approach is to use optional binding or optional chaining to handle values gracefully.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
var greeting: String?

// ...
println( \(greeting!))  // Noncompliant; could cause a runtime error

if greeting != nil {
  println( \(greeting!))  // Noncompliant; better but still not great
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
var greeting: String?

// ...
if let howdy = greeting {
  println(howdy)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
