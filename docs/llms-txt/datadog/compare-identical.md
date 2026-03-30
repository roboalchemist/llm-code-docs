# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/compare-identical.md

---
title: Prevent identical comparison
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent identical comparison
---

# Prevent identical comparison

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/compare-identical`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Avoid comparing the same expression, it always results to `true`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    if a == a {

    }

    if a == b {

    }

    if (1 + 2) == (1 + 2) {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    if a == b {

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
