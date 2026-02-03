# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/enum-wrapping.md

---
title: Enums should be a single line or one entry per line.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enums should be a single line or one entry per line.
---

# Enums should be a single line or one entry per line.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/enum-wrapping`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

An enum should be a single line, or each enum entry has to be placed on a separate line. In case the enumeration contains enum entries and declarations those are to be separated by a blank line.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
enum class Foo {
    A,
    B, C,
    D
}

enum class Foo {
    A;
    fun foo() = "foo"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
enum class Foo { A, B, C, D }

enum class Foo { 
    A, 
    B,
    C, 
    D 
}

enum class Foo {
    A,
    B,
    C,
    D,
    ;

    fun foo() = "foo"
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 