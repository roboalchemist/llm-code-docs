# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/defer-lock.md

---
title: Do not defer Lock
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not defer Lock
---

# Do not defer Lock

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/defer-lock`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Deferring calls to `Mutex.Lock()` is nearly always a mistake, either by introducing a `defer` where it doesn't belong, or by mistyping `Unlock` as `Lock`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func test() {
    mutex.Lock()
    defer mutex.Lock()
}

func test() {
    defer mutex.Lock()
}

func test() {
    mutex.RLock()
    defer mutex.RLock()
}

func test() {
    defer mutex.RLock()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func test() {
    mutex.Lock()
    defer mutex.Unlock()
}

func test() {
    mutex.RLock()
    defer mutex.RUnlock()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
