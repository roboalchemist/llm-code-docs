# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/errors-new-errorf.md

---
title: Use fmt.Errorf instead of errors.New with fmt.Sprintf
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use fmt.Errorf instead of errors.New with fmt.Sprintf
---

# Use fmt.Errorf instead of errors.New with fmt.Sprintf

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/errors-new-errorf`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

You should use `fmt.Errorf("something %w", foo)` instead of `errors.New(fmt.Sprintf("something %s", foo))`.

Here are a few reasons why:

1. Error wrapping: By using `fmt.Errorf` with the `%w` format specifier instead of `%s`, your new error object wraps the original error. This makes it possible to access the original error object using `errors.Is` and `errors.As`.
1. Simplicity: The `fmt.Errorf` function simplifies the error message creation by combining the formatting and error wrapping in one function call. In contrast, using `errors.New(fmt.Sprintf("something %s", foo))` requires an extra step of formatting the string separately before creating the error.
1. Consistency: By consistently using `fmt.Errorf`, developers maintain a uniform approach to error handling and can easily recognize and handle errors throughout the codebase. Using a single idiomatic method rather than mixing different styles ensures consistency and improves code readability and maintainability.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func myFunc() error {
	foo := "foo"
	return errors.New(fmt.Sprintf("error: %s", foo))
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func myFunc() error {
	foo := "foo"
	return fmt.Errorf("error: %w", foo)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 