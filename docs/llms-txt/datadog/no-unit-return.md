# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/no-unit-return.md

---
title: Enforce not returning Unit type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce not returning Unit type
---

# Enforce not returning Unit type

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/no-unit-return`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Explicitly returning `Unit` in Kotlin is generally redundant and not recommended. Kotlin automatically infers and returns `Unit` for functions that don't explicitly return a value.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun foo(): Unit{}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun foo() {}

fun bar(a: Int, b: Int): Int {
    return a + b
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 