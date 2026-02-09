# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/signal-trapped.md

---
title: Invalid signal being trapped
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Invalid signal being trapped
---

# Invalid signal being trapped

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/signal-trapped`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Using `signal.Ignore(syscall.SIGKILL)` or `signal.Reset(os.Kill)` to handle the `SIGKILL` signal is not considered good practice because the `SIGKILL` signal is designed to be uncatchable and unignorable.

In most operating systems, including Unix-based systems, the `SIGKILL` signal is a special signal that cannot be caught, ignored, or handled by any process. It is intended as a forceful termination signal that immediately terminates a process without allowing it to perform any cleanup or additional operations.

Therefore, attempting to ignore or reset the `SIGKILL` signal using `signal.Ignore(syscall.SIGKILL)` or `signal.Reset(os.Kill)` will have no effect. The process will still be forcefully terminated when a `SIGKILL` signal is sent to it.

It is generally not recommended to handle the `SIGKILL` signal programmatically because it defeats the purpose of the signal itself, which is to guarantee the immediate termination of a process if needed.

Handling other signals, such as `SIGINT` or `SIGTERM`, can be useful to gracefully shut down a process and perform necessary cleanup operations before termination. However, `SIGKILL` signals should not be caught or ignored as they are meant to forcefully terminate processes without any chance of intervention.

In conclusion, it is not good coding practice to use `signal.Ignore(syscall.SIGKILL)` or `signal.Reset(os.Kill)` to handle the `SIGKILL` signal, as it is not catchable or ignorable by design.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    signal.Ignore(os.Signal(signal.SIGKILL))
    signal.Ignore(os.Kill)
    signal.Reset(os.Kill)
    signal.Ignore(syscall.SIGKILL)
    signal.Notify(p, syscall.SIGKILL)
    signal.Notify(p, os.SIGKILL)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    signal.Notify(p, os.SIGUSR1)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 