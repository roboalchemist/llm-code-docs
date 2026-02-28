# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/unary-operator-spacing.md

---
title: Enforce unary operator spacing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce unary operator spacing
---

# Enforce unary operator spacing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/unary-operator-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

It is recommended to have no spaces around unary operators.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun foo1(i: Int) = i ++

fun foo2(i: Int) = ++ i

fun foo3(i: Int) = ++
    i
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun foo1(i: Int) = i++

fun foo2(i: Int) = ++i

fun foo3(i: Int) = ++i
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
