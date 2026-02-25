# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/invalid-seek-value.md

---
title: Invalid seek value
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Invalid seek value
---

# Invalid seek value

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/invalid-seek-value`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, it is recommended to pass the arguments to a function in the correct order, according to the function signature. This helps improve code readability, maintainability, and reduces the chances of errors.

The reason why we should avoid `myValue.Seek(io.SeekStart, 0)` and use `myValue.Seek(0, io.SeekStart)` instead is to follow the convention of passing the offset (or other numerical parameter) before the whence parameter.

The `Seek` function in Go's `io` package takes two parameters: `offset` and `whence`. The `offset` parameter represents the distance from the reference point, and the `whence` parameter represents the reference point itself.

By following the convention of passing the offset before the whence parameter, the code becomes more consistent with Go's standard library and promotes uniformity across different codebases.

This convention aligns with how other functions in the standard library, as well as commonly used idioms in Go, work. For instance, in the `Seek` function's counterpart, the `Read` function, the offset is passed before the buffer parameter: `Read(buffer []byte, offset int64)`

By using `myValue.Seek(0, io.SeekStart)` and `myValue.Seek(10, myio.SeekCurrent)`, it better conveys the intention of the code and makes it easier for developers to understand the purpose of each parameter.

To summarize, it is good coding practice to pass function arguments in the correct order, according to the function signature and established conventions. In this case, it means passing the offset before the whence parameter, as in `myValue.Seek(0, io.SeekStart)` and `myValue.Seek(10, myio.SeekCurrent)`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    myValue.Seek(io.SeekStart, 0)
    myValue.Seek(myio.SeekCurrent, 10)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    myValue.Seek(0, io.SeekStart)
    myValue.Seek(10, myio.SeekCurrent)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
