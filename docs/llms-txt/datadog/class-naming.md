# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/class-naming.md

---
title: Class names should be upper camel case
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Class names should be upper camel case
---

# Class names should be upper camel case

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/class-naming`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Kotlin, it's a convention to name classes using upper camel case. This rule ensures that class names start with an uppercase letter and have no underscores. This helps enhances readability and allows for differentiation between class names and other identifiers in the code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
class foo
class Foo_Bar
class `Some class in the production code`
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
class Foo {}

class Foo1 {}

class FooBar {}

 // Any keyword is allowed when wrapped between backticks
class `class`
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
