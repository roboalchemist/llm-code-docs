# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/comparing-address-nil.md

---
title: Do not check address to nil
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not check address to nil
---

# Do not check address to nil

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/comparing-address-nil`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The code `if &x == nil` is not recommended in Go and should be avoided.

Here are a few reasons why:

1. **Incorrect Comparison**: In Go, comparing the address of a variable `&x` directly to `nil` using `==` is not a valid or meaningful comparison. The address of a variable is a memory location and cannot be directly compared to `nil` to check for its value.
1. **Pointer Check**: Comparing the address of a variable to `nil` using `==` does not accurately check if the variable itself is nil. It only checks if the address is null, not the value stored at that address.
1. **Incorrect Usage of** `nil`: In Go, `nil` is typically used to check if a pointer or reference type is uninitialized or doesn't point to a valid object. It is not meant to be used to compare the address of a variable.

To check if a variable is nil, you should directly compare its value to `nil` without taking its address:

```go
if x == nil {
    // Code block
}
```

This is the correct and idiomatic way to check if a variable is nil in Go.

By avoiding the usage of `&x == nil` and using `x == nil` instead, you can write cleaner and more accurate code that adheres to Go's best practices.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    if &myVar == nil {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    var ptr *int = &myVar
    if ptr == nil {

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 