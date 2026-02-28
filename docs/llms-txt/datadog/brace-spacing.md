# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/brace-spacing.md

---
title: Enforce brace spacing for lambdas
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce brace spacing for lambdas
---

# Enforce brace spacing for lambdas

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/brace-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

In lambda expressions, there should be a space separating each brace from the function's body. If the function takes parameters, there should also be a space on either side of the arrow.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val values = list.filter {it > 10}
val values = list.filter { x->x > 10 }
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val values = list.filter { it > 10 }
val values = list.filter { x -> x > 10 }
val values = list.filter int@{ it > 10 }
val values = list.filter {
    it > 10
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
