# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/unnecessary-blank-identifier.md

---
title: Remove unnecessary blank identifiers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Remove unnecessary blank identifiers
---

# Remove unnecessary blank identifiers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/unnecessary-blank-identifier`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, when using range iterations or receiving values from channels, it is recommended to avoid assigning the iteration or received value to the blank identifier `_`. Instead, it is preferred to omit the assignment entirely.

Here's why it is best to use `for range s {}`, `x = someMap[key]`, and `<-ch` instead of using the blank identifier `_`:

1. Clarity and Readability: By omitting the assignment entirely, it makes the code more readable and self-explanatory. Using `_` can introduce confusion and make it less clear what the purpose of the assignment is or if the value is discarded intentionally or accidentally.
1. Avoiding Variable Pollution: Using `_` as an assignment can unnecessarily pollute the variable space. Although Go allows the use of the blank identifier `_` to disregard a value, it is a good practice to avoid introducing unnecessary variables, especially if they are never used.
1. Linting and static analysis: Some linting tools and static analyzers may flag the use of `varName = _` as an indication of accidental assignment or failure to handle errors or returned values properly. Removing these assignments eliminates such warnings or false-positive detections.

For example, consider the following code snippets:

```go
for _ = range aSlice {}
x, _ = something()
_ = <- aChannel
```

```go
for range aSlice {}
x = something()
<-aChannel
```

Both snippets achieve the same result, but the second one that omits the assignments using `_` is preferred for its simplicity, readability, and adherence to Go's best practices.

By using `for range s {}`, `x = someMap[key]`, and `<-ch` instead of assigning to `_`, you can write cleaner and more readable Go code while avoiding unnecessary variable assignments and potential confusion.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    for _ = range aSlice {

    }
    x, _ = myMap[key]
    _ = <- aChannel

    x, _ = myFunction()

    for key, _ = range myMap {

    }

    for _, _ = range myMap {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    for aSlice {

    }
    x = myMap[key]
    <- aChannel

    for _, val = range mySlice {

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
