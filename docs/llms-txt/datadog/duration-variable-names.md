# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/duration-variable-names.md

---
title: Don't put time units in Duration variables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Don't put time units in Duration variables
---

# Don't put time units in Duration variables

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/duration-variable-names`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, the `time.Duration` type represents a duration of time. It is an integer or float type that represents the length of a duration in units such as seconds, milliseconds, or nanoseconds.

When working with `time.Duration` variables in Go, it is important to note that the type itself already represents a duration with a specific unit. The unit of the duration is determined by the context in which it is used. Therefore, it is not necessary to explicitly include the unit in the variable name or identifier.

Here are a few reasons why we should avoid using time units in variable names for Go's `time.Duration` type:

1. **Clarity and readability**: By not including time units in the variable name, the code becomes more concise, clear, and easier to read. This is because the `time.Duration` type already implies that the value represents a duration.
1. **Flexibility and reusability**: By not tying the variable to a specific unit, it becomes more flexible and reusable. For example, if a variable is named `retryTimeout` instead of `retryTimeoutSeconds`, it can be easily changed to represent a different unit (e.g., milliseconds) without affecting the variable name.
1. **Consistency with standard library**: Go's standard library, including the `time` package, follows the convention of using the type name (`Duration`) without including time units in variable names. By following this convention, our code aligns better with the standard library and promotes code consistency.

To ensure good coding practices, it is recommended to name Go `time.Duration` variables in a descriptive and context-specific manner without explicitly mentioning the time unit in the variable name. This approach leads to clear and maintainable code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    var foo time.Duration
    var xms time.Duration
    var xy, xms time.Duration
    var blaMs time.Duration

    xms := 5 * time.Second
    xms := 5 * time.Millisecond
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    var fooDuration time.Duration
    
    timeToWait := 5 * time.Second
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 