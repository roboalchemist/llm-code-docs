# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/avoid-call-to-gc.md

---
title: Avoid calling the GC directly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid calling the GC directly
---

# Avoid calling the GC directly

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/avoid-call-to-gc`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, it is generally recommended to avoid using `runtime.GC()` and prevent direct calls to the garbage collector (GC). Here are a few reasons why:

1. Efficiency: Go's garbage collector is designed to automatically manage memory and determine when to run the garbage collection process based on the needs of the program. The Go runtime is optimized to efficiently handle garbage collection without manual intervention. Directly calling `runtime.GC()` can disrupt the optimized garbage collection process and potentially lead to performance issues.
1. Unpredictable Behavior: Calling the GC directly can introduce unpredictable behavior and potentially cause unintended consequences. The Go runtime employs a sophisticated garbage collector that operates based on heuristics and runtime conditions. Manually triggering the GC may interfere with the GC's ability to perform effective memory management and may not yield the expected results.
1. Code Readability and Simplicity: Directly calling the GC makes the code more complex and harder to understand. It can obscure the underlying memory management and make the code less maintainable. The Go language promotes writing clean, readable code, and relying on the automatic garbage collector helps maintain this simplicity and readability.
1. Focus on Algorithmic Optimization: Instead of manually calling the GC, it is generally better to focus on algorithmic optimization and writing efficient code. Optimizing data structures, reducing unnecessary allocations, and managing resources effectively can have a more significant impact on the performance of a Go program compared to manual GC calls.

In most cases, it is best to rely on Go's automatic garbage collector and let it handle memory management. Trusting the runtime's automatic GC ensures efficient memory usage and allows developers to focus on writing clear, maintainable code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    runtime.GC()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
