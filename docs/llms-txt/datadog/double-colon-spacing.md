# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/double-colon-spacing.md

---
title: Enforce spacing around double colons
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce spacing around double colons
---

# Enforce spacing around double colons

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/double-colon-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

In callable references, there should be no spaces separating the class, instance, method, or property from the double colons (`::`).

An expression like `List::filter` is correct, while `List :: filter` is not.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val clz1 = Foo ::class
val clz2 = Foo:: class
val clz3 = Foo :: class

val filter1 = List ::filter
val filter2 = List:: filter
val filter3 = List :: filter

val constr = :: Regex
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val filter = List::filter
val clz = Foo::class
val constr = ::Regex
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 