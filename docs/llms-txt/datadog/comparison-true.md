# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/comparison-true.md

---
title: Do not compare to true
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not compare to true
---

# Do not compare to true

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/comparison-true`

**Language:** Go

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Go, it is recommended to use the `if foo` syntax, where `foo` is a boolean expression, rather than comparing it explicitly to `true` using `if foo == true`.

Here are the reasons why `if foo` is preferred:

1. **Simplicity and Readability**: Using `if foo` reduces unnecessary verbosity and improves code readability. It directly expresses the condition based on the truthiness of `foo`, making it easier to understand the intent of the condition without the need for an explicit comparison.
1. **Idiomatic Expression**: In Go, boolean expressions like `foo` already evaluate to `true` or `false`, so comparing them explicitly to `true` is redundant and unnecessary.
1. **Avoiding Errors**: Using `if foo` helps prevent common mistakes, such as accidentally using `=` (assignment operator) instead of `==` (equality operator) in the comparison, which would lead to a logical error.

For example, consider the following code snippets:

```go
1
2
3
if foo {
    // Code block
}
```

```go
1
2
3
if foo == true {
    // Code block
}
```

Both snippets achieve the same result if `foo` evaluates to `true`. However, the first snippet using `if foo` is preferred for its simplicity, clarity, and adherence to Go's idiomatic style.

By using `if foo` instead of `if foo == true`, you can write cleaner and more readable code that takes advantage of the natural boolean evaluation in Go.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    if foo == true {
        
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    if foo {
        
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 