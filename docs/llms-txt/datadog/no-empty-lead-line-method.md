# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/no-empty-lead-line-method.md

---
title: No leading empty lines in method blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > No leading empty lines in method blocks
---

# No leading empty lines in method blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/no-empty-lead-line-method`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

No leading empty lines in method blocks

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun foo() {

   val a = 2
   val b = 3
   println("bar")
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun foo() {
   val a = 2
   val b = 3
   print("bar")
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
