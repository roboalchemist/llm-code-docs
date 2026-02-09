# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/closure-max-lines.md

---
title: Closures should not have too many lines
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Closures should not have too many lines
---

# Closures should not have too many lines

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/closure-max-lines`

**Language:** Swift

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Closures are designed to be a concise way of injecting behavior without defining a separate function. However, when a closure grows beyond a few lines, it becomes harder to read and maintain. Large closures reduce clarity and make the code less adaptable. To keep the source clean and understandable, closures should remain short, and more complex logic should be extracted into dedicated functions.

## Arguments{% #arguments %}

- `max-lines`: Maximum number of lines allowed in a closure. Default: 40.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift

// A list of numbers to process.
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// NON-COMPLIANT: The closure passed to `forEach` is too long and complex.
// It mixes data transformation, filtering, and printing, harming readability.
numbers.forEach { number in
    // 1. First, let's double the number
    let doubled = number * 2
    print("Processing \(number)...")

    // 2. Check if the doubled number is a multiple of four
    if doubled.isMultiple(of: 4) {
        // 3. Now, let's perform a more complex check
        // Imagine some business logic here
        let isSpecialCase = (doubled + number) % 3 == 0
        
        if isSpecialCase {
             print("Found a special case for \(number)!")
        }





































        print("Final doubled value is \(doubled)")
    } else {
        print("\(doubled) is not a multiple of 4.")
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import Foundation

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

/// Processes a single number with all the required business logic.
/// By moving the logic here, we make it testable and reusable.
func processNumber(_ number: Int) {
    let doubled = number * 2
    print("Processing \(number)...")

    if doubled.isMultiple(of: 4) {
        let isSpecialCase = (doubled + number) % 3 == 0
        if isSpecialCase {
             print("Found a special case for \(number)!")
        }
        print("Final doubled value is \(doubled)")
    } else {
        print("\(doubled) is not a multiple of 4.")
    }
}

// COMPLIANT: The closure is now a simple, one-line call
// to a well-named function. The code is readable and maintainable.
numbers.forEach(processNumber)

// An alternative compliant example using a trailing closure syntax:
numbers.forEach { number in
    processNumber(number)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 