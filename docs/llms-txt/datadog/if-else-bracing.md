# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/if-else-bracing.md

---
title: Enforce if/else expressions to use braces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce if/else expressions to use braces
---

# Enforce if/else expressions to use braces

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/if-else-bracing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule ensures that all `if/else` expressions in your Kotlin code are always enclosed in braces `{}`. This is important for readability and to prevent potential errors. When braces are omitted in `if/else` expressions, it can lead to confusion about which statements are included in the conditional block, especially in complex codebases.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun func(value: Int) {
    if (value > 0)
        foo()
    else if (value < 0) {
        bar()
    } else
        baz()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun func(value: Int) {
    if (value > 0) {
        foo()
    } else if (value < 0) {
        bar()
    } else {
        baz()
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
