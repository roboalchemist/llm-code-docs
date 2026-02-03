# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/bad-nil-guard.md

---
title: Bad nil guard
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Bad nil guard
---

# Bad nil guard

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/bad-nil-guard`

**Language:** Go

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

This rule pertains to the improper use of nil checks in Go code. Nil checks are important in Go to prevent runtime panics that occur when you try to access fields or methods on nil values. The rule violations occur when the nil checks are incorrectly combined with other conditions, especially when using logical operators such as `&&` or `||`.

The improper use of nil checks can lead to confusing code and potential runtime errors. For instance, checking if a variable is nil and trying to access its field in the same condition `(X == nil && X.F)` is contradictory and will cause a runtime panic if X is indeed nil. Similarly, using the OR operator `(X != nil || X.F)` might lead to a runtime panic if X is nil, because the second condition will still be evaluated.

To avoid these issues, ensure that nil checks are done correctly **before** accessing any fields or methods. For example, when combining a nil check with other conditions, be sure to use the `&&` operator to ensure that the other conditions are only evaluated if the variable is not nil. Additionally, ensure the nil check occurs before a condition that accesses the field of a potentially nil variable. Following these practices will help to maintain the clarity of your code and avoid potential runtime panics.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main(req, http) {
    if (req == nil && req.Method == http.MethodGet) {
        // ...
    } else if (req != nil || req.Method == http.MethodPost){ 
        // ...
    } else if (req == nil && len(req.URL.Path) > 0){
        // ...
    } else if (req.Method == http.MethodDelete || req == nil) {
        // ...
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main(req, http) {
    if (req == nil) {
        // ...
    } else if (req != nil && len(req.URL.Path) > 0) {
        // ...
    } else if (req != nil && req.Method == http.MethodDelete) {
        // ...
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 