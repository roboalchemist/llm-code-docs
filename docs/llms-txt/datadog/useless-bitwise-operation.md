# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/useless-bitwise-operation.md

---
title: Avoid useless bit operations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid useless bit operations
---

# Avoid useless bit operations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/useless-bitwise-operation`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The expressions `x|0`, `x^0`, and `x&0` are bitwise operations that involve the number `0`. In these specific cases, the operation with `0` doesn't have any effect on the value `x`.

1. `x|0`: The bitwise OR (`|`) operation between `x` and `0` will result in `x` itself. This is because any bit OR'ed with `0` will retain its original value. Therefore, `x|0` can be simplified and replaced with just `x`.
1. `x^0`: The bitwise XOR (`^`) operation between `x` and `0` is similar to the OR operation. XOR'ing any bit with `0` will preserve its original value. As a result, `x^0` is equivalent to `x`. Thus, the expression `x^0` can be simplified and replaced by just `x`.
1. `x&0`: The bitwise AND (`&`) operation between `x` and `0` will always yield `0`. This is because any bit AND'ed with `0` will always result in `0`. Therefore, `x&0` can be simplified and replaced by just `0`.

Simplifying these expressions by replacing them with their respective values (`x` or `0`) can enhance code readability and reduce unnecessary operations. However, it's important to note that these simplifications only hold true when being operated on with the constant `0`. If the constant value changes or the expressions involve variables, the behavior and result may vary.

By avoiding unnecessary operations and writing code that clearly exprresses your intent, you can make your code more maintainable and readable.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    println(x | 0)
    println(x & 0)
    println(x ^ 0)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    println(x)
    println(0)
    println(x)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 