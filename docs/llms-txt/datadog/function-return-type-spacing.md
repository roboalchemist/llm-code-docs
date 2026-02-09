# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/function-return-type-spacing.md

---
title: Enforce function return type spacing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce function return type spacing
---

# Enforce function return type spacing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/function-return-type-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Kotlin enforces consistent spacing around the function return type: one space before the return type.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun foo1() : String = "some-result"

fun foo2():  String = "some-result"

fun foo3():String = "some-result"

fun foo4():
    String = "some-result"

fun foo5(bar: String):String = "some-result"

fun foo6() :String = "some-result"
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun foo(): String = "some-result"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 