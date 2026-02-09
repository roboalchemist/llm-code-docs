# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/if-let-shorthand.md

---
title: Remove redundant identifier in optional binding if condition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Remove redundant identifier in optional binding if condition
---

# Remove redundant identifier in optional binding if condition

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-code-style/if-let-shorthand`

**Language:** Swift

**Severity:** Warning

**Category:** Code Style

## Description{% #description %}

- **Minimum `Swift` version**: 5.7
- [SE-0345](https://github.com/apple/swift-evolution/blob/main/proposals/0345-if-let-shorthand.md)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
if let name = name {
    // ...
}

if let self = self {
    // ...
}
    
if interactionEnabled,
   let userTapLocation = userTapLocation {
    // ...
}

if let user = user, 
   var device = device {
    // ...
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
if let name {
    // ...
}

if let name = user?.name {
    // ...
}
    
if let user = user as? User {
    // ...
}
 
if var user = currentUser() {
    // ...
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 