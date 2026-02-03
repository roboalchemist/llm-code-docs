# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/multiline-loop.md

---
title: Braces required for multiline for, while, and do statements.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Braces required for multiline for, while, and do statements.
---

# Braces required for multiline for, while, and do statements.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/multiline-loop`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Braces are required for multiline `for`, `while`, and `do` statements.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
for (i in 1..10)
    println(i)

var i = 0
while (i < 5) 
  println(i)
  i++

do 
    val foo = bar()
while (foo != null) 
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
for (i in 1..10) {
    println(i)
}

var i = 0
while (i < 5) {
  println(i)
  i++
} 

do {
    val foo = bar()
} while (foo != null) 
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 