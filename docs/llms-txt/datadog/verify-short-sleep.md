# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/verify-short-sleep.md

---
title: Sleep is in nanoseconds by default; verify short sleep
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Sleep is in nanoseconds by default; verify short sleep
---

# Sleep is in nanoseconds by default; verify short sleep

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/verify-short-sleep`

**Language:** Go

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Go, the function `time.Sleep` is used to pause the execution of a program for a specified duration. The duration is typically specified using a `time.Duration` value, which represents a length of time.

Calling `time.Sleep` with a small number as the argument can lead to inefficient or unpredictable behavior in a program. This is because the argument is interpreted as a duration in nanoseconds, and using a small number can cause the program to consume excessive CPU resources or introduce unnecessary delays.

Here are some good coding practices to avoid calling `time.Sleep` with a small number:

1. Avoid using a plain number as the argument: Instead of passing a small number directly to `time.Sleep`, use the `time.Duration` type to specify the desired duration explicitly. This will make the code more readable and maintainable.
1. Prefer using predefined durations: Go provides predefined durations like `time.Second`, `time.Millisecond`, and `time.Microsecond`. These constants define durations in a more human-readable and understandable way. Use these constants to specify the desired delay rather than using arbitrary small values.
1. Calculate durations dynamically: If you need to specify a small delay that is less than a predefined duration, you can calculate it dynamically using multiplication or division. For example, instead of using `time.Sleep(100)`, you can use `time.Sleep(100 * time.Millisecond)` to achieve the same effect in a more accurate and maintainable way.
1. Consider alternative approaches: In some cases, using `time.Sleep` may not be the most appropriate solution. If you need to introduce delays between operations, consider using channels, timers, or other concurrency primitives provided by the Go language. These constructs can offer more granular control over scheduling and coordination.

By following these good coding practices, you can ensure that the use of `time.Sleep` in Go is efficient and predictable, avoiding any unintended side effects caused by calling it with a small number as an argument.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import ("time")

func main(){
    time.Sleep(1)
    time.Sleep(9000)
    time.Sleep(100 * time.Millisecond)
    time.Sleep(5 * time.Nanosecond)

    fmt.Println("done sleeping")
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 