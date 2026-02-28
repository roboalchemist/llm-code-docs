# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/simplify-make.md

---
title: Simplify make and avoid 0 as second argument
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Simplify make and avoid 0 as second argument
---

# Simplify make and avoid 0 as second argument

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/simplify-make`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, developers should avoid using `make([]int, 0)` and instead use `make([]int)`.

Here are a few reasons why:

1. **Simplicity and clarity**: Using `make([]int)` instead of `make([]int, 0)` is simpler and clearer in its intent. The `make([]int)` syntax creates a slice with a length and capacity of 0, indicating an empty slice. It avoids unnecessary redundancy by omitting the explicit specification of a capacity of 0.
1. **Efficiency**: The `make([]int)` expression is more efficient in terms of memory allocation. When creating a slice with a length and capacity of 0, Go's underlying implementation already handles the allocation and management of an empty slice efficiently. Explicitly specifying a capacity of 0 in `make([]int, 0)` doesn't provide any additional benefit in terms of performance.
1. **Readability and maintainability**: Code using `make([]int)` is easier to read and maintain because it represents the intent of creating an empty slice explicitly. It aligns with the idiomatic Go style and is widely recognized and understood by the Go community.

In summary, it is recommended to use `make([]int)` when creating an empty slice in Go instead of `make([]int, 0)`. This approach simplifies the code, improves its readability, and ensures efficient memory allocation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    foo := make([]int, 0, 0)
    foo := make(map[string]string, 0)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    foo := make([]int, 0)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
