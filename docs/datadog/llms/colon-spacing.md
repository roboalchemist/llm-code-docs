# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/colon-spacing.md

---
title: Enforce consistent spacing around colon
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce consistent spacing around colon
---

# Enforce consistent spacing around colon

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/colon-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule enforces consistent spacing around the colon in Kotlin code. In Kotlin, it's a common convention to have one space after the colon when declaring types. This applies to class inheritance, interfaces, and type declaration.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
class Foo:Bar

class Foo    :    Bar


// Subclass (Child Class)
class Dog(name: String)  : Animal(name) {

    // Overriding the function
    override fun makeSound() {
        println("$name barks")
    }
}


interface Pet :  Animal {
    fun play()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
class Foo : Bar

// Subclass (Child Class)
class Dog(name: String) : Animal(name) {

    // Overriding the function
    override fun makeSound() {
        println("$name barks")
    }
}


interface Pet : Animal {
    fun play()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
