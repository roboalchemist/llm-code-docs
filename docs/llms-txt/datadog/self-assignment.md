# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/self-assignment.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/self-assignment.md

---
title: Prevent self-assignment of variables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent self-assignment of variables
---

# Prevent self-assignment of variables

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/self-assignment`

**Language:** Go

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Self-assignments are not useful and should generally be avoided.

Here are a few reasons why:

```go
x := 10
x = x
```

Self-assignments are not useful and should generally be avoided. Here are a few reasons why:

1. **Useless operation**: Self-assignments don't change the value of the variable. It's essentially a no-op operation that doesn't have any impact on the program's execution or the variable's state. It adds unnecessary code clutter and can confuse other developers who may assume that the self-assignment serves some purpose.
1. **Reduced readability**: Self-assignments can make the code less readable and harder to understand. When encountering such code, developers might spend unnecessary time trying to understand the intention or purpose behind the self-assignment.
1. **Potential for bugs**: Self-assignments can sometimes be a result of unintended code duplication or errors during refactoring. Although they don't cause any functional issues, they can introduce confusion and make it harder to spot actual bugs or unintended behaviors in the code.
1. **Compiler optimization**: The Go compiler is built to perform various optimizations to generate efficient code. It is capable of detecting and eliminating self-assignments during the compilation process. By removing self-assignments from the code, we allow the compiler to focus on more meaningful optimizations that can improve the performance of the program.

In summary, self-assignments in Go are not useful and should be removed from the code. They don't serve any purpose, reduce code readability, and can potentially introduce confusion or mask actual bugs. Removing self-assignments leads to cleaner and more maintainable code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    var foo int
    var bar int
    var baz int
    foo = foo
    foo, bar = foo, baz
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    var foo int
    var bar int
    var baz int
    foo = bar
    foo, bar = bar, baz
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 