# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/avoid-bare-return.md

---
title: Avoid bare returns
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid bare returns
---

# Avoid bare returns

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/avoid-bare-return`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The "Avoid bare returns" rule in Go static analysis is designed to increase clarity and readability in your code. A bare return is when a function that has named return values returns those values implicitly, without explicitly stating what is being returned.

While Go's allowance for bare returns can make code more concise, it can also make it more difficult to understand and debug, especially in larger functions. Implicitly relying on the state of named return values can lead to unexpected behavior if those values are modified elsewhere in the function.

To adhere to this rule and promote better coding practices, always explicitly return values in your functions. This makes it clear what values are being returned and in what state, reducing the chance of bugs and making your code easier to understand. For example, instead of writing `return` in a function that returns an `int` and a `bool`, write `return 0, false`.

### Learn More{% #learn-more %}

- [Named return values](https://go.dev/tour/basics/7)
- [Proposal to remove bare returns](https://github.com/golang/go/issues/21291)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func func1(arg int) (a int) {
    return
}

func func2(arg int) (b int) {
    return
}

func func3(arg int) (a int, b bool) {
    return
}


func func4(a string, b int) (a int, b string) {
    return
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func func1(arg int) {
    return
}

func func2(arg int) int {
    return 4
}

func func3(arg int) (int, bool) {
    return 3, false
}


func func3(arg int) (int, bool) {
    return 3, true
}

func func2(arg int) int {
    return
}

func func3(arg int) (int, bool) {
    return
}


func func3(arg int) (int, bool) {
    return 3, true
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
