# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/annotation-blank-line.md

---
title: Annotated declarations should be visually separated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Annotated declarations should be visually separated
---

# Annotated declarations should be visually separated

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/annotation-blank-line`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

When defining functions with annotations, separating them with a blank line provides more visual clarity.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
// Functions

fun parse() {}
@Benchmark
fun process() {

}

// Classes

annotation class Foo
@MustBeDocumented
@Repeatable
annotation class Bar

annotation class Foo
@MustBeDocumented
annotation class Bar(val info: String)

class Baz {
    fun parse() {}
    @Inject constructor() { }
}


fun parse() {}
@Entity
abstract class User {

}

fun parse() {}
@Entity
@Sample
class User {
    fun foo()
}

fun parse() {}
@Entity
sealed class User {

}

fun parse() {}
@Deprecated
fun interface SomeInterface {
    fun doSomething()
}

fun parse() {}
@Deprecated
interface Marker

fun parse() {}
@Deprecated
class Invalid : Exception()

fun parse() {}
@Deprecated
@Sample
abstract class Invalid: Exception()
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
// Functions

fun parse() {}

@Benchmark
fun process() {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
