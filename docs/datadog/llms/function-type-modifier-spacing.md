# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/function-type-modifier-spacing.md

---
title: Enforce function type spacing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce function type spacing
---

# Enforce function type spacing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/function-type-modifier-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

There should be a single space for type modifiers for a function type and the parameters or receiver.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
// Function type
val process: suspend() -> Unit = {}

// Function type with receiver
val process: suspend   String.() -> Unit = { println(this) }

// Function type with nullable receiver
val process: suspend   String?.() -> Unit = { if (this != null) println(this) }

// Nullable function type
val process: (suspend() -> Unit)? = null

// Function type as parameter
suspend fun execute(task: suspend  () -> Unit) { task() }
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
// Function type
val process: suspend () -> Unit = {}

// Function type with receiver
val process: suspend String.() -> Unit = { println(this) }

// Function type with nullable receiver
val process: suspend String?.() -> Unit = { if (this != null) println(this) }

// Nullable function type
val process: (suspend () -> Unit)? = null

// Function type as parameter
suspend fun execute(task: suspend () -> Unit) { task() }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
