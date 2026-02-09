# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/check-len.md

---
title: Check to prevent a length less than 0
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check to prevent a length less than 0
---

# Check to prevent a length less than 0

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/check-len`

**Language:** Go

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

In Go, the built-in `len()` function returns the length of a slice, map, or string, and it never produces a negative value. The length of any data structure in Go is always a non-negative integer.

Hence, the condition `len(mySlice) < 0` will always evaluate to false, and the code block within the if statement will never execute.

To fix this issue, you should remove the unnecessary check for `len(mySlice) < 0`:

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    if len(mySlice) < 0 {
        // never occurs
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    if len(mySlice) == 0 {
        
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 