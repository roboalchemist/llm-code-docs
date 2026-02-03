# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/annotation-spacing.md

---
title: Enforce annotation separation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce annotation separation
---

# Enforce annotation separation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/annotation-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Each annotations should be placed on a separate line. This is important because it makes the code more readable and easier to understand. When multiple annotations are placed on the same line, it can become difficult to distinguish between them and understand their individual impacts on the associated code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
@JvmField

fun foo() {}

@Foo @Bar
/**
 * block comment
 */
class FooBar {
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
@Serializable
class CreateActionRequest {
    @Suppress("unused") // All fields are required
    @Serializable
    private class Data(val id: String, val attributes: Attributes) {
        @EncodeDefault
        val type = "something"
    }
}
```

```kotlin
@JvmField
fun foo() {}

@JvmField
fun foo(
    x: Int
) {}

/**
 * block comment
 */
@Foo
class FooBar {
}

@Foo
@Bar
class FooBar {
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 