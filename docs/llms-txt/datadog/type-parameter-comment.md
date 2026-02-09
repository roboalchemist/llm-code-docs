# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/type-parameter-comment.md

---
title: Avoid comments directly within Kotlin type parameters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid comments directly within Kotlin type parameters
---

# Avoid comments directly within Kotlin type parameters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/type-parameter-comment`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

In Kotlin, placing comments directly inside the angle brackets (`<...>`) of a type parameter declaration, such as `Foo<in /* some comment */ Bar>`, is considered poor code style. While this syntax is technically valid, it can significantly hinder code readability and disrupt consistent formatting, making it difficult for developers to quickly grasp the type's definition and its intent. This practice also deviates from standard conventions where type parameters are typically kept clean, containing only essential elements like variance modifiers and the type identifier.

## How to remediate{% #how-to-remediate %}

To ensure clearer and more maintainable code, move comments associated with type parameters outside the angle brackets. Comments can be placed on a separate line immediately before or after the type parameter definition, or within the containing declaration if they describe the type parameter's overall purpose. This approach maintains code readability and adheres to common Kotlin style guidelines, making the code easier to parse and understand for other developers.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
class Foo1<in /* some comment */ Bar>
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
class Foo1<
    /* some comment */ 
    out Bar
    >
class Foo2<
    // some comment 
    out Bar
    >
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 