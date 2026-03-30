# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/function-name-min-length.md

---
title: Avoid very short function names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid very short function names
---

# Avoid very short function names

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/function-name-min-length`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Function names should be descriptive of the function behavior and functionalities. Instead of using a very short name, always have a name that indicates what the function is doing.

## Arguments{% #arguments %}

- `min-length`: Minimum length for function names. Default: 2.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun a() {

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun valid() {

}

infix fun to() {

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
