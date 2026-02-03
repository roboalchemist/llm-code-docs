# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/avoid-empty-critical-sections.md

---
title: Avoid empty critical sections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid empty critical sections
---

# Avoid empty critical sections

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/avoid-empty-critical-sections`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Empty critical sections are often a mistake. Instead of unlocking, developers often miss using `defer` to `defer` unlocking the mutex.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func test() {
    mutex.Lock()
    mutex.Unlock()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func test() {
    mutex.Lock()
    doSomething()
    mutex.Unlock()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 