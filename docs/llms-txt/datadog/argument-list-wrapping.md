# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/argument-list-wrapping.md

---
title: All arguments should be on separate lines or the same line.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > All arguments should be on separate lines or the same line.
---

# All arguments should be on separate lines or the same line.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/argument-list-wrapping`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

All arguments should be on separate lines or the same line.

In long argument lists, put a line break after the opening parenthesis. Indent arguments, and group multiple closely related arguments near each other.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val foo =
    foo(
        a,
        b, c,
    )

val bar =
    foo(
        a,
        b, c, // hi
    )

    
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val foo =
    foo(
        a,
        b,
        c,
    )

val foo = foo(a, b, c)

private fun telemetryAttributes(
    element: PsiElement,
    logInfo: LogLineInfo
) = mapOf(
    "language" to element.language.id,
    "framework" to logInfo.framework, // deprecated - see IDE-3771 (suggest to remove after May-2025)
    "logs.framework" to logInfo.framework,
    "logs.level" to (logInfo.level?.label ?: "")
)

val servicesWithProfiling = client.profilingApi().findServicesWithProfiling(
                emptySet(),
                ctx.environment, // do we want to pass the env?
                ctx.timeInterval // use context interval
)

drawSquare(
    x = 10, y = 10,
)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 