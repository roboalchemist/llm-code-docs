# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/mod-one-always-zero.md

---
title: Replace var % 1 by 0
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Replace var % 1 by 0
---

# Replace var % 1 by 0

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/mod-one-always-zero`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

A modulus operation `%` with a constant value (1) on the variable `foo` and then checks if the result is equal to 0. Writing `myVariable % 1` is equivalent to writing `0`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    v := foo % 1
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    v := foo % 2
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 