# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/collection-size.md

---
title: Collection size should not always be true or false
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Collection size should not always be true or false
---

# Collection size should not always be true or false

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/collection-size`

**Language:** Swift

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule identifies conditions where a collection's size is compared in a way that will always evaluate to true or false, such as checking if `count < 0` or `count >= 0`. Since collection counts are never negative, these comparisons are logically incorrect and indicate a potential flaw or misunderstanding in the code.

To avoid violations of this rule, ensure that comparisons involving collection sizes use valid and meaningful operators. For example, use `count == 0` to check if a collection is empty, or `count > 0` to verify it contains elements. Reviewing the logic behind size comparisons helps maintain correct and readable code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
if (something.count < 0) {
    // some statement
} 
```

```swift
if (something.count >= 0) {
    // some statement
} 
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
if (something.count == 0) {
    // some statement
} 
```

```swift
if (something.count > 0) {
    // some statement
} 
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 