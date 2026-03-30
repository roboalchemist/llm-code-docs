# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/manual-string-trimming.md

---
title: Avoid manual string trimming
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid manual string trimming
---

# Avoid manual string trimming

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/manual-string-trimming`

**Language:** Go

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

In Go, the `strings.TrimPrefix()` function provides a more idiomatic and efficient way to remove a prefix from a string compared to using `strings.HasPrefix()` and slicing the string manually. It is preferred for:

1. Readability: `strings.TrimPrefix(str, prefix)` conveys the intention of removing the specified prefix from `str` more clearly than using `strings.HasPrefix()` and slicing `str`. It's a self-explanatory function that makes the code more readable and easier to understand.
1. Simplicity: By using `strings.TrimPrefix()`, you eliminate the need for manual slicing and calculating the length of the prefix. It simplifies your code and reduces the chances of introducing errors.

For example, consider the following code snippets:

```go
if strings.HasPrefix(str, prefix) {
    str = str[len(prefix):]
}
```

```go
str = strings.TrimPrefix(str, prefix)
```

Both snippets remove the prefix from the string if it exists. However, the second snippet using `strings.TrimPrefix()` is preferred for its simplicity, readability, and potential performance benefits.

By using `strings.TrimPrefix()` instead of the manual slicing approach, you can write cleaner and more efficient code that adheres to Go's idiomatic principles.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    if strings.HasPrefix(str, prefix) {
        str = str[len(prefix):]
        str2 := str[len(prefix):]
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    strings.TrimPrefix(str, prefix)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
