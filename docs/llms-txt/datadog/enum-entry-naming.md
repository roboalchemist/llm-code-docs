# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/enum-entry-naming.md

---
title: Kotlin enum entries must follow naming conventions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Kotlin enum entries must follow naming conventions
---

# Kotlin enum entries must follow naming conventions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/enum-entry-naming`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule enforces consistent naming conventions for enum entries in Kotlin, aligning with established community guidelines. Adhering to a standard naming style, such as UPPER_SNAKE_CASE or UpperCamelCase, significantly improves code readability and maintainability. Inconsistent naming can lead to confusion, making it harder for developers to quickly understand the purpose and intent of enum members. Violations occur when enum entries do not follow either of these recommended patterns.

## How to remediate{% #how-to-remediate %}

To fix this issue, ensure all enum entries follow either UPPER_SNAKE_CASE (all uppercase letters with words separated by underscores, for example, `MY_ENUM_ENTRY`) or UpperCamelCase (also known as PascalCase, where each word starts with an uppercase letter and no underscores, for example, `MyEnumEntry`). Choose one style and apply it consistently across your enum definitions for clarity and uniformity. tests:

- filename: NonCompliantCode.kt code: |- enum class Foo { foo, bAr, Foo_Bar, } annotation_count: 3
- filename: CompliantCode.kt code: |- enum class Foo { FOO, Foo, FOO_BAR, FooBar, } annotation_count: 0

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
enum class Foo {
    foo,
    bAr,
    Foo_Bar,
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
enum class ProductDetectionStatus {
    @SerialName("detected")
    DETECTED,

    @SerialName("undetected")
    UNDETECTED
}
```

```kotlin
enum class Foo {
    FOO,
    Foo,
    FOO_BAR,
    FooBar,
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
