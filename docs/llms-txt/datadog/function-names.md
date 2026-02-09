# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/function-names.md

---
title: Function names should comply with a naming convention
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Function names should comply with a naming convention
---

# Function names should comply with a naming convention

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/function-names`

**Language:** Swift

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Function names should consistently follow the team's established naming convention. Using a standard format makes code easier to read, maintain, and understand across the codebase. Any function name that doesn't match the required pattern (such as starting with a lowercase letter) should be updated to align with the convention.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
import Foundation

// NON-COMPLIANT: This function name starts with an uppercase letter (PascalCase),
// which violates the lower-camel-case convention.
func DoSomething() {
    print("Doing something...")
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import Foundation

// COMPLIANT: This function name follows the lower-camel-case convention.
// It starts with a lowercase letter.
func doSomething() {
    print("Doing something...")
}

// COMPLIANT: A multi-word example that also follows the convention.
func calculateArea(width: Double, height: Double) -> Double {
    return width * height
}

// COMPLIANT: Another example adhering to the rule.
func printUserDetails(name: String, age: Int) {
    print("User: \(name), Age: \(age)")
}

// allow leading underscore
func _invalidPrivateFunction() {
    print("This is an invalid private function name.")
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 