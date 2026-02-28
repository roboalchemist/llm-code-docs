# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/avoid-yoda-conditions.md

---
title: Put constants and values on the right
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Put constants and values on the right
---

# Put constants and values on the right

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/avoid-yoda-conditions`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

A "Yoda condition" is a notation style that places the constant or value on the left side of an equality check.

Standard notation:

```go
if something == 42 { }
```

Yoda notation:

```go
if 42 == something { }
```

This is sometimes used in interpreted programming languages to avoid the problem of accidental assignment. For example, in JavaScript, `if (something = 42)` assigns `something` to `42` instead of checking equality, and so using Yoda notation would throw a runtime error instead of introducing a logic error.

The Go compiler prevents this kind of mistake, so the more idiomatic standard notation should be preferred.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    if 51 == something {

    }

    if "myValue" == something {

    }

    if 0.0 == myValue && 0 == plop {

    }


    if 0.0 < myValue {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    if something == 51 {

    }

    if something == "myValue" {

    }

    if myValue == 0.0 && plop == 0 {

    }


    if 0.0 < myValue {

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
