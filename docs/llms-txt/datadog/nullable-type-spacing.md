# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/nullable-type-spacing.md

---
title: Enforce nullable type spacing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce nullable type spacing
---

# Enforce nullable type spacing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/nullable-type-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

A type can be declared as nullable by appending a question mark (`?`) to the type name. The proper coding convention is to have no space between the type name and the question mark. This rule ensures that there is no space between the type and the question mark.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val foo: String ? = null
val foo: List<String ?> = listOf(null)
val foo: Map<String, String> ? = listOf(null);
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val foo: String? = null
val foo: List<String?> = listOf(null)
val foo: Map<String, String>? = listOf(null);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 