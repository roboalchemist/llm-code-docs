# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/statement-wrapping.md

---
title: Statements should not be on same line as curly brace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Statements should not be on same line as curly brace
---

# Statements should not be on same line as curly brace

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/statement-wrapping`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

When using a multi-line statement with a curly brace, you should always put the contained code on a separate line from the curly brace.

The one exception to this is when using a lambda expression.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun doTask() { if (enabled) {
        spawn()
    }
}

val stringified = when (num) { /* comment */ 10 -> "Ten"
    20 -> "Twenty"
    else -> "Other"
}

durations.filter { d > 0 }.forEach { total += d
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun doTask() { 
    if (enabled) {
        spawn()
    }
}

val stringified = when (num) { 
    10 -> "Ten"
    20 -> "Twenty"
    else -> "Other"
}

// Single line block statements are ok
val double: (Int) -> Int = { a -> a * 2 }
enum class Status { OK, ERROR }

class Widget { // Comments are ok
    val enabled = true
    val kind = "mechanical"
}

durations.filter { d > 0 }.forEach {
    total += d
}

// It's fine to include params on a lamdba
val add: (Int, Int) -> Int = { a, b ->
    a + b
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 