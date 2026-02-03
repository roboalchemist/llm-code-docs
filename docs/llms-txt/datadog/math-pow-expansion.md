# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/math-pow-expansion.md

---
title: Expand math.Pow calls
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Expand math.Pow calls
---

# Expand math.Pow calls

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/math-pow-expansion`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Simple operations such as `math.Pow` with a small number can be simplified. Simplification should be used when applicable.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    foo := math.Pow(x, 0)
    foo := math.Pow(x, 1)
    foo := math.Pow(x, 2)
    foo := math.Pow(x, 3)
    foo := math.Pow(x, 4)
    foo := math.Pow(x, 010)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    foo := 1
    foo := x
    foo := x*x
    foo := x*x*x
    foo := math.Pow(x, 4)
    foo := math.Pow(x, 010)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 