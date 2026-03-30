# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/no-line-break-before-assignment.md

---
title: Prevents line break before assignment operator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevents line break before assignment operator
---

# Prevents line break before assignment operator

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/no-line-break-before-assignment`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Keeping the assignment operator on the same line as the value being assigned improves understandability of code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val concurrency // The number of coroutines to use
    = 6

fun sum(a: Int, b: Int): Int
    =      a + b

fun countFor(jobName: String?
= null): Int = 3

val (first, last)
    = getName()

class Router {
    val isEnabled get()
        = true
}

val generate: () -> String?
        // For now, just return null
        = { null }
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val concurrency = // The number of coroutines to use
    6

fun sum(a: Int, b: Int): Int =
    a + b

fun countFor(jobName: String? =
null): Int = 3

val (first, last) =
    getName()

class Router {
    val isEnabled get() =
        true
}

val generate: () -> String? =
        // For now, just return null
        { null }

fun sum(a: Int, b: Int): Int = a + b
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
