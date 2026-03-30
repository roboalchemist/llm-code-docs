# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/printf-sprintf.md

---
title: Do not use Printf with Sprintf
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use Printf with Sprintf
---

# Do not use Printf with Sprintf

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/printf-sprintf`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, developers should avoid using `fmt.Printf(fmt.Sprintf("something"))` and instead use `fmt.Printf("something")`.

Here are a few reasons why:

1. **Unnecessary complexity**: The `fmt.Sprintf` function is used to format a string with placeholders and values. But when you have a simple string like `"something"`, there is no need to use `fmt.Sprintf` to create it. It adds unnecessary complexity to the code without any benefit.
1. **Performance impact**: Using `fmt.Sprintf` to create a string unnecessarily involves extra processing and memory allocation for string formatting. This can have a performance impact, especially if the format string is used frequently or in performance-sensitive areas of the code.
1. **Readability and maintainability**: The excessive use of formatting functions can make the code harder to read and understand. It can also introduce opportunities for mistakes or confusion when working with complex format strings.
1. **Code smell detection**: Many code analysis and linter tools can detect unnecessary usage of `fmt.Sprintf` with constant strings and flag it as a code smell or potential issue. This can lead to noise and make it harder to identify genuine issues in the codebase.

By directly using `fmt.Printf("something")`, you keep the code simpler, more readable, and avoid unnecessary performance overhead. It ensures that the formatting functions are used when needed, rather than wrapping constant strings in unnecessary formatting constructs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    fmt.Printf(fmt.Sprintf("something"))
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    fmt.Printf("something")
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
