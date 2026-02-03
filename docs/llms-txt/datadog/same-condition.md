# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/same-condition.md

---
title: Replace multiple if with a switch
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Replace multiple if with a switch
---

# Replace multiple if with a switch

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/same-condition`

**Language:** Swift

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule encourages developers to replace multiple consecutive `if` statements that compare the same value with a `switch` statement. Using a `switch` provides clearer intent, improves readability, and makes the control flow easier to follow when handling multiple discrete cases of a single variable.

To comply with this rule, identify sequences of `if` or `else if` conditions that test the same variable against different values and refactor them into a single `switch` statement. This practice leads to cleaner, more maintainable, and idiomatic Swift code. For example, instead of writing `if x == 1 { } else if x == 2 { }`, use `switch x { case 1: ... case 2: ... }`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
class Foo {
    func bar(plop: Int) {
        if plop == 1 {

        } else if plop == 2 {

        } else if plop == something {

        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
class Foo {
    func bar(plop: Int) {
      // no else here, this example is non-sensical and should not pass
      if (x == 3) {
        if (x == 4) {
            // something
        }
      }
    }
}
```

```swift
class Foo {
    func bar(plop: Int) {
        switch plop {
            case 1:
                // something
            case 2:
                // something else
            default:
                // something else as well
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 