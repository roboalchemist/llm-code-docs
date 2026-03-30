# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/guard-let-shorthand.md

---
title: Remove redundant identifier in optional binding guard
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Remove redundant identifier in optional binding guard
---

# Remove redundant identifier in optional binding guard

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/guard-let-shorthand`

**Language:** Swift

**Severity:** Warning

**Category:** Code Style

## Description{% #description %}

This rule identifies and flags redundant identifiers in optional binding within `guard` statements, such as `guard let name = name else { ... }`. In Swift, when the identifier on the left side of the binding is the same as the optional being unwrapped, you can omit the explicit assignment and write `guard let name else { ... }` instead. This simplification improves code readability by reducing unnecessary repetition.

To comply with this rule, simply omit the explicit assignment when unwrapping an optional with the same identifier, using `guard let variable else { ... }` rather than `guard let variable = variable else { ... }`. Always prefer this concise form unless you need to bind to a different variable name or perform type casting.

## Notes{% #notes %}

- **Minimum `Swift` version**: 5.7
- [SE-0345](https://github.com/apple/swift-evolution/blob/main/proposals/0345-if-let-shorthand.md)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
guard let name = name else {
    // ...
}

guard let self = self else {
    // ...
}

guard interactionEnabled,
   let userTapLocation = userTapLocation else {
    // ...
}

guard let user = user,
   var device = device else {
    // ...
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
guard let name else {
    // ...
}

guard let name = user?.name else {
    // ...
}

guard let user = user as? User else {
    // ...
}

guard var user = currentUser() else {
    // ...
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
