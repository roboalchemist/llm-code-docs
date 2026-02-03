# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/avoid-nil-check-loop.md

---
title: No need to check for nil before a loop
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > No need to check for nil before a loop
---

# No need to check for nil before a loop

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/avoid-nil-check-loop`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, if a slice is `nil`, it is considered empty (with a length of 0). When a `for range` loop is used on an empty slice, it simply executes zero times. Therefore, it is not necessary to check if the slice `s` is `nil` before using it in a `for range` loop.

Consider the following code snippets:Consider the following code snippets:

```go
func main () {
    if s != nil {
        for _, x := range s {
        
        }
    }
}
```

In the provided code, the `if` condition `s != nil` is checking if `s` is `nil` before executing the `for range` loop. However, this check is not necessary because even if `s` is `nil`, the loop will not execute. It is an unnecessary extra check that can be removed to make the code simpler and more readable.

Removing the `if` condition and directly using the `for range` loop will not impact the behavior of the code because the loop will simply not execute when `s` is `nil`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    if s != nil {
        for _, x := range s {
        
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    for _, x := range s {
    
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 