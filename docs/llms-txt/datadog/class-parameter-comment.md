# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/class-parameter-comment.md

---
title: Enforce comment placement in class parameter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce comment placement in class parameter
---

# Enforce comment placement in class parameter

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/class-parameter-comment`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

When defining a class, comments should be placed on a separate line, before the class parameter they document.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
class Foo(
   foo: /** some kdoc */ String
)
class Bar(
    bar:
       // some comment
       String
)
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
class Foo(
    /** some kdoc */
    foo: String
)
class Bar(
    // some comment
    bar: String
)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 