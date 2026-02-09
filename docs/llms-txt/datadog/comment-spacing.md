# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/comment-spacing.md

---
title: Enforce line comment spacing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce line comment spacing
---

# Enforce line comment spacing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/comment-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

To improve clarity, the `//` symbol of a line comment should be padded by at least one space on both sides.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val count: Int = 1//non-compliant
val count: Int = 2// non-compliant
val count: Int = 3 //non-compliant

//non-compliant

    //non-compliant
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val count: Int = 1 // compliant

// compliant

    // compliant
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 