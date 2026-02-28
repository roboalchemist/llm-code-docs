# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/final-newline.md

---
title: Enforce final newline
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce final newline
---

# Enforce final newline

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/final-newline`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule enforces the inclusion of a final newline at the end of every file. Many command-line utilities expect or require the presence of a final newline to function correctly.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
package main

fun main(args : Array<String>) {
    println("Hello world!")
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
package main

fun main(args : Array<String>) {
    println("Hello world!")
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
