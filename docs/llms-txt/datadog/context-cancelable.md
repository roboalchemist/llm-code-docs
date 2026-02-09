# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/context-cancelable.md

---
title: Call the context cancellation function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Call the context cancellation function
---

# Call the context cancellation function

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/context-cancelable`

**Language:** Go

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

In Go, it is important to call the cancellation function returned by the `context.WithTimeout` and `context.WithDeadline` functions. These functions are designed to create a new context that can be cancelled, thus the cancellation function needs to be called for proper cleanup.

This rule is crucial because not calling the cancellation function can lead to resource leaks. A context that is not cancelled will remain in memory until the parent context's cancellation function is called or the parent context's deadline expires. This could potentially lead to high memory usage, especially in long-running programs or services that create many contexts.

To adhere to this rule, always call the cancellation function when the work associated with the context is done. This can be achieved by using `defer` immediately after the context is created, or by explicitly calling the cancellation function when the work is done. Alternatively, in testing scenarios, you can use `t.Cleanup` to call the cancellation function after the test is completed.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    ctx, cancel := context.WithTimeout()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    ctx, cancel := context.WithTimeout();
    t.Cleanup(cancel);
}
```

```go
func main() {
    ctx, cancel := context.WithTimeout();
    cancel();
}
```

```go
func main() {
    ctx, cancel := context.WithTimeout();
    defer cancel();
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 