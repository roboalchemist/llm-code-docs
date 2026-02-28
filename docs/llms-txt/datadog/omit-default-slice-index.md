# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/omit-default-slice-index.md

---
title: Omit default slices
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Omit default slices
---

# Omit default slices

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/omit-default-slice-index`

**Language:** Go

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

In Go, the expression `s[n:len(s)]` is used to slice a string or slice `s` starting from index `n` up to the end of `s`. However, it is considered suboptimal and can be replaced with the simpler and more expressive `s[n:]` notation.

Using `s[n:len(s)]` is not optimal for a few reasons:

1. Readability: The `s[n:]` notation provides a clearer and more concise representation of slicing from index `n` to the end of `s`. It eliminates the need to explicitly specify `len(s)`, making the code more readable.
1. Simplicity: By using `s[n:]`, you remove unnecessary redundancy in the code. It improves the simplicity of your code and reduces the chances of introducing errors when manually specifying the length of `s`.
1. Performance: Although the performance difference may be negligible, using `s[n:]` is more efficient than creating a `len(s)` expression. The `s[n:]` notation directly references the underlying slice without requiring an additional length calculation.

For example, let's consider the following code snippets:

```go
s := "Hello, World!"
fmt.Println(s[7:len(s)])
```

Output: "World!"

```go
s := "Hello, World!"
fmt.Println(s[7:])
```

Output: "World!"

Both snippets will produce the same output, but the second one using `s[7:]` is preferred for its simplicity and readability.

By replacing `s[n:len(s)]` with `s[n:]`, you can improve the clarity and maintainability of your code while still achieving the desired slicing functionality.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    d := s[n:len(s)]
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    d := s[n:]
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
