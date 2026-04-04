# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/time-parse-format.md

---
title: Avoid custom time format
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid custom time format
---

# Avoid custom time format

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/time-parse-format`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Make sure your code use a valid time format. See the [official Go documentation](https://pkg.go.dev/time#pkg-constant) for the valid time format.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    time.Parse("foobar", something)
    time.Parse("00", something_else);
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    time.Parse(time.ANSIC, something)
    time.Parse("2006-01-02", something_else)

    mytime := time.ANSIC
    time.Parse(mytime, another_thing)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
