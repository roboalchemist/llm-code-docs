# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/iboutlet-private.md

---
title: Variables of type IBOutlet should be private
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Variables of type IBOutlet should be private
---

# Variables of type IBOutlet should be private

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/iboutlet-private`

**Language:** Swift

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

All variables of type `IBOutlet` should be set as private. `IBOutlet` variables are typically used in Swift to connect the UI elements from the storyboard to the code. Making these variables private enhances encapsulation and data hiding, which are fundamental principles of object-oriented programming.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
class MyClass {
    @IBOutlet var label: UILabel!
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
class MyClass {
    @IBOutlet private var label: UILabel!
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 