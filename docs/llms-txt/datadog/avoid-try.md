# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/avoid-try.md

---
title: '"try!" should not be used'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > "try!" should not be used
---

# "try!" should not be used

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/avoid-try`

**Language:** Swift

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The `try!` operator should not be used because it forces execution of potentially failing code without proper error handling. If the call does throw an error, the program will crash immediately, leading to unpredictable behavior and poor maintainability. Instead, use `try?` with optional binding or the full `doâcatch` syntax to safely handle errors and keep the code resilient.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
//
//
//
let myvar = try! dangerousCode(foo);  // Noncompliant
// ...
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
guard let myvar = try? dangerousCode(foo) else {
  // handle error
}

// or

if let myvar = try? dangerousCode(foo); {
  // ...
} else {
  // handle error
}

// or

do {
  let myvar = try dangerousCode(foo)
  // ...
} catch {
  // handle error
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 