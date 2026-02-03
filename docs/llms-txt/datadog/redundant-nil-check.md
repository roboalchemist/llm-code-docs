# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/redundant-nil-check.md

---
title: Avoid redundant nil check
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid redundant nil check
---

# Avoid redundant nil check

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/redundant-nil-check`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, it is recommended to avoid using `something == nil && len(something) == 0` in an `if` condition and instead use just `len(something) == 0`.

Here are a few reasons why:

1. **Simplicity and readability**: The expression `len(something) == 0` clearly conveys the intent of checking if a variable or collection is empty. It is more concise and easier to understand for other developers reading the code. Including `something == nil` in the condition adds unnecessary complexity and may confuse readers.
1. **Consistent behavior**: In Go, the `len()` function is specifically designed to handle different types, including slices, arrays, maps, and strings. Using `len()` directly allows consistency in checking the length of any data structure without the need to handle specific cases for `nil`.
1. **Avoiding nil checks**: Checking `something == nil` adds an extra condition to handle the case when `something` is `nil`, which may or may not be desired or necessary. By focusing only on the length check with `len(something) == 0`, you eliminate the need for a separate nil check, simplifying the code.

Therefore, it is recommended to use `len(something) == 0` to check if something is empty, rather than `something == nil && len(something) == 0`. This approach enhances code readability, maintains consistency, and avoids unnecessary nil checks in Go.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    if something == nil && len(something) == 0{
        println("foo")
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    if len(something) == 0 {
        println("foo")
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 