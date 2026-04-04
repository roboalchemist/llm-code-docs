# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/boolean-get-function-name.md

---
title: Functions returning boolean should not use prefix get
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Functions returning boolean should not use prefix get
---

# Functions returning boolean should not use prefix get

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/boolean-get-function-name`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go programming, it is considered good coding practice to use the `is` or `has` prefix instead of `get` when naming functions that return a boolean value. This convention is suggested to improve code readability and maintainability.

The reason for this recommendation is that functions prefixed with `get` typically imply that they will return some value. Using `get` for a function that returns a boolean can be misleading and confusing for other developers who may expect it to return some non-boolean value.

By using the `is` or `has` prefix, it explicitly indicates that the function is intended to check the presence or state of a condition and will return a boolean value. This naming convention makes it easier for developers to understand the function's purpose and appropriately use it in their code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func getSomething() bool {

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func hasSomething() bool {

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
