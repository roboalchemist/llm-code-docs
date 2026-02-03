# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/redundant-type-var-declaration.md

---
title: Omit redundant type declaration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Omit redundant type declaration
---

# Omit redundant type declaration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/redundant-type-var-declaration`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, it is considered good practice to avoid declaring the type when it is obvious or when the type can be inferred from the assignment. This is known as type inference, and it offers several benefits:

1. Readability: By omitting the explicit type declaration, the code becomes more concise and easier to read. Redundant type declarations can clutter the code and introduce unnecessary noise. When the type is obvious from the assigned value, omitting the type declaration can improve code readability and make it more expressive.
1. Flexibility and maintainability: Using type inference allows for easier changes to the underlying type without manually updating every instance where it is declared. If the type needs to be changed in the future, you only need to modify the assignment, and Go's type inference mechanism will handle the rest. This reduces the maintenance effort required and improves code maintainability.
1. Clean code appearance: Omitting the type declaration when it is obvious results in cleaner code syntax. Code that is free from excessive explicit type declarations tends to look more elegant and consistent. It minimizes redundancy and focuses on the essential logic, contributing to a cleaner and more streamlined codebase.
1. Compatibility: Go's type inference mechanism ensures compatibility with future changes to the type of the assigned value. If the assigned value is changed to a type-compatible value, the code will continue to compile and run without any modifications. This allows for flexibility in your code while maintaining correctness.

That being said, it is important to strike a balance and avoid excessive use of type inference. Clear and explicit type declarations are still valuable when they enhance code clarity, such as when documenting or expressing the intent of the code. It is essential to find the right balance between brevity and clarity in your codebase.

By utilizing Go's type inference mechanism and avoiding explicit type declarations when the type is obvious, you can achieve more readable, maintainable, and concise code that adheres to Go's idiomatic style.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {

    var v int = 1
    var b bool = true
    var c bool = false
    var s string = "hello"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {

    var v = 1
    var b = true
    var c = false
    var s = "hello"
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 