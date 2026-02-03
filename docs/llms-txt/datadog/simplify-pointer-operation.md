# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/simplify-pointer-operation.md

---
title: Simplify pointer operation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Simplify pointer operation
---

# Simplify pointer operation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/simplify-pointer-operation`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Incorrect pointer manipulation can potentially lead to undefined behavior or introduce unnecessary complexity in the code. By understanding the correct usage of pointers and references, we can write cleaner and more maintainable code.

With the call `functionTakesPointer(&*pt1)`, the code attempts to take the address of the value pointed to by `pt1` and then dereference it. This operation doesn't serve any useful purpose and is redundant. It is considered best practice to simply pass the pointer itself without extra operators, as shown in the correct alternative, `functionTakesPointer(pt1)`.

Similarly, with `functionTakesValue(*&pt1)`, the code attempts to take the reference of `pt1` and then dereference it. Again, this operation is unnecessary and can lead to confusion for other developers reading the code. The correct alternative is to pass the value directly, without additional operators: `functionTakesValue(pt1)`.

To avoid these errors, remember the following good coding practices:

1. When passing pointers to functions, pass the pointer directly without unnecessary address-of or dereference operators.
1. When passing values to functions, pass values directly without unnecessary reference or dereference operators.
1. Focus on writing clear and concise code that accurately conveys your intentions to fellow developers.
1. Take advantage of code review and static analysis tools to identify and correct such mistakes early in the development process.

By following these practices, you can enhance the clarity and maintainability of your code, reducing the risk of introducing bugs and making it easier for others to read and understand your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    functionTakesPointer(&*pt1)
	functionTakesValue(*&pt1)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    functionTakesPointer(pt1)
	functionTakesValue(pt1)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 