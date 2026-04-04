# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/no-finalizers-on-exit.md

---
title: Avoid using runtime finalizers on exit
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using runtime finalizers on exit
---

# Avoid using runtime finalizers on exit

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-security/no-finalizers-on-exit`

**Language:** Kotlin

**Severity:** Error

**Category:** Security

**CWE**: [833](https://cwe.mitre.org/data/definitions/833.html)

## Description{% #description %}

This ensures the proper termination of Kotlin programs. It is generally considered unsafe to use the `System.runFinalizersOnExit(true)` method because it can lead to unpredictable program behavior. This method forces all objects undergoing finalization to be finalized when the JVM exits, which can cause problems if an object is in the middle of a critical operation.

Instead of `System.runFinalizersOnExit(true)`, you can use the Java Runtime API's `addShutdownHook` method. This method registers a new virtual-machine shutdown hook, meaning it adds a thread to run when the JVM begins its shutdown sequence. This allows you to handle any cleanup actions yourself, providing a safer and more predictable termination process.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun foo() {
  System.runFinalizersOnExit(true)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun main() {
    Runtime.getRuntime().addShutdownHook(object : Thread() {
        override fun run() {
            handleShutdown()
        }
    })
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
