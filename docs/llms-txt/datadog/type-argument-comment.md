# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/type-argument-comment.md

---
title: Enforce comment placement in type argument
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce comment placement in type argument
---

# Enforce comment placement in type argument

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/type-argument-comment`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

In type arguments, comments should be placed on a separate line, before the type argument they document.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun Foo<out /* some comment */ Any>.foo() {}
fun Foo<
    Any, // some comment
    Other
    >.foo() {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun Foo<
    /* some comment */ 
    out Any
    >.foo() {}
fun Foo<
    // some comment 
    out Any
    >.foo() {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 