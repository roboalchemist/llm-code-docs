# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/specify-return-type.md

---
title: User must specify return type via ->.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > User must specify return type via ->.
---

# User must specify return type via ->.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/specify-return-type`

**Language:** Swift

**Severity:** Error

**Category:** Code Style

## Description{% #description %}

In Swift, specifying a function's return type is crucial for readability, maintainability, and to avoid potential runtime errors. This rule enforces that the return type of a function should always be explicitly stated using the '->' symbol followed by the type of the value that will be returned.

Not specifying a return type can lead to confusion for other developers who might use your function, as they won't be able to predict what kind of value they should expect. Additionally, it can cause errors if the function is expected to return a value but doesn't, or returns a different type than expected.

To adhere to this rule, always specify the return type of your function in its declaration. For instance, if your function is supposed to return an integer, you would write `func addTwoNums(num1: Int, num2: Int) -> Int`. This makes it clear that the function will return an integer value.

## Compliant Code Examples{% #compliant-code-examples %}

```swift
func addTwoNums(num1: Int, num2: Int) {
    return num1 + num2;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
