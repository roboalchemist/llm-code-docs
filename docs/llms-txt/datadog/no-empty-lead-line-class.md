# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/no-empty-lead-line-class.md

---
title: No blank lines at the start of a class
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > No blank lines at the start of a class
---

# No blank lines at the start of a class

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/no-empty-lead-line-class`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule is in place to ensure that Kotlin classes do not begin with unnecessary blank lines. The presence of blank lines at the start of a class can lead to confusion and can make the code harder to read. It breaks the flow of the code and can make it less intuitive to understand the structure of the class.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin




class Foo {

    val foo = "foo"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
class Foo {
    val bar = "bar"
    val foo = "foo"
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 