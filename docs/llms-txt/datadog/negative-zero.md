# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/negative-zero.md

---
title: Avoid negative zero
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid negative zero
---

# Avoid negative zero

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/negative-zero`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, negative zero (`-0` or `-0.0`) is considered the same as zero (`0` or `0.0`). This behavior is a result of how floating-point numbers are represented and handled in the Go language specification.

Floating-point numbers in Go follow the standards defined by the IEEE 754 floating-point arithmetic standard. According to this standard, there are two representations for zero: positive zero and negative zero. Both of these representations have the same magnitude but differ in sign. However, they are considered equal in terms of numerical value.

The Go language specification explicitly states that comparisons between floating-point numbers, including zero and negative zero, should follow the IEEE 754 standard. This means that comparing zero and negative zero with equality operators (`==`) will always result in `true`. For example, `0 == -0` and `0.0 == -0.0` both evaluate to `true`.

The reason for this behavior is to ensure consistency and to avoid unnecessary complexity when working with floating-point numbers. By treating zero and negative zero as equal, developers can focus on the numerical value itself without having to account for sign differences.

It's important to note that this behavior is specific to floating-point numbers in Go. In other programming languages or contexts, negative zero may have different semantics or behaviors. Therefore, it's always a good practice to consult the language specification or documentation to understand how zero and negative zero are handled in a specific programming language or environment.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main (){
    foo := -0.0
    foo := 0.0
    bar := float32(-0.0)
    baz := float64(-0.0)
    plopage := -float32(0)
    plopige := -float64(0)
    plopege := -float32(0.0)
    plopyge := -float64(0.0)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main (){
    foo := 0.0
    foo := 0.0
    bar := float32(0.0)
    baz := float64(0.0)
    plopage := float32(0)
    plopige := float64(0)
    plopege := float32(0.0)
    plopyge := float64(0.0)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
