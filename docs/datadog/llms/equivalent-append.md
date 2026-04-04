# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/equivalent-append.md

---
title: Do not use append for assignment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use append for assignment
---

# Do not use append for assignment

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/equivalent-append`

**Language:** Go

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

In Go, the `append()` function is used to append elements to a slice. It is a built-in function that takes a slice and one or more elements as arguments and returns a new slice with the appended elements.

When `append()` is called with a single argument, it is similar to the assignment of that argument to a variable. This is because the `append()` function returns a new slice that includes the original elements of the input slice and the appended element(s).

For example:

```go
s := []int{1, 2, 3}
s = append(s, 4)
```

In this code snippet, the `append()` function is called with a single argument `s` and the value `4`. The `append()` function returns a new slice with the elements `[1, 2, 3, 4]`, and this new slice is assigned back to the variable `s`. The original value of `s` is replaced with the new slice containing the appended element.

It is important to note that the `append()` function does not modify the original slice in-place since slices are reference types in Go. Instead, it returns a new slice that combines the elements of the original slice and the appended element(s).

In summary, when `append()` is used with a single argument, it effectively performs an assignment of the argument to the variable, replacing the original value with a new slice that includes the appended element(s).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    x = append(y)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    x = y
    gitdbClientValue = getGitDBClient(api)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
