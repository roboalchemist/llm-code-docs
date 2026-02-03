# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/angle-bracket-spacing.md

---
title: Avoid extra spaces inside Kotlin angle brackets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid extra spaces inside Kotlin angle brackets
---

# Avoid extra spaces inside Kotlin angle brackets

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/angle-bracket-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule enforces consistent spacing around angle brackets used for type parameters in Kotlin. It flags instances where there are unnecessary spaces immediately after the opening `<` or immediately before the closing `>`. Inconsistent or excessive spacing within generic type declarations can reduce code readability and deviate from standard Kotlin coding conventions, making the codebase harder to maintain and understand, especially in collaborative environments.

## How to remediate{% #how-to-remediate %}

To fix this issue, ensure that there are no extra spaces directly inside the angle brackets. Remove any space between the opening angle bracket (`<`) and the first type parameter, and between the last type parameter and the closing angle bracket (`>`). This practice promotes cleaner code that aligns with common Kotlin style guides, enhancing readability and consistency. For example, change `Map< Int, String >` to `Map<Int, String>`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val foo: Map< Int, String> = mapOf()

val bar: Map<Int, String > = mapOf()

val foo: Map< Int, String > = mapOf()

val baz: Set<String > = setOf()

val bin: Set< String, Pair< Int, String > > = setOf()
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val foo: Map<Int, String> = mapOf()

val bar: Map<Int, String> = mapOf()

val baz: Map<Int, String> = mapOf()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 