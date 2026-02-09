# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/modifier-order.md

---
title: Enforce modifier ordering
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce modifier ordering
---

# Enforce modifier ordering

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/modifier-order`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule ensures that Kotlin modifier keywords are used in the correct order as defined by the Kotlin style guide.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
abstract class Foo {
    final public val foo = "foo"
    
    open protected val bar = "bar"

    open suspend internal fun baz(v: Any): Any = ""
}

abstract class A {
    open protected val v = ""

    open suspend internal fun f(v: Any): Any = ""

    lateinit protected var lv: String
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
abstract class Foo {
    public final val foo = "foo"

    protected open val bar = "bar"

    internal open suspend fun baz(v: Any): Any = ""
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 