# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/time-now-sub.md

---
title: Use Since() instead of Now().Sub()
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use Since() instead of Now().Sub()
---

# Use Since() instead of Now().Sub()

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/time-now-sub`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Go's `time` package provides functions and methods for working with dates and times. When calculating the duration between a specific time and the current time, it is recommended to use the `time.Since(x)` function instead of `time.Now().Sub(x)`.

Here are a few reasons why:

1. Readability: The `time.Since(x)` function conveys the intention of calculating the duration since a specific time `x` in a straightforward manner. It's more readable and easier to understand than chaining `time.Now().Sub(x)`, which requires reading the code from right to left.
1. Performance: Using `time.Since(x)` avoids the unnecessary creation of an intermediate `time.Time` value with `time.Now()`. By directly calculating the time duration since `x`, you eliminate the overhead of the additional function call and improve performance.
1. Consistency: The `time.Since(x)` function provides a consistent and idiomatic way of calculating the duration since a specific time. It follows the design principles of the standard library and promotes best practices for Go code.

For example, consider the following code snippets:

```go
x := time.Date(2022, time.March, 20, 0, 0, 0, 0, time.UTC)
duration := time.Now().Sub(x)
fmt.Println(duration)
```

Output: The duration between the current time and March 20, 2022.

```go
x := time.Date(2022, time.March, 20, 0, 0, 0, 0, time.UTC)
duration := time.Since(x)
fmt.Println(duration)
```

Output: The duration between the current time and March 20, 2022.

Both snippets achieve the same result, but the second one using `time.Since(x)` is preferred for its simplicity, readability, and performance.

By using `time.Since(x)` instead of `time.Now().Sub(x)`, you can write more concise and idiomatic Go code, improving readability and maintaining consistency with the standard library.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    x := time.Now().Sub(x)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    x := time.Since(x)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
