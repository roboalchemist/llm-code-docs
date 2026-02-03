# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/extension-function-spacing.md

---
title: Enforce extension function spacing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce extension function spacing
---

# Enforce extension function spacing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/extension-function-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

To keep code consistently styled, ensure there are no superfluous spaces in extension function declarations.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun <T>  List<T>.printAll() {}
fun <T> List <T>.printAll() {}
fun <T> List<T> .printAll() {}
fun <T> List<T>. printAll() {}

fun String ?.printAll() {}

fun String? .printAll() {}
fun String?. printAll() {}

fun Foo .Bar.printAll() {}
fun Foo. Bar.printAll() {}
fun Foo.Bar .printAll() {}
fun Foo.Bar. printAll() {}

fun Foo.Bar.printAll () {}
fun Foo.Bar.printAll (
    
) {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun <T> List<T>.printAll() {}

fun String?.printAll() {}

fun Foo.Bar.printAll() {}

fun Foo.Bar.printAll(
    
) {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 